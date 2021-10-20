# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:13:30 2021

@author: JohnZhong
"""

#fix bugs when user input number out of range and invalid input
import random
number_guess = random.randint(1, 100)
j = 1
while True:
    try:
            user_guess = int(input("Please guess a number between 1-100: "))
            if user_guess in range(1, 101):
                break
            else:
                print("The number is out of range, please give another try!")
    except(ValueError, SyntaxError):
            print("Invalid data, please enter a number!")
while user_guess != number_guess:
    if user_guess > number_guess:
        print("Wrong guess! The number is too large!")
        user_guess = int(input("Please try another number: "))
    elif user_guess < number_guess:
        print("Wrong guess! The number is too small!")
        user_guess = int(input("Please try another number: "))
    j += 1
else:
    print("Bingo! Congretulations! You are right!!")
print("The correct number is", number_guess)
print("Your guess count is", j)