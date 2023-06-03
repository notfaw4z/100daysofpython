from art import logo
from  random import randint
print(logo)

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
turns = 0


#Function to assign the number of turns to the user based on their input
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

#Check answer function
def check_answer(user_guess, number, turns):
  """checks answer against guess and returns the number of turns remaining"""
  if user_guess == number:
    print(f"You got it! The answer was {user_guess}.")
  elif user_guess > number:
    print("Too high.")
    return turns - 1 
  else:
    print("Too low.")
    return turns - 1 


def game():
  #Choosing number between 1 and 100
  print("Welcome to the Number Guessing Game!")
  number = randint(1, 100)
  print("I'm thinking of a number between 1 and 100.")
  print(f"Number is {number}")
  
  
  turns = set_difficulty()
  

  user_guess = 0
  while user_guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    #Let user guess the number
    user_guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if wrong
    turns = check_answer(user_guess,number, turns)

    if turns == 0:
      print("You've run out of guesses. You lose.")
      return
    elif user_guess != number:
      print("Guess again.")

game()
