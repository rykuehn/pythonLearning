import random

def game():
  secret_numb = random.randint(1, 10)
  guesses = [];

  while len(guesses) < 5:
    try:
      play_guess = int(input("What is your guess?"))
    except ValueError:
      print("{} is not a number".format(play_guess))
    else:
      if play_guess == secret_numb:
        print("You got it!")
        break
      else:
        if play_guess < secret_numb:
          print("My number is higher than {}".format(play_guess))
        elif play_guess > secret_numb:
          print("My number is lower than that".format(play_guess))
        guesses.append(play_guess)

  else:
    print("My number is {}, you didn't get it within 5 guesses").format(secret_numb)

  play_again = input("Do you want to play again? Y/n")

  if play_again.lower() != 'n':
    game();
  else:
    print("Byeeeee")

game();