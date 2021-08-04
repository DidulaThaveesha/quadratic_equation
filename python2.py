import math  
#create variables
a = 0
b = 0
c = 0
discriminant_part = 0
root_1 = 0
root_2 = 0

#process
print("A quadratic equation :=ax**2+bx+c")#quadratic equation
a=float(input("Enter the coefficient of x**2:"))
b=float(input("Enter the coefficient of x:"))
c=float(input("Enter the constant value:"))

discriminant_part=(b**2-4*a*c)

if discriminant_part == 0:
    root_2 = (((-b) + math.sqrt(discriminant_part)) / (2*a))
    root_1 = (((-b) - math.sqrt(discriminant_part)) /(2*a))
    print("The discriminant is greater than zero -> There are two real distinct roots")
    print("The roots of x**2-",b,"x+",c,"=0","is","%0.2f"%root_1,"and","%0.2f"%root_2)

elif discriminant_part > 0:
    root_2 = (((-b) + math.sqrt(discriminant_part)) / (2*a))
    root_1 = (((-b) - math.sqrt(discriminant_part)) /(2*a))
    print("The discriminant is zero -> There are two real identical roots")
    print("The roots of x**2-",b,"x+",c,"=0","are","%0.2f"%root_1,"and","%0.2f"%root_2)

else:
    print("The discriminant is less than zero -> There are no real roots")


