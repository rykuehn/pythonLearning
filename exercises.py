# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

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

