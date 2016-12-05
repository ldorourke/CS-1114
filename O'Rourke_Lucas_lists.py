'''
Lucas O'Rourke
lor215
hw9.py


There are four different questions for this problem. Each one is explained
individually above it. Question 3 is very ambiguous. Without clarification
from the PTC, I would not have understood "changes the order (in place)".

'''


# q1 finds the absolute value of each number in the list and then returns the
# maximum value of that list

def main_q1():
    max_val = max_abs_val([-19, -3, 20, -1, 0, -25])
    print("The maximum value is:", max_val)

def max_abs_val(lst):
    for index in range(len(lst)):
        lst[index] = abs(lst[index])
        maximum_val = max(lst)
    return maximum_val

main_q1()



# q2 finds all the indices of a given value in a given list

def main_q2():
    index_of_val = find_all(["a", "b", 10, "bb", "a"], "a")
    print(index_of_val)

def find_all(lst, val):
    lst_index = []
    for index in range(len(lst)):
        if lst[index] == val:
            lst_index.append(index)
    return lst_index

main_q2()



# q3 reverses a list in 2 different ways. The first way creates a new list
# in reverse order. The second way reverses the list in place.

def main_q3():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse1(lst1)
    print("After reverse1, lst1 is", lst1, "and the returned list\
 is", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    rev_lst2 = reverse2(lst2)
    print("After reverse2, lst2 is", rev_lst2)

def reverse1(lst):
    new_lst = lst[::-1] # Creates a new list slicing the original backwards
    return new_lst
  
def reverse2(lst):
    x = 1
    for ind in range(len(lst)//2): # Only iterate over half the length
        temp = lst[ind]  # Set temporary value to the value at the index

        # swaps the index value to corresponding index value on other side
        # of the list
        lst[ind] = lst[len(lst) - x] 
        lst[len(lst) - x] = temp # resets the temporary variable
        x += 1
    return lst

main_q3()



# q4 implements two run length string encoders. The first takes a string
# and prints out a list of each character and how many of that character
# there is. The second takes a list of characters and how many of each
# there are and then creates a string with that ecndoded list

def main_q4():
    res_a = encode_of_string("aadccccaa")
    res_b = decode_of_list([["a", 2], ["d", 1], ["c", 4], ["a", 2]])
    print("The encoded list for part a is", res_a)
    print("The decoded string for part b is", res_b)
    

# part a
def encode_of_string(string):
    char_lst = []
    char_count = 1
    for ind in range(len(string)): 
        if ind + 1 < len(string):
            if string[ind] == string[ind+1]:
                char_count += 1
            else:
                char_lst.append([string[ind], char_count])
                char_count = 1
        else:
            char_lst.append([string[ind], char_count]) 
    return char_lst
                
        
# part b
def decode_of_list(lst):
    res_string = ""
    for sub_lst in lst:
        res_string += sub_lst[0]*sub_lst[1]
    return res_string

main_q4()

