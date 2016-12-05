'''
Lucas O'Rourke
Checks validity of a user inputted password
'''

password = input("Enter a password: ")
count_upper = 0
for upper in range(len(password)):
    if (ord(password[upper]) >= 65 and ord(password[upper]) <= 90):
        count_upper += 1
count_lower = 0
for lower in range(len(password)):
    if (ord(password[lower]) >= 97 and ord(password[lower]) <= 122):
        count_lower += 1
numbers = "1234567890"
count_num = 0
for num in password:
    if num in numbers:
        count_num += 1
special = "!@#$"
count_spec = 0
for spec in password:
    if spec in special:
        count_spec += 1
if len(password) >= 8 and count_upper >= 2 and count_lower >= 1 and\
count_num >= 2 and count_spec >= 1:
    print(password, "is a valid password")
else:
    print(password, "is not a valid password")


  
