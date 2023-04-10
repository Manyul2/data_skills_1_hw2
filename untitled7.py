#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:44:24 2023

@author: laura
"""

# PPHA 30535
# Spring 2023
# Homework 2

# YOUR CANVAS NAME HERE manyul2
# YOUR GITHUB USER NAME HERE manyul2

# Due date: Sunday April 9th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]
def evaluate(lis):
    return ['big' if sum(i) > 10 else 'just right' if sum(i) == 10 else 'small' for i in lis]
print(evaluate(start_list))    

#source: 
#https://realpython.com/python-eval-function/#:~:text=Python's%20eval()%20allows%20you,or%20a%20compiled%20code%20object.


# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 30
    return a + b
x = my_func()

# modified
def my_func(a = 10):
    b = 30
    return a + b
x = my_func()
print(x)
# the modified function is preferable because it avoids using global variables 
#that could lead to unexpected result like when a is redefined elsewhere, and 
#it's also eaiser to read and debug.


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random
from numpy import random
import string 

def password_generator(length, special_chars = True):
    if length < 8 or length > 16:
        print('Invalid password length.\nLength should be between 8 and 16.')
        return
    candidates = list(string.ascii_letters)  
    candidates += list(range(10))
    if special_chars:
        candidates += ['!', '@', '$', '%', '^', '&','*']
    return ''.join(random.choice(candidates) for i in range(length))
password_generator(16)
password_generator(25)
#string.ascii_letters generates all lower+upper case letters.
#string.ascii_letters source: https://docs.python.org/3/library/string.html
#random choice https://www.w3schools.com/python/ref_random_choice.asp

# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 3, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes a container holding any number of these 
# instances and returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class covid():
    def __init__(self, name, vaccine, doses, had_covid):
        self.name = name
        self.vaccine = vaccine
        self.doses = doses
        self.had_covid = had_covid
    def get_record(self):
        dose_quant = 'dose' if self.doses == 1 else 'doses'
        if_covid = 'had covid' if self.had_covid else "didn't have covid"
        which_vaccine = self.vaccine if self.vaccine != 'none' else 'vaccine'
        print(f"{self.name} received {self.doses} {dose_quant} of {which_vaccine} and {if_covid}.")
    def same_shot(self, other):
        if self.vaccine == other.vaccine:
            print(f'{self.name} and {other.name} received the same vaccine.')
        else:
            print(f'{self.name} and {other.name} received different vaccine.')
def all_data(containter):
    return [[i.name, i.vaccine, i.doses, i.had_covid] for i in containter]
aaron = covid("Aaron", "Moderna", 3, False)
ashu = covid("Ashu", "Pfizer", 2, False)
alison = covid("Alison", "none", 0, True)
asma = covid("Asma", "Pfizer", 1, True)

aaron.get_record()
ashu.get_record()
alison.get_record()
asma.get_record()
asma.same_shot(ashu)
all_data([aaron])
all_data([aaron, ashu])




