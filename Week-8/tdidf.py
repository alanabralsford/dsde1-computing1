import string as s

class TfIdf:
    #def __init__(self):
      #  self.docs_tf = {}
    
    #docs_tf = dict()

    def __init__(self, filename, tf=dict()):
        g = self.read_file(filename)
        h = self.string_to_list(g)
        e = self.compute_tf(h)
        print(e)
        self.tf = e

        return


    def read_file(self, textFile):
        f = open(textFile + ".txt", "r")
        #print(f.read())
        contents = f.readlines()
        f.close()
        s_contents = ""
        #print(contents)
        return(s_contents.join(contents))
    
    def string_to_list(self, string):
        sentence = string.lower()
        for char in sentence:
            if char in s.punctuation.replace('/',""):
                sentence = sentence.replace(char, '')
        list1 = sentence.split()
        for word in list1:
            if word == ' ':
                list1.remove(word)
            return(list1)
        
    def compute_tf(self, list_strings):
        dictionary = dict()
        for word in list_strings:
            if word not in dictionary.keys():
                dictionary[word] = 1
            else:
                dictionary[word] += 1

        '''for word, number in dictionary.items(): 
            dictionary[word] = number/10'''



        return dictionary

file = TfIdf("text-files/mercutio")
file.read_file("text-files/mercutio")
print(file.string_to_list("I love dogs and Victor hates glitter"))

