#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:26:48 2023

@author: Justus v. Samson-Himmelstjerna, Niklas Pawelzik, Benedikt Korbach, Alvaro Guijarro May
"""


from ArrayDeque import ArrayDequeMaxlen, Empty


def main():
    # initialize the deque with a maximum size of 10
    AQM = ArrayDequeMaxlen(10)

    # Print the current deque contents and menu options for the user
    while True:
        print(f"\nDeque contents: {AQM._data}")
        print("Please select an option:")
        print("1 - Add element to the front")
        print("2 - Add element to the back")
        print("3 - Remove element from the front")
        print("4 - Remove element from the back")
        print("5 - Remove first occurrence of an element")
        print("6 - Get the first element")
        print("7 - Get the last element")
        print("8 - Check if deque is empty")
        print("9 - Return the number of elements in deque")
        print("0 - Exit program")

        # Get user input for their menu choice
        choice = int(input("Your choice: "))

        if choice == 0:
            print("Exiting program...")
            break

        elif choice == 1:
            # Get user input for the element to add to the front of the deque
            element = input("Enter the element to add to the front: ")
            # Add the element to the front of the deque
            AQM.add_first(element)
            # print a confirmation message
            print(f"Added element {element} to the front")

        elif choice == 2:
            # Get user input for the element to add to the back of the deque
            element = input("Enter the element to add to the back: ")
            # Add the element to the back of the deque
            AQM.add_last(element)
            # print a confirmation message
            print(f"Added element {element} to the back")

        elif choice == 3:
            # Remove the first element from the deque
            element = AQM.delete_first()
            # print a confirmation message
            print(f"Removed element {element} from the front")

        elif choice == 4:
            # Remove the last element from the deque
            element = AQM.delete_last()
            # print a confirmation message
            print(f"Removed element {element} from the back")

        elif choice == 5:
            # Get user input for the element to remove from the deque
            element = input("Enter the element to remove: ")
            # Remove the first occurrence of the element from the deque
            try:
                removed_element = AQM.delete_first_match(element)
                # print a confirmation message
                print(f"Removed first occurrence of element {removed_element}")
            except ValueError as e:
                # If the element is not found, print an error message
                print(e)

        elif choice == 6:
            # Retrive the first element and print a message accordingly
            try:
                element = AQM.first()
                print(f"The first element is {element}")
            except Empty as e:
                print(e)

        elif choice == 7:
            # Retrive the last element and print a message accordingly
            try:
                element = AQM.last()
                print(f"The last element is {element}")
            except Empty as e:
                print(e)

        elif choice == 8:
            # Check if the deque is empty and print a message accordingly
            if AQM.is_empty():
                print("Deque is empty")
            else:
                print("Deque is not empty")

        elif choice == 9:
            # Return the number of elements in deque
            length = AQM.__len__()
            print(f"The deque consists of {length} elements")

        else:
            print("Invalid choice, please try again")


if __name__ == '__main__':
    main()
