from Car import *
def main():
    # Create an instance of Car
    my_car = Car("2008", "Honda Accord")
    print(f"my_car after instantiating: {my_car}")

    my_car.setSpeed(116)
    print(f"my_car after my_car.setSpeed(116): {my_car}")

    my_car.setSpeed(136)
    print(f"my_car after my_car.setSpeed(136): {my_car}")
    
    # Accelerate 4 times
    print ("*** car is accelerating ***")
    for i in range(4):
        my_car.accelerate()
        print ("Current speed: ", my_car.getSpeed())

    my_car.setSpeed(11)
    print(f"my_car after my_car.setSpeed(11): {my_car}")
  
    # Brake 3 times
    print ("*** car is braking ***")
    for i in range(3):
        my_car.brake()
        print ("Current speed: ", my_car.getSpeed())

    print(f"my_car at program end: {my_car}")

if __name__ == "__main__":
    main()
