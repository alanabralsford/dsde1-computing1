message = 'if this has printed, code has been executed successfully'
print(message)
x = 0
print("what is your message?")
r = input('-->')
print(r)
print("guess a number between 1 and 10")
guess = input('-->')
guess = int(guess)
import random
roll = random.randint(1,10)
if (roll == guess):
    print(roll == guess)
else:
    while (x < 2):
        print(roll)
        """
        in a real situation, take this line out as it tells
        you the generated number, I kept this to test the game
        """
        print("guess a number between 1 and 10")
        guess = input('-->')
        guess = int(guess)
        if (roll == guess):
            print(roll == guess)
            break
        print(roll == guess)
        x = x + 1