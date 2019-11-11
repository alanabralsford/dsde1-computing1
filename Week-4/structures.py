'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''
#NOTES
# ".join(filter(str.isalnum 
#removes all special characters, punctuation and spaces from string

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list".

the_list = [0,1,2,3,4]
def first_and_last(the_list):
    return the_list[0], the_list[-1]
# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    if end > beginning:
        print('ValueError1')
        raise ValueError
    elif end > len(the_list):
        print('ValueError2')
        raise ValueError
    elif end < 0:
        print('ValueError3')
        raise ValueError
    elif beginning < 0:
        print('ValueError4')
        raise ValueError
    elif beginning > len(the_list):
        print('ValueError5')
        raise ValueError
    else:
        new_list = the_list[end:beginning]
        return(new_list[::-1])
        #return(the_list[-end:-beginning])

    
#print part_reverse()

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    second_list = (the_list[0:index] + ([the_list[index]]*index) + the_list[index+1:len(the_list)])
    return second_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    rev = word[::-1]
    if (rev == word):
        print(rev)
        return True
    return False

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence_1 = sentence.lower()
    sentence_2 = ''.join(filter(str.isalnum,sentence_1))
    sentence_1st = list(sentence_2)
    sentence_2nd = list(sentence_2)
    sentence_2nd.reverse()
    if sentence_1st == sentence_2nd:
        result = (True)
        return result
    else:
        result = (False)
        return result
    return

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2):
    sentenceone = list(sentenece1)
    sentencetwo = list(sentence2)

    while sentenceone[0] == ' ':
        del sentenceone[0]
    while sentenceone[-1] == ' ':
        del sentenceone[-1]

    condition_1_one = sentenceone[0].isupper()                  #Checks ONE starts with uppercase
    if sentenceone[-1] == '.':
        condition_2_one = True
    elif sentenceone[-1] == '!':
        condition_2_one = True
    elif sentenceone[-1] == '?':
        condition_2_one = True
    else:
        condition_2_two = False


    while sentencetwo[0] == ' ':
        del sentencetwo[0]
    while sentencetwo[-1] == ' ':
        del sentencetwo[-1]

    condition_1_two = sentencetwo[0].isupper()                  #Checks two starts with uppercase
    if sentencetwo[-1] == '.':
        condition_2_two = True
    elif sentencetwo[-1] == '!':
        condition_2_two = True
    elif sentencetwo[-1] == '?':
        condition_2_two = True
    else:
        condition_2_two = False
    
    if condition_1_one and condition_2_one == True:             #Checks ONE respects all conditions
        one = 'yes'
    else:
        raise ValueError
    if condition_1_two and condition_2_two == True:             #Checks TWO respects all conditions
        two = 'yes'
    else:
        raise ValueError

    finalone = ''.join(map(str, sentenceone))
    finaltwo = ''.join(map(str, sentencetwo))

    return print(finalone+' '+finaltwo)



# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    for key, value in dictionary.items():
        if key == key:
            return True
        else:
            return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    return ("value" in dictionary.values())

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    z = dictionary1.copy()   # start with x's keys and values
    z.update(dictionary2)    # modifies z with y's keys and values & returns None
    return z

print(first_and_last(the_list))
print(palindrome_word("santa"))
print(palindrome_word("level"))
print(part_reverse(the_list, 3, 1))
print(repeat_at_index([0, 1, 2, 3, 4], 3))
print(repeat_at_index(the_list, 3))
print(palindrome_sentence("Eva, can I see bees in a cave?"))
print(palindrome_sentence("Eva, can I see bees in a cavee?"))
print(concatenate_sentences("Hello there.", "My name is alana!"))