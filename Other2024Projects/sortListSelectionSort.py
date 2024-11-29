"""A program that simulates the selection sort algorithm to sort a list of numbers in ascending or descending order. 
It uses a menu to allow the user to choose what they want to do (sort ascending, sort descending, or exit).
The program will prompt the user to enter a list if they haven't already, and then sort the list in the chosen order.
The program will continue to prompt the user until they choose to exit."""

#function used to compare current value with the rest of the list in ascending order
def comparatorAscending(value: int, data: list[int]) -> list[int]:
    valueIndex = data.index(value) #get the index of the current value
    for i in range(valueIndex + 1, len(data)): #loop through the list starting from the index of the current value
        if data[i] < value: #if the value at the current index is less than the current value
            data[valueIndex], data[i] = data[i], data[valueIndex] #swap the values
    return data #return the sorted list after this iteration

def comparatorDescending(value: int, data: list[int]) -> list[int]:
    valueIndex = data.index(value) #get the index of the current value
    for i in range(valueIndex + 1, len(data)): #loop through the list starting from the index of the current value
        if data[i] > value: #if the value at the current index is greater than the current value
            data[valueIndex], data[i] = data[i], data[valueIndex] #swap the values
    return data #return the sorted list after this iteration

def isSorted(data: list[int], order: str) -> bool:
    if order == "ascending": #check if the list is required to be sorted in ascending order
        for i in range(len(data) - 1): #loop through the list
            if data[i] > data[i + 1]: #if the current value is greater than the next value
                return False #return False
    elif order == "descending": #check if the list is required to be sorted in descending order
        for i in range(len(data) - 1): #loop through the list
            if data[i] < data[i + 1]: #if the current value is less than the next value
                return False #return False
    return True #return True if the list is sorted

def sortListSelectionSort(data: list[int], order: str) -> list[int]:
    if order == "ascending": #check if the list is required to be sorted in ascending order
        i = 0 #initialize the index to 0
        while not isSorted(data, order): #loop until the list is sorted
            if i == len(data): #if the index is equal to the length of the list
                i = 0 #reset the index to 0
            data = comparatorAscending(data[i], data) #sort the list using the comparator function
            i += 1 #increment the index
    elif order == "descending": #check if the list is required to be sorted in descending order
        i = 0 #initialize the index to 0
        while not isSorted(data, order): #loop until the list is sorted
            if i == len(data): #if the index is equal to the length of the list
                i = 0 #reset the index to 0
            data = comparatorDescending(data[i], data) #sort the list using the comparator function
            i += 1 #increment the index
    return data #return the sorted list

def menu():
    # Display the menu first
    print("Selection Sort Simulator")
    print()
    print("1. Sort list in ascending order")
    print("2. Sort list in descending order")
    print("3. Exit")
    print()
    # Get the user's choice, using exeption handling to ensure the input is an integer
    try:
        choice = int(input("Enter your choice: "))
    except ValueError: #if the input is not an integer
        print("Choice needs to be an integer!\n") #print an error message
        choice = 0 #set the choice to 0
    data = [] #initialize the list of numbers
    while choice: #loop until the user chooses to exit
        if choice == 1: #if the user chooses to sort the list in ascending order
            if not data: #if the list is empty
                #prompt the user to enter a list of numbers
                data = list(map(int, input("Enter the list of numbers separated by space: ").split()))
            #sort the list in ascending order and print the sorted list
            print("Sorted list in ascending order:", sortListSelectionSort(data, "ascending"))
        elif choice == 2: #if the user chooses to sort the list in descending order
            if not data: #if the list is empty
                data = list(map(int, input("Enter the list of numbers separated by space: ").split()))
            #sort the list in descending order and print the sorted list
            print("Sorted list in descending order:", sortListSelectionSort(data, "descending"))
        elif choice == 3: #if the user chooses to exit
            print("Exiting...") #print a message indicating that the program is exiting
            exit() #exit the program
        else: #if the user enters an invalid choice
            print("Invalid choice! Please try again.") #print an error message
        # Display the menu again
        print()
        print("1. Sort list in ascending order")
        print("2. Sort list in descending order")
        print("3. Exit")
        print()
        # Get the user's choice again
        try:
            choice = int(input("Enter your choice: "))
        except ValueError: #if the input is not an integer
            print("Invalid choice! Please try again.") #print an error message

if __name__ == "__main__": #if the program is run as the main program
    menu() #call the menu function to start the program

# This program uses the Procedural paradigm - more information on this paradigm can be found at https://en.wikipedia.org/wiki/Procedural_programming
# The program uses functions to perform specific tasks, such as sorting the list, displaying the menu, and checking if the list is sorted.
# For more information on the Selection Sort algorithm, visit https://en.wikipedia.org/wiki/Selection_sort
# For more information about Programming Paradigms, visit https://en.wikipedia.org/wiki/Programming_paradigm
# For more information about Python Functions, visit https://www.w3schools.com/python/python_functions.asp