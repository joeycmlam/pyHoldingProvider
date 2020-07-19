import pgConnection

class Position:

    holdings = None
    mv = 0
    db = None

    def __init__(self):
        print ('init')
        self.db = pgConnection.dbConnection()

    def loadHolding(self):
        self.holdings = self.db.execSQL('select stock_code, quantity, bookcost from holding')

    def getHolding(self):
        self.loadHolding()
        return self.holdings

    def getMV(self):
        return self.mv

def main():
    print('test')
    p = Position()
    holdings = p.getHolding()
    for aRecord in holdings:
        print(aRecord)

if __name__ == '__main__':
    main()
