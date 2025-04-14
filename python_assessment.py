

import random
import time

game_over = False


print("Welcome to the Guess the Number game!")
user_input = input("What's your name, gamer? ").capitalize()
time.sleep(1)
inp_tries= int(input(" How many tries would you like"))
tries = inp_tries 
print("Hi, {}, would you like to play my guessing game? 🙂".format(user_input))
question = input("Yes or No: ").lower()


if question == "yes":
    time.sleep(1)
elif question == "no":
    print("Next time maybe!")
    exit()
else:
    print("Oh well... Till we meet again, {}".format(user_input))
    exit()

time.sleep(1)
print("About to start the game. Are you ready, {}?".format(user_input))
time.sleep(2)
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")


game_number = random.randint(1, 100)

# Start guessing loop
while not game_over:
    try:
        input_2 = int(input("Come on, guess ☺️: "))
    except ValueError:
        print("Oops! Please enter a valid number.")
        continue  # Ask again without reducing tries

    if input_2 == game_number:
        print("Great Game, {}! 🎉".format(user_input))
        points += 1
        print("You get an extra point! Total points: {}".format(points))
        game_over = True
    elif input_2 > game_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

    tries -= 1

    if tries == 0 and not game_over:
        print("Your attempts are over. Game Over 😞")
        print("The number was:", game_number)
        game_over = True
    elif not game_over:
        print("Tries left: {}".format(tries))



