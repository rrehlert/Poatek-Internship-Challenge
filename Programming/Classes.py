class FuelPump:
    def __init__(self, price, quantity):
        self.__fuelPrice = price          #added underscores in names to make them private variables
        self.__fuelQuantity = quantity

    def setPrice(self, price):
        if price >= 0:
            self.__fuelPrice = price
            #print(f"Price set at {self.__fuelPrice}")       #Debug purposes
            return price
        else:
            #print(f"Price cannot be negative")       #Debug purposes   
            return 0
        

    def get_price(self):
        #print(f"Price is {self.__fuelPrice}")       #Debug purposes
        return self.__fuelPrice        

    def setQuantity(self, quantity):
        if quantity >= 0:
            self.__fuelQuantity = quantity
            return quantity
            #print(f"Liters available {self.__fuelQuantity}")        #Debug purposes
        else:
            #print(f"Quantity cannot be negative")       #Debug purposes       
            return 0

    def get_quantity(self):
        #print(f"Liters available {self.__fuelQuantity}")        #Debug purposes
        return self.__fuelQuantity        

    def check_fuel_by_price(self, price):
        liters = price / self.get_price()
        liters_available = self.get_quantity()
        #print(f"Price requested: {price}, Liters wanted: {liters}, Liters available: {liters_available} ")        #Debug purposes
        if liters_available >= liters:
            #print("Check OK")       #Debug purposes
            return liters    
        else:
            #print("Check not OK")       #Debug purposes
            return 0
            

    def check_fuel_by_liters(self, liters):
        liters_available = self.get_quantity()
        #print(f"Liters wanted: {liters}, Liters available: {liters_available}")     #Debug purposes
        if liters_available >= liters:
            price = liters * self.get_price()
            #print("Check OK")       #Debug purposes
            return price
        else:
            #print("Check not OK")       #Debug purposes
            return 0

    def __pump_liters(self, liters):
        self.__fuelQuantity = self.__fuelQuantity - liters
        #print(f"Liters pumped {liters}")        #Debug purposes
        #print(f"Liters available {self.__fuelQuantity}")        #Debug purposes

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