#1 Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
def name():
  name = input("What is your name?")
  try:
    age = int(input("What is your age?"))
    numOfPrints = int(input("How many times do you want this printed?"))
    
  except ValueError:
    print("That is not a number")
    years = 100 - age

    while numOfPrints > 0:
      print("You will die in {} years \n".format(years))
      numOfPrints = numOfPrints - 1

#2 Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

def odd_even():
  try:
    num1 = int(input("Pick a number"))
    num2 = int(input("Pick a number"))
  except ValueError:
    print("That is not a number")
    if num2 % 2 == 0 and num2 % num1 == 0:
      print("{} is an even number".format(num2))
      print("Yeah!")
    elif num2 % 2 == 0:
      print("{} is an even number".format(num2))
    elif num2 % 2 == 1:
      print("{} is an odd number".format(num2))
    elif num2 % 4 == 0:
      print("{} is a mulitple of four".format(num2))

#3 write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def lessThan5(list):
  print([num for num in list if num < 5])

#4 Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def divisors():
  try:
    num = int(input("pick a number"));
  except ValueError:
    print("please enter a number")
  for i in range(1, num + 1):
    if num % i == 0:
      print(i)

#5 and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

import random

#create random lists
a = random.sample(range(25), 10)
b = random.sample(range(25), 10)

def list_overlap(x, y):
  print(list(set([num for num in x if num in y])))


#6 Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def is_palindrome(word):
  #print(word == word[::-1]) 
  x = ''
  for i in range(len(word)):
    x+= word[len(word) - 1 - i]
  print(x == word)

#is_palindrome("racecar")
















