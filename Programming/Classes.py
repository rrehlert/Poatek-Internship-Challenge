class FuelPump:
    def __init__(self, price, quantity):
        self.__fuelPrice = price          #added underscores in names to make them private variables
        self.__fuelQuantity = quantity

    def setPrice(self, price):
        if price >= 0:
            self.__fuelPrice = price
            return price
        else:  
            return 0
        

    def get_price(self):
        return self.__fuelPrice        

    def setQuantity(self, quantity):
        if quantity >= 0:
            self.__fuelQuantity = quantity
            return quantity
        else:     
            return 0

    def get_quantity(self):
        return self.__fuelQuantity        

    def check_fuel_by_price(self, price):
        liters = price / self.get_price()
        liters_available = self.get_quantity()
        if liters_available >= liters:
            return liters    
        else:
            return 0
            

    def check_fuel_by_liters(self, liters):
        liters_available = self.get_quantity()
        if liters_available >= liters:
            price = liters * self.get_price()
            return price
        else:
            return 0

    def __pump_liters(self, liters):
        self.__fuelQuantity = self.__fuelQuantity - liters

    def fillWithPrice(self, price):
        if not price or price < 0:
            return 0
        else:    
            liters = self.check_fuel_by_price(price)
            if not liters:
                return 0
            else:
                self.__pump_liters(liters)
                return liters
    
    def fillWithLiters(self, liters):
        if not liters or liters < 0:
            return 0
        else:
            price = self.check_fuel_by_liters(liters)
            if not price or not liters:
                return 0
            else:
                self.__pump_liters(liters)
                return price

if __name__ == "__main__":
    pump = FuelPump(5,250)
    print(pump.get_price())
    print(pump.get_quantity())
    print(pump.setQuantity(-250))
    print(pump.setPrice(7))
    print(pump.get_price())
    print(pump.setQuantity(200))
    print(pump.get_quantity())
    print(pump.fillWithLiters(50))
    print(pump.fillWithPrice(35))
    print(pump.get_quantity())
    print(pump.fillWithLiters(150))