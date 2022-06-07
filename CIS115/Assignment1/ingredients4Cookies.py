##Michael Mumme, CIS115, Maya Tolappa, 9/9/21
##This program will portion out the serving size for however many cookies you'd like to bake.
desiredNumberOfCookies = int(input("Enter the number of cookies: "))
print(f"{desiredNumberOfCookies * 1.75 / 48:.1f} cups of sugar \n{desiredNumberOfCookies * 1 / 48:.1f} cups of butter \n{desiredNumberOfCookies * 2.75 / 48:.1f} cups of flour")

##Enter the number of cookies: 25
##0.9 cups of sugar 
##0.5 cups of butter 
##1.4 cups of flour
##
##Enter the number of cookies: 50
##1.8 cups of sugar 
##1.0 cups of butter 
##2.9 cups of flour
