'''
Lucas O'Rourke
lor215
hw10.py

There are four different problems, all using list functions. Each problem has
an explanation above, and the complicated ones have comments within the code.
Q1 was the most difficult. Not clear if we can user random function.
'''

# q1 asks a user to input an integer and creates a permutated list
# containing all numbers 1-n

import random
def main_q1():
    n = int(input("Please enter an integer to create a permutated list: "))

    # Create a list 1 to n and then call the create permutation function
    lst_1_to_n = list(range(1, n+1))
    permutated = create_permutation(lst_1_to_n)
    print("The permutated list from 1 to n is", permutated)
    

def create_permutation(lst):
    # Create list of range of indices in the length of the list
    ind_lst = list(range(len(lst)))
    
    permutated_lst = []
    for ind in range(len(lst)):

        # Create a random index from the index list
        rand_ind = random.randint(0, (len(ind_lst) -1))

        # Append the index value of the index list to the permutated list
        permutated_lst.append(lst[ind_lst[rand_ind]])

        # Remove the random integer from the index list
        ind_lst.remove(ind_lst[rand_ind])
    return permutated_lst
        
        

main_q1()

    


# q2 runs two while loops to get user input and creates a list in each one
# it then calls the add_list function if the two lists are the same length
# with those 2 lists and return a list with the sum of each corresponding
# element

def main_q2():
    seen_done1 = False
    print("Enter numbers on a seperate line and then type 'done'")
    lst1 = []
    lst2 = []
    while seen_done1 == False: # Creates user list until done is inputted
        user_inp = input()
        if user_inp == "done":
            seen_done1 = True
        else:
            lst1.append(int(user_inp))
    print("Create second list of equal length")
    seen_done2 = False
    while seen_done2 == False: # Creates second user list
        user_inp = input()
        if user_inp == "done":
            seen_done2 = True
        else:
            lst2.append(int(user_inp))
    if len(lst1) != len(lst2): # Prints if the lengths are not the same
        print("Lists are different lengths.")
    res = add_list(lst1, lst2)
    print(res)
    
def add_list(lst1, lst2):
    res_lst = []
    for index in range(len(lst1)):
        sum_of_index = lst1[index] + lst2[index] # Adds the sum of indices together
        res_lst.append(sum_of_index) # Appends sum of indices to resulting list
    return res_lst

main_q2()



# q3 takes a list and returns a sequence of lists

def main_q3():
    res = create_prefix_lists([2,4,6,8,10])
    print(res)
    
def create_prefix_lists(lst):
    entire_lst = []
    for ind in range(len(lst) +1):
        entire_lst.append(lst[0:ind]) # slicing technique appending a list to a list
    return entire_lst
        
main_q3()   



# q4 first reads a menu from the user and creates a list of the item and its
# corresponding price. It then asks three customers what they want to order
# using a while loop. Once they all entered done, it return a list of their
# orders and then calls another function to calculate the price. In the main
# it calculates the tip and tax and prints out the total price.

def main_q4():
    menu = read_menu()
    res_price = 0
    for order in range(3):

        # Calls the customer order function 3 times
        customer_order = read_customer_order()

        # Computes the price and then adds it to the resulting price
        res_price += compute_price(menu, customer_order)
    tip = res_price*0.15
    tax = res_price*0.085
    total = round((res_price + tax + tip), 2)
    print("The total with tax and tip included is:", total)
        
def read_menu():
    n = int(input("How many items are on the menu? "))
    menu_lst = []
    for x in range(n):
        item = input("Enter items in the form 'name:price': ")

        # splits the item into the name and then the item in a list
        item = item.split(":")
        menu_lst.append(item)
    return menu_lst

def read_customer_order(): # Takes individual customer orders
    seen_done = False
    print("What would you like to order? Enter items in seperate lines\
 and finish with done")
    order_lst = []
    while seen_done == False:
        order = input()
        if order == "done":
            seen_done = True
        else:
            order_lst.append(order)
    return order_lst

def compute_price(menu_lst, order_lst): 
    price_lst = []
    for item in order_lst:
        for menu_item in menu_lst:
            
            # Menu item at index 0 is the item. If the order has an item on
            # the menu, then it will append index 1 (the price) to a  new list
            if item == menu_item[0]:
                price_lst.append(float(menu_item[1]))
    total_price = sum(price_lst)
    return total_price
                
main_q4()
        
        
