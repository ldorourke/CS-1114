'''
Lucas O'Rourke
CS 1114
lor215

This program takes a user input for a train line and prints out every stop on
that train line. It first cleans all the data and removes any extraneous information
of the given file and creates a new file. Then it creates a list of every stop
and the line that it is on in the format [line, stop]. Program stops running
when the user enteres "done".

'''

def main():
    clean_data("train_stop_data.csv", "cleaned_data.csv")
    lines_list = create_line_list("cleaned_data.csv")
    seen_done = False # flag variable
    while seen_done == False:
        user_inp = input("\nPlease enter a train line or 'done' to stop: ")
        print("")
        user_inp = user_inp.upper() # makes user input upper
        if user_inp == "DONE":
            seen_done = True
        else:
            find_train_stops(user_inp, lines_list)

def clean_data(filename, out_filename): # cleans data and creates a new file
    # with only desired data
    
    in_file = open(filename, "r")
    out_file = open(out_filename, "w")
    first_line = in_file.readline()
    for line in in_file:
        stripped = line.strip() # strips the line of extra white spaces
        split_line = stripped.split(",") # splits the line into a list at the commas
        train_line = split_line[0] # the train line is at value 0
        stop_name = split_line[2] # stop name is at value 2
        out_file.write(train_line+","+stop_name+"\n")
    in_file.close()
    out_file.close()

def create_line_list(cleaned_data): # Creates a list of lists with all the stops
    # on each line
    in_file = open(cleaned_data, "r")
    entire_list = []
    for line in in_file:
        stripped = line.strip() # strips line of white spaces
        split_line = stripped.split(",") # splits into a list at comma
        train_line = split_line[0]  # the stop is at value 0
        backwards = train_line[::-1] # reverses the string of the stop because
        # only the first number matters in this program
        
        final_train_line = 0
        for char in backwards: # runs through all the characters in the backwards string
            final_train_line = char # sets the train line as the last character

        # returns list of lists with the train line, and each stop at that line    
        entire_list.append([final_train_line, split_line[1]]) 
    return entire_list          


def find_train_stops(train_line, stop_list): # prints out every stop at desired line
    all_stops = "" # creates string for all stops on the user inputted train line
    for elem in stop_list: # takes each individual list in the entire list
        line = elem[0] 
        if line == train_line: # if user input = the stop, it proceeds
            if elem[1] not in all_stops: # only adds to string if not already there
                all_stops += elem[1]+", "
    if len(all_stops) == 0: # accounts for user not putting in a valiud input
        print("There is no", train_line, "line")
    else:
        all_stops = all_stops.strip(", ") 
        print(train_line+" line: ", end ="")
        print(all_stops) # prints all of the stops at the line


main()
