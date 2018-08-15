# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
#To avoid the: RuntimeError: maximum recursion depth exceeded
import sys
sys.setrecursionlimit(100000)

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for line in range(1, 21):
    print(line, data_list[line])

#print([data_list[i] for i in range(1, 21)])

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows
print("\nTASK 2: Printing the genders of the first 20 samples")
print([data_list[i][6] for i in range(1, 21)])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for line in range(len(data)):
        column_list.append(data[line][index])

    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(len(column_to_list(data_list, -2)))
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
for line in range(len(data_list)):
    if data_list[line][-2] == "Female":
        female += 1
    elif data_list[line][-2] == "Male":
        male += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Args
    Param1: a list/array/dataset
    Will browse the list, and count every occurs of  female gender and male gender
    """
    male = 0
    female = 0
    for line in range(len(data_list)):
        if data_list[line][-2] == "Female":
            female += 1
        elif data_list[line][-2] == "Male":
            male += 1
    return [male, female]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Args
    param1: list/array/dataset
    Will Get the result of count_gender function and will find the bigger one
    """
    answer = ""
    male = count_gender(data_list)[0]
    female = count_gender(data_list)[1]

    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Equal"             
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")
def count_user_types(data_list):
    subscriber = 0
    customer = 0
    for line in range(len(data_list)):
        if data_list[line][-2] == "Subscriber":
            subscriber += 1
        elif data_list[line][-2] == "Customer":
            customer += 1
    return [subscriber, customer]

user_list = column_to_list(data_list, -3)
user_types = ["Subscriber", "Customer"]
quantity_user_type = count_user_types(data_list)
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity by User Type')
plt.xlabel('User Type')
plt.xticks(y_pos, user_types)
plt.title('Quantity by User Type')
plt.show(block=True)


input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because has gender column's with empty value  "
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
count = 0
for duration in trip_duration_list:
    mean_trip += float(duration)
    
    if count == 0:
        count += 1
        min_trip = float(duration)
        max_trip = min_trip
        
    if min_trip > float(duration):
        min_trip = float(duration)
    if float(duration) > max_trip:
        max_trip = float(duration)

mean_trip /= len(trip_duration_list)

#https://en.wikipedia.org/wiki/Quicksort
def quickSort(A, lo, hi):
    """
    Args:
    param1: A list.
    param2: start o list the index 0.
    param3: end of list the len of index - 1
    Uses two indices that start at the ends of the array being partitioned,
    then move toward each other, until they detect an inversion.
    """
    if lo < hi:
        p = partition(A, lo, hi)
        quickSort(A, lo, p - 1)
        quickSort(A, p + 1, hi)
    return A
def partition(A, lo, hi):
    """
    Args:
    param1: A list.
    param2: start o list the index 0.
    param3: end of list the len of index - 1
    A pair of elements, one greater than or equal to the pivot, 
    one lesser or equal, that are in the wrong order relative to each other. 
    The inverted elements are then swapped. 
    When the indices meet, the algorithm stops and returns the final index.
    """
    pivot = float(A[lo])
    i = lo + 1
    j = hi

    while True:
        while i <= j and float(A[i]) <= pivot:
            i = i + 1

        while float(A[j]) >= pivot and j >= i:
            j = j -1

        if j < i:
            break
        else:
            A[i], A[j] = A[j], A[i]

    A[lo], A[j] = A[j], A[lo]
    return j

trip_duration_list = quickSort(trip_duration_list,0,len(trip_duration_list)-1)

#median https://www.youtube.com/watch?v=B1HEzNTGeZ4
mod = len(trip_duration_list) % 2 
midle = int(len(trip_duration_list)/2) 
if  mod > 0:
    median_trip = float(trip_duration_list[midle])
else:
    median_trip = float((float(trip_duration_list[midle]) + float(trip_duration_list[midle + 1])) / 2)


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, -5))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
param1: The first parameter.
param2: The second parameter.
Returns:
List of X values
"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "no"

def count_items(column_list):
    item_types = set(column_list)
    count_items = count(column_list)
    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------