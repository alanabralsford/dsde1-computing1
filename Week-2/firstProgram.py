message = 'if this has printed, code has been executed successfully'
print(message)
print("what is your message?")
r = input('-->')
print(r)
print("guess a number between 1 and 10")
guess = input('-->')
guess = int(guess)
import random
roll = random.randint(1,10)
print(roll == guess)
print(roll)