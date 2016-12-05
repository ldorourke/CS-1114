'''
Lucas O'Rourke
BMI Calculator based on user input
'''

weight = int(input("Please enter weight in pounds: "))
height = int(input("Please enter height in inches: "))
kil_weight = weight*0.453592
met_height = height*0.0254
bmi = kil_weight/met_height**2
rounded = round(bmi, 7)
print("BMI is", rounded)
