##Michael Mumme, Employee Information through classes -- Lab 5

class Employee:
    __empName = "-na-"
    __idNumber = '0'
    __department = "-na-"
    __title = "-na-"
    
    def __init__(self, inp_empName, inp_idNumber, inp_dept, inp_title):
        self.__empName = inp_empName
        self.__idNumber = inp_idNumber
        self.__department = inp_dept
        self.__title = inp_title
        
    def setEmpName(self, inp_empName):
        self.__empName = inp_empName

    def setIdNumber(self, inp_idNumber):
        self.__idNumber = inp_idNumber

    def setDepartment(self, inp_dept):
        self.__department = inp_dept

    def setTitle(self, inp_title):
        self.__title = inp_title
    
    def getEmpName(self):
        return self.__empName
        
    def getIdNumber(self):
        return self.__idNumber
        
    def getDepartment(self):
        return self.__department

    def getTitle(self):
        return self.__title

    def __str__(self):
        returnVariable = f"\n\tName       : {self.__empName}\n"
        returnVariable += f"\tID         : {self.__idNumber}\n"
        returnVariable += f"\tDepartment : {self.__department}\n"
        returnVariable += f"\tTitle      : {self.__title}\n"
        return returnVariable

##Employee 1:
##	Name       : Susan Meyers
##	ID         : 47899
##	Department : Accounting
##	Title      : Vice President
##
##
##Employee 2:
##	Name       : Mark Jones
##	ID         : 39119
##	Department : IT
##	Title      : Programmer
##
##
##Employee 3:
##	Name       : Joy Rogers
##	ID         : 81774
##	Department : Manufacturing
##	Title      : Engineer






