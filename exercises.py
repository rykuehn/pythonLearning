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

def divisors(num):
  divisor_list = []
  for i in range(1, num + 1):
    if num % i == 0:
      divisor_list.append(i)
  return divisor_list

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

#7 Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

sample = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def only_evens(listItem):
  print([num for num in listItem if num % 2 == 0])

#8 Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

def rock_paper_scissors():
  points = {'rock': 2, 'scissors': 1, 'paper': 0}

  player1 = input("Player 1 pick: Rock, paper, or scissors ").lower()
  player2 = input("Player 2 pick: Rock, paper, or scissors ").lower()

  score1 = points[player1]
  score2 = points[player2]

  if player1 == 'paper' and player2 == 'rock':
    print('player 1: {}, player 2: {}, player 1 wins!'.format(player1, player2))
  elif player1 == 'rock' and player2 == 'paper':
    print('player 1: {}, player 2: {}, player 2 wins!'.format(player1, player2))
  elif score1 > score2:
    print('player 1: {}, player 2: {}, player 1 wins!'.format(player1, player2))
  elif score2 > score1:
    print('player 1: {}, player 2: {}, player 2 wins!'.format(player1, player2))
  else:
    print("Tie")
  
  playAgain = input('Would you like to play again?').lower()
  
  if playAgain == 'yes':
    rock_paper_scissors();


#9 Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

def high_low():
  number = random.randint(1, 10)
  try:
    guess =  int(input("Pick a number between 1 - 10 : "))
  except ValueError:
    print("{} is not a number!".format(guess))
  if guess > number:
    print("Your guess is too high")
  elif guess < number:
    print("Your guess is too low")
  else:
    print("{} is exactly the same as {}".format(number, guess))

#10 write a program that returns a list that contains only the elements that are common between the lists (without duplicates) using comprehensions.

a = random.sample(range(25), 5)
b = random.sample(range(25), 5)

def common_in_lists(a, b):
  print([num for num in a for num2 in b if num == num2])

#11 Ask the user for a number and determine whether the number is prime or not

def is_prime():
  try:
    num = int(input("Give me a number"))
  except ValueError:
    print("not a number")
  div = divisors(num)
  if len(div) <= 2:
    print("prime")
  else:
    print("not prime")

#12 Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

def first_last(listItem):
  print([listItem[0], listItem[len(listItem) - 1]]);

#13 Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

def fib_return(num):
  i = 1;
  if num == 0:
    fib = []
  elif num == 1:
    fib = [1]
  elif num == 2:
    fib = [1, 1]
  else:
    fib = [1, 1]
    while i < num - 1:
      fib.append(fib[i] + fib[i - 1])
      i += 1
  print(fib)























