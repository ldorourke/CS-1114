'''
Lucas O'Rourke
Calculate whether or not three sides form an equilateral triangle
'''

import math
import turtle
print("Please enter length's of a triangle's sides")
first = int(input("Length of first side: "))
second = int(input("Length of second side: "))
third = int(input("Length of third side: "))
first_2 = first**2
second_2 = second**2
third_2 = third**2
if first == second and first == third:
    print(str(first)+',', str(second)+',', str(third)+',', "form an equilateral triangle")

elif (first == second or first == third or second == third):
    if (first > second and first > third):
        if (second_2 + third_2 == first_2):
           print(str(first)+',', str(second)+',', str(third)+',', "form an\
 isosceles right triangle")
    else:
        print(str(first)+',', str(second)+',', str(third)+',', "form an isosceles triangle")

   
elif first != second or first != third or second!= third:
    print(str(first)+',', str(second)+',', str(third)+',', "form a scalene triangle")


# Problem 5

a = first
b = second
c = third
angle_B = math.degrees(math.acos(((a**2) + (c**2) - (b**2))/(2*a*c)))
angle_A = math.degrees(math.acos(((b**2)+(c**2)-(a**2))/(2*c*b)))
angle_C = 180 - angle_B - angle_A

abc = turtle.Turtle()
abc.right(180-angle_B)
abc.forward(a)
abc.right(180-angle_C)
abc.forward(b)
abc.right(180-angle_A)
abc.forward(c)
