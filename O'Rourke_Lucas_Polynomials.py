'''
Lucas O'Rourke
Takes a second degree polynomial and prints out its roots
'''

import math
a = int(input("Please enter value of a: "))
b = int(input("Please enter value of b: "))
c = int(input("Please enter value of c: "))
if a is 0 and b is 0 and c is 0:
    print("The equation has infinite infinite number of solutions")
elif a is 0 and b is 0:
    print("The equation has no real solution")
elif a is 0 and c is 0:
    print("The equation has infinite number of solutions")
elif b is 0 and c is 0:
    print("The equation has infinite number of solutions")
elif a is 0:
    x = (-c/b)
    print("The equation has single real solution, x =", x)
elif b is 0:
    if c < 0 and a > 0:
        x = (abs(c)/abs(a))**0.5
        print("The equation has two real solutions, x =", x, "and", -x)
    elif c < 0 and a < 0:
        print("The equation has no real solution")
    elif c > 0 and a > 0:
        print("The equation has no real solution")
    elif c > 0 and a < 0:
        x = (abs(c)/abs(a))**0.5
        print("The equation has two real solutions, x =", x, "and", -x)
elif c is 0:
    x = -b/a
    print("The equation has two real solutions  x = 0 and x =", x)
elif a is not 0 and b is not 0 and c is not 0:
    if ((b**2) - (4*a*c)) is 0:
        x = -b/(2*a)
        print("The equation has single real solution, x =", x)
    elif ((b**2)-(4*a*c)) < 0:
        print("The equation has no real solution")
    elif ((b**2)-(4*a*c)) > 0:
        x1 = ((-1*b)+((b**2)-(4*a*c))**0.5)/(2*a)
        x2 = ((-1*b)-((b**2)-(4*a*c))**0.5)/(2*a)
        print("The equation has two real solutions, x =", round(x1, 2)\
              , "and", round(x2,2))
