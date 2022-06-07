# Programming Exercise 10-4

from EmployeeDefinition import *

def main():
    # Create three instances of Employee
    emplo1 = Employee('Susan Meyers', '47899',
                        'Accounting', 'Vice President')
    emplo2 = Employee('Mark Jones', '39119',
                        'IT', 'Programmer')
    emplo3 = Employee('Joy Rogers', '81774',
                        'Manufacturing', 'Engineer')

    print(f"Employee 1:{emplo1}\n")
    print(f"Employee 2:{emplo2}\n")
    print(f"Employee 3:{emplo3}\n")

# Call the main function.
if __name__ == '__main__':
    main()
