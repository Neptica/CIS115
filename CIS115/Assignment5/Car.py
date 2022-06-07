class Car:
    __make_model = ""
    __year = ""
    __speed = 0
        
    #my_car = CarDefinition.Car("2008", "Honda Accord")
    def __init__(self, param_year, param_make_model):
        self.__make_model = param_make_model
        self.__year = param_year
        self.__speed = 0

    ############# make_model################
    def setMake_model(self, param_make_model):
        self.__make_model = param_make_model

    def getMake_model(self):
        return self.__make_model

    ############# Make################
    def setYear(self, param_year):
        self.__year = make

    def getYear(self):
        return self.__year
    
    ############# speed################
    def setSpeed(self, inp_speed):
        if inp_speed < 0 or inp_speed > 130:
            print(f"Speed cannot be {inp_speed} mph.",
                  "Speed be must be 0-130 mph")
        else:
            self.__speed = inp_speed

    def getSpeed(self):
        return self.__speed

    
    ############## accelerate function ############
    def accelerate(self):
        self.__speed += 6
        if self.__speed > 130:
            print(f"Error speed cannot be {self.__speed} since it is greater than 130 mph. Resetting to 130 mph")
            self.__speed = 130

            

    ############## brake function ################
    def brake(self):
        self.__speed -= 8
        if self.__speed < 0:
            print(f"Error speed cannot be {self.__speed} since it is less than 0 mph. Resetting to 0 mph")
            self.__speed = 0

        
    ############# str ############
    def __str__(self):
        ret_val = f"Year : {self.__year}"
        ret_val += f", Make and Model : {self.__make_model}"
        ret_val += f", Speed : {self.__speed}"
        return ret_val

##my_car after instantiating: Year : 2008, Make and Model : Honda Accord, Speed : 0
##my_car after my_car.setSpeed(116): Year : 2008, Make and Model : Honda Accord, Speed : 116
##Speed cannot be 136 mph. Speed be must be 0-130 mph
##my_car after my_car.setSpeed(136): Year : 2008, Make and Model : Honda Accord, Speed : 116
##*** car is accelerating ***
##Current speed:  122
##Current speed:  128
##Error speed cannot be 134 since it is greater than 130 mph. Resetting to 130 mph
##Current speed:  130
##Error speed cannot be 136 since it is greater than 130 mph. Resetting to 130 mph
##Current speed:  130
##my_car after my_car.setSpeed(11): Year : 2008, Make and Model : Honda Accord, Speed : 11
##*** car is braking ***
##Current speed:  3
##Error speed cannot be -5 since it is less than 0 mph. Resetting to 0 mph
##Current speed:  0
##Error speed cannot be -8 since it is less than 0 mph. Resetting to 0 mph
##Current speed:  0
##my_car at program end: Year : 2008, Make and Model : Honda Accord, Speed : 0
