#Program to randomly picks an integer from 1 to 100
import random
random.random()
u_guessTaken = 10
print("You ready to guess?")
user_name = input("Enter your name: \n")
guess_number = random.randint(1, 100)
print("Lets give it a try:  \n" + str(user_name))
#To have a loop to continue the guess taken until it reach the number of tries


while u_guessTaken < 15:
    print("Ready to guess? Think of a number between 1 and 100")
    guess = input()
    guess = int(guess)
    u_guessTaken += 1

while u_guessTaken > 10:
    print("Ready to guess? Think of a number between 1 and 100")
    guess = input()
    guess = int(guess)
    u_guessTaken -= 2


    if guess < guess_number:
        print("Your guess is too low")

    if guess > guess_number:
        print("Your guess is too high")

    if guess == guess_number:
        break

    if guess == guess_number:
        u_guessTaken = str(u_guessTaken)
        print("Well done! \n" + user_name ) + ("You guessed the number in" + u_guessTaken + "guesses")

    if guess != guess_number:
        guess_number = str(guess_number)
        print("UHH...the number i was thinking of was \n" + guess_number)






