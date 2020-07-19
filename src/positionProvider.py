import pgConnection
import holding
import json
from decimal import Decimal
import sys


def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

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
                h = holding.Holding(stock_code=aRecord[0], quantity=aRecord[1], bookcost=aRecord[2])
                print(h)
                self.holdings.append(h)
        except (Exception) as err:
            print(err)
            self.holdings = None

        return self.holdings

    def getMV(self):
        return self.mv

    def getHoldingJosn(self, lstHolding):
        result = json.dumps(lstHolding)


def main():
    try:
        p = Position()
        result = p.getHolding()
        print(p.getHoldingJosn(result))
    except (Exception) as err:
        sys.exit(err)


if __name__ == '__main__':
    main()
