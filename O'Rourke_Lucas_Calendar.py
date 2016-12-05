'''
Lucas O'Rourke
lor215
hw8q1.py

The user inputs a year and the day that January 1st falls on in that year.
The code checks if it is a leap year and then creates a yearly calendar
based on the user inputs through the use of tabs, new lines, and for loops.

'''

def main():
   user_year = int(input("Please enter a year: "))
   jan1_day = int(input("Please enter the day number for January 1st of this\
year (e.g. Mon = 1): "))
   calendar_year(user_year, jan1_day)

def calendar_month(days_in_month, start_day):
    print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")
    print(" \t"*(start_day -1), end="")
    for num in range(1, days_in_month + 1):
        print(num, end="")
        if (((start_day)+num)%7) == 1:
            print("\n", end="")
        else:
            print("\t", end="")
    next_start_day = (days_in_month + start_day)%7
    if next_start_day == 0:
        next_start_day = 7
    return next_start_day

def check_leap_year(year):
    is_leap_year = False;
    if (year%4 == 0):
        is_leap_year = True
        if (year%100 == 0):
            is_leap_year = False
            if (year%400 == 0):
               is_leap_year = True
    return is_leap_year
    
def calendar_year(year, start_day):
    months = ["January", "February", "March", "April", "May", "June",\
              "July", "August", "September", "October", "November", "December"]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap_year(year) == True:
        days_in_month[1] = 29
    for i in range(0,12):
        print(2*"\n", 2*"\t", months[i], year)
        start_day = calendar_month(days_in_month[i], start_day)
        
main()
