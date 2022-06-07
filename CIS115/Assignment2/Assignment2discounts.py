##Michael Mumme, Assignment 2, Maya Tolappa
##This program will use the number of packages purchased to calculate the
##quantity purchased, full price, discount rate, discount amount, and the final price.

numberPackages = int(input("Number of packages: "))
pricePackage = 99.99
if numberPackages < 0 or numberPackages > 300:
    print("The number of packages must be between 0-300")
else: #The program is within the number parameters set (0-300)
    if numberPackages < 10:
        fullPrice = numberPackages * pricePackage
        discountAmount = fullPrice * 0.0
        finalPrice = fullPrice - discountAmount
        print(f"Quantity Purchased: {numberPackages}")
        print(f"Full Price: ${fullPrice}")
        print("Discount Rate: 0%")
        print(f"Discount Amount: ${discountAmount:.2f}")
        print(f"Final Price: ${finalPrice:.2f}")
    else:
        if numberPackages < 20:
            fullPrice = numberPackages * pricePackage
            discountAmount = fullPrice * 0.1
            finalPrice = fullPrice - discountAmount
            print(f"Quantity Purchased: {numberPackages}")
            print(f"Full Price: ${fullPrice:.2f}")
            print("Discount Rate: 10%")
            print(f"Discount Amount: ${discountAmount:.2f}")
            print(f"Final Price: ${finalPrice:.2f}")
        else:
            if numberPackages < 50:
                fullPrice = numberPackages * pricePackage
                discountAmount = fullPrice * 0.2
                finalPrice = fullPrice - discountAmount
                print(f"Quantity Purchased: {numberPackages}")
                print(f"Full Price: ${fullPrice:.2f}")
                print("Discount Rate: 20%")
                print(f"Discount Amount: ${discountAmount:.2f}")
                print(f"Final Price: ${finalPrice:.2f}")
            else:
                if numberPackages < 100:
                    fullPrice = numberPackages * pricePackage
                    discountAmount = fullPrice * 0.3
                    finalPrice = fullPrice - discountAmount
                    print(f"Quantity Purchased: {numberPackages}")
                    print(f"Full Price: ${fullPrice:.2f}")
                    print("Discount Rate: 30%")
                    print(f"Discount Amount: ${discountAmount:.2f}")
                    print(f"Final Price: ${finalPrice:.2f}")
                else:
                        fullPrice = numberPackages * pricePackage
                        discountAmount = fullPrice * 0.4
                        finalPrice = fullPrice - discountAmount
                        print(f"Quantity Purchased: {numberPackages}")
                        print(f"Full Price: ${fullPrice:.2f}")
                        print("Discount Rate: 40%")
                        print(f"Discount Amount: ${discountAmount:.2f}")
                        print(f"Final Price: ${finalPrice:.2f}")
        
print("eop")

##SAMPLE ONE
##Number of packages: 5
##Quantity Purchased: 5
##Full Price: $499.95
##Discount Rate: 0%
##Discount Amount: $0.00
##Final Price: $499.95

##SAMPLE TWO
##Number of packages: 15
##Quantity Purchased: 15
##Full Price: $1499.85
##Discount Rate: 10%
##Discount Amount: $149.98
##Final Price: $1349.87

##SAMPLE THREE
##Number of packages: 200
##Quantity Purchased: 200
##Full Price: $19998.0
##Discount Rate: 40%
##Discount Amount: $7999.20
##Final Price: $11998.80

##SAMPLE FOUR
##Number of packages: 55
##Quantity Purchased: 55
##Full Price: $5499.45
##Discount Rate: 30%
##Discount Amount: $1649.83
##Final Price: $3849.61

##SAMPLE FIVE
##Number of packages: -1
##The number of packages must be between 0-300
##
##SAMPLE SIX
##Number of packages: 400
##The number of packages must be between 0-300
