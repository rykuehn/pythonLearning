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













