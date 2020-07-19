import pgConnection
import json
import sys
from decimal import Decimal

class CustomJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(CustomJsonEncoder, self).default(obj)

class Holding:
    def __init__(self, stock_code, quantity, bookcost):
        self.stock_code = stock_code
        self.quantity = 0
        self.bookcost = 0


class Position:

    holdings = None
    mv = 0
    db = None

    def __init__(self):
        self.db = pgConnection.dbConnection()

    def loadHolding(self):
        result = self.db.execSQL('select stock_code, quantity, bookcost from holding')
        return result

    def getHolding(self):
        try:
            self.holdings = []
            dbResult = self.loadHolding()
            for aRecord in dbResult:
                #h = Holding(stock_code=aRecord[0], quantity=aRecord[1], bookcost=aRecord[2])
                jsonStr = json.dumps(aRecord, cls=CustomJsonEncoder)
                self.holdings.append(aRecord)
        except (Exception) as err:
            print(err)
            self.holdings = None

        return self.holdings

    def getMV(self):
        return self.mv

    def getHoldingJosn(self):
        result = json.dumps(self.holdings, cls=CustomJsonEncoder)
        return result

def main():
    try:
        p = Position()
        result = p.getHolding()
        print(p.getHoldingJosn())
    except (Exception) as err:
        sys.exit(err)


if __name__ == '__main__':
    main()
