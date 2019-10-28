'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    a = a + 1
    print(a)
#print(inc(5))
inc(5)

# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    a = a + 1
    return a
print(inc_return(12))

# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    sum = a + b
    return sum
print(sum(5, 3))


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    sum2 = sum(a, b)
    sum2 = inc_return(sum2)

    return sum2

print(sum_inc(2,4))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    boolTest =  (a % 2) == 0
    return boolTest
print(is_even(5))


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    s = str()
    for i in range(repeat):
        s += phrase
    print(s)
    #for i in range(repeat)
        #string = phrase * repeat
    
    #print string
string_repeat("dog", 4)

def main()
    # input function you want to test

if __name__ = '__main__':
    main()
    #in the terminal, its studying internal variable in python, executing from command line not interactive shell


    #return (phrase * (int(length/len(phrase))+1))[:repeat]
    # hint: you can add strings together 
    # in order to concatenate them
#print(string_repeat(dog, 5))

