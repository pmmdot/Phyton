import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b**2) - (4*a*c)

if d == 0:
    d1 = ((-b) + math.sqrt(d))/(2*a)
    print("The quadratic has Equal Roots")
    print(f"The root is {d1}")
elif d > 0:
    d1 = ((-b) + math.sqrt(d))/(2*a)
    d2 = ((-b) - math.sqrt(d))/(2*a)
    print("The roots are:")
    print(d1)
    print(d2)
else:
    print("No real Roots")

