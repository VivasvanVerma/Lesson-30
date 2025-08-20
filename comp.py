class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: ", self.__maxprice)
    def Setmaxprice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.Setmaxprice(1000)
c.sell()