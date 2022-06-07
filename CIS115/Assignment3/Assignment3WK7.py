##Michael Mumme, Assignment 3, Salaries
##This program calculates money per day worked, collective total, and only accepts number from 2-50 inclusive.

dailySalary = 0.01
numberDays = int(input("Enter number of days: "))
totalSalary = 0

while numberDays < 2 or 50 < numberDays:
    print("Number must be between 2-50")
    numberDays = int(input("Enter number of days: "))

print("Day \t\t    Salary for the Day \n-------------------------------------")

for control in range(1, numberDays + 1, 1):
    print(f"{control} \t\t\t ${dailySalary}")
    totalSalary += dailySalary
    dailySalary *= 2

print(f"The total salary for {numberDays} days is ${totalSalary:.2f}")
    

##Enter number of days: 0
##Number must be between 2-50
##Enter number of days: 100
##Number must be between 2-50
##Enter number of days: 10
##Day 		    Salary for the Day 
##-------------------------------------
##1 			 $0.01
##2 			 $0.02
##3 			 $0.04
##4 			 $0.08
##5 			 $0.16
##6 			 $0.32
##7 			 $0.64
##8 			 $1.28
##9 			 $2.56
##10 			 $5.12
##The total salary for 10 days is $10.23

##Enter number of days: -1
##Number must be between 2-50
##Enter number of days: 55
##Number must be between 2-50
##Enter number of days: 5
##Day 		    Salary for the Day 
##-------------------------------------
##1 			 $0.01
##2 			 $0.02
##3 			 $0.04
##4 			 $0.08
##5 			 $0.16
##The total salary for 5 days is $0.31
