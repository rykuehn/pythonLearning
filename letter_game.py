import random
import os
import sys

words = ["apple", "orange", "grapes", "melon", "blueberry"]

def clear():
  if(os.name == 'nt'):
    os.system = 'cls'
  else:
    os.systelm = ('clear')

def draw(bad_guesses, good_guesses, secret_word):
  clear()

  print('Strikes: {}/7'.format(len(bad_guesses)))
  print('')
  
  for letter in secret_word:
      if letter in good_guesses:
        print(letter, end='')
      else:
        print('_', end='')
    print('')
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

def get_guess(bad_guesses, good_guesses):
  guess = input('Guess a letter: ').lower()

    if len(guess) != 1:
      print("You can only guess a single letter!")
      continue
    elif guess in bad_guesses or guess in good_guesses:
      print('you have already guessed that letter!')
      continue
    elif not guess.isalpha():
      print('You can only guess letters!')
      continue
    else:
      return guess

    if guess in secret_word:
      good_guesses.append(guess)
      if len(good_guesses) == len(list(secret_word)):
        print("You win! The word was {}".format(secret_word))
        break

def play(done):
  clear()
  secret_word = random.choice(words)
  bad_guesses = []
  good_guesses = []

  while True:
    draw(bad_guesses, good_guesses, secret_word)
    guess = get_guess(bad_guesses, good_guesses)

    if guess in secret_word:
      good_guesses.append(guess)
      found = True
      for letter in secret_word:
        if letter not in good_guesses:
          found = False
        if found:
          print("You win!")
        else:
          print("You lose!")
          done = True
    else:
      bad_guesses.append(guess)
      if len(bad_guesses) == 7:
        draw(bad_guesses, good_guesses, secret_word)
        print("You lost")
        done = True

    if done:
      play_again = input("Do you want to play again ? y/n").lower()
      if play_again != "n":
        return play(done = False)
      else:
        sys.exit()

def welcome():
  start = input("Press enter to start and Q to quit").lower()
  if start = 'q':
    print("Bye")
    sys.exit()
  else:
    return True

print("Welcom to the letter guess game")
done = False

while True:
  clear()
  welcome()
  play(done)

while True:
  start = input("Press enter/return to start, and Q to quit")
  if start.lower() == 'q':
    break
  secret_word = random.choice(words)
  bad_guesses = []
  good_guesses = []

  while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
    

    else:
      bad_guesses.append(guess)

  else:
    print("You didnt get it, my secret word was {}".format(secret_word))