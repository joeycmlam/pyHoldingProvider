class Position:

    holdings = ''
    mv = 0

    def __init__(self):
        print ('init')
        self.loadHolding()
        self.mv = 1000

    def loadHolding(self):
        self.holdings = 'xxx'

    def getHolding(self):
        return self.holdings

    def getMV(self):
        return self.mv

def main():
    print('test')
    p = Position()
    print('MV', p.getMV())

if __name__ == '__main__':
    main()
