class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price is {}".format(self.__maxprice))
    def setmaxprice(self, price):
        self.maxprice = price
c = computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setmaxprice(1000)
c.sell()