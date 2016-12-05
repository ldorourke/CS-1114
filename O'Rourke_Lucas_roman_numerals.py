'''
Lucas O'Rourke
Converts integer to roman numerals
'''

# This program converts any integer to roman numerals
integer = int(input("Please enter a positive integer: "))
string = ""
if integer >= 1000:
    string += (integer // 1000) * "M"
    integer = integer % 1000
if integer >= 500:
    string += (integer // 500) * "D"
    integer = integer % 500
if integer >= 100:
    string += (integer // 100) * "C"
    integer = integer % 100
if integer >= 50:
    string += (integer // 50) * "L"
    integer = integer % 50
if integer >= 10:
    string += (integer // 10) * "X"
    integer = integer % 10
if integer >= 5:
    string += (integer // 5) * "V"
    integer = integer % 5
if integer >= 1:
    string += (integer // 1) * "I"
print("The roman numeral of", integer, "is", string)
