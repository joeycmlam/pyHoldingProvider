
class Holding:

    def __init__(self, stock_code, quantity, bookcost):
        self.stock_code = stock_code
        self.quantity = quantity
        self.bookcst = bookcost

    def __str__(self):
        return "Holding: stock_code = [%s], " \
               "quantity = [%d] bookcost = [%d]" % (self.stock_code, self.quantity, self.bookcst)