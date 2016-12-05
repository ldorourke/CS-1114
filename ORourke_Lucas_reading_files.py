'''

Lucas O'Rourke
CS 1114
lor215

This file removes the unwanted data from a CSV file and creates a new, cleaned up file.
It then creates a new CSV file for temperatures and precipitation in metric units. Then it
calculates the average high and low temperature for each month in each city in either imperial
or metric. Part D is a made up problem in which it finds the highest and lowest value of a list
created in Part C for each month and prints out the highest average.

'''

# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    in_file = open(complete_weather_filename, "r")
    out_file = open(cleaned_weather_filename, "w")
    for line in in_file: 
        if line != "\n":
            stripped = line.strip() # Takes out new lines and white spaces
            split_line = stripped.split(",") # splits each line into a list at commas

            # Iterates through split line in order to find each desired value
            city = split_line[0]
            date = split_line[1]
            high = split_line[2]
            low = split_line[3]
            precipitation = split_line[8]
            if precipitation == "T": # "T" is the only non-numeric value
                precipitation = "0" # Changes the value to 0 if precipitaion = "T"

            # Writes all of the values into new CSV file    
            out_file.write(city+","+date+","+high+","+low+","+precipitation+"\n")
    in_file.close()
    out_file.close()

# Part B
def f_to_c(f_temperature): 
    temp_celc = (float(f_temperature) - 32)*(5/9) # Unrounded to ensure accuracy
    return temp_celc

def in_to_cm(inches):
    cm_length = float(inches)*2.54 # Unrounded to ensure accuracy
    return cm_length

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    in_file = open(imperial_weather_filename, "r")
    out_file = open(metric_weather_filename, "w")
    first_line = in_file.readline() # Takes the first line out of the foor loop
    out_file.write(first_line+"\n")
    for line in in_file:
         if line != "\n":
            stripped = line.strip()
            split_line = stripped.split(",")
            city = split_line[0]
            date = split_line[1]
            high = split_line[2]
            low = split_line[3]
            precipitation = split_line[4]
            metric_high = f_to_c(high) # Converts each high to metric
            metric_low = f_to_c(low) # Converts each low to metric
            metric_precip = in_to_cm(precipitation) # Converts each precipitation to metric

            # Writes all of the values into the new CSV file
            out_file.write(city+","+date+","+str(metric_high)+","+str(metric_low)+\
                           ","+str(metric_precip)+"\n")
    in_file.close()
    out_file.close()
     
# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    # Prints average highs and lows in each month for the given city
    in_file = open(weather_filename, "r")
    first_line = in_file.readline()
    entire_list = []
    for i in range(12):
        entire_list.append([0, 0, 0]) # Creates a list of length 12 and has three values at each
        # point in the list: high, low, and count for number of days in the month
        
    for line in in_file:
        stripped = line.strip()
        split_line = stripped.split(",")
        if split_line[0] == city:
            date = split_line[1].split("/")
            month = int(date[0])
            index = month - 1
            month_list = entire_list[index]
            month_list[0] += float(split_line[2])
            month_list[1] += float(split_line[3])
            month_list[2] += 1
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August",\
                   "September", "October", "November", "December"]
    print("")
    print("Average temperatures for "+city+":")
    month_count = 0
    list_high = []
    list_low = []
    for elem in entire_list: # Finds average of high and low for each month
        high = elem[0]
        low = elem[1]
        count = elem[2]
        avg_high = high/count
        avg_low = low/count
        list_high.append(avg_high)
        list_low.append(avg_low)
        if unit_type == "imperial":
            print(months_list[month_count]+": "+str(round(avg_high))+"F High, "+str(round(avg_low))+"F low")
            month_count += 1
        else:
            print(months_list[month_count]+": "+str(round(avg_high))+"C High, "+str(round(avg_low))+"C low")
            month_count += 1

    in_file.close()
    return (list_high, list_low)


# Part D
def find_highest_and_lowest(city1_lst, city2_lst, city3_lst):
    high_lst1 = city1_lst[0]
    low_lst1 = city1_lst[1]
    high_lst2 = city2_lst[0]
    low_lst2 = city2_lst[1]
    high_lst3 = city3_lst[0]
    low_lst3 = city3_lst[1]
    
    max_city1 = max(high_lst1)
    max_city2 = max(high_lst2)
    max_city3 = max(high_lst3)
    min_city1 = min(low_lst1)
    min_city2 = min(low_lst2)
    min_city3 = min(low_lst3)
    
    print("The highest average temperature of any month for San Francisco is", round(max_city1),\
          "F and the lowest average temperature of any month is", round(min_city1), "F")
    print("The highest average temperature of any month for New York is", round(max_city2), "C and\
 the lowest average temperature of any month is", round(min_city2), "C")
    print("The highest average temperature of any month for San Jose is", round(max_city3), "F and\
 the lowest average temperature of any month is", round(min_city3), "F")
    
    
    
      
def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")

    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")

    print ("Running Part C")
    city1 = print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    city2 = print_averages_per_month("New York", "weather in metric.csv", "metric")
    city3 = print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("\nRunning Part D\n")
    find_highest_and_lowest(city1, city2, city3)
    

 
main()
