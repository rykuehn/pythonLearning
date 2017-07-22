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

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.