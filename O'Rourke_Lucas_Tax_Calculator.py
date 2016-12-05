'''
Lucas O'Rourke
Calculates the total price with tax included
'''

first = int(input("Enter price of first item: "))
second = int(input("Enter price of second item: "))
club = input("Does customer have a club card (Y/N): ")
tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
if first > second:
    second_price = second*0.5
    together = second_price + first
    if club is "Y":
        tot_club = together - (together*.1)
        tot_tax1 = tot_club + tot_club*(tax/100)
        print("Base price =", (first+second))
        print("Price after discounts =", round(tot_club, 2))
        print("Total price =", round(tot_tax1, 2))
    elif club is "N":
        tot_tax2 = together + together*(tax/100)
        print("Base price =", (first+second))
        print("Price after discounts =", round(together, 2))
        print("Total price =", round(tot_tax2, 2))
elif second > first:
    first_price = first*0.5
    together = first_price + second
    if club is "Y":
        tot_club = together - (together*.1)
        tot_tax1 = tot_club + tot_club*(tax/100)
        print("Base price =", (first+second))
        print("Price after discounts =", round(tot_club, 2))
        print("Total price =", round(tot_tax1, 2))
    elif club is "N":
        tot_tax2 = together + together*(tax/100)
        print("Base price =", (first+second))
        print("Price after discounts =", round(together, 2))
        print("Total price =", round(tot_tax2, 2))
