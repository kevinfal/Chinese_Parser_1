
from dictionary import dictionary

"""

"""
class parser:
    def __init__(self,source):
        self.dictionary = dictionary(source)

    """
        separates all of the words in a sentence or given input
    """
    def separate_words(self, input):
        returned = []
        i = 0
        while i < len(input):
            print("loop call")
            print(input[i:len(input)])

            if(input[i] == ' '):
                i+= 1
                continue

            i2 = self.complete_word( input, i) # set i2 to index of where word ends
            print(i2)
            if(i2 == None):
                print("NONE")
                returned.append("/?" + input[i] + "?/")  # character not found in dictionary
                i2 = i
                continue
            returned.append(input[i:i2])       # word is input[i:i2], add to list

            # this happens when word is one character
            if(i == i2):
                print("ERROR, THIS IS WHY")
                i2 += 1
            i = i2                         # i = i2 + 1 to not pass through covered characters
        return returned

    """
        Arguments:
            index: index of where word starts

        Returns:
            (int) index of where the word ends, 
            None if character at index is not a word
    """
    def complete_word(self, input, index):
        word = input[index]
        print("called complete_word: " + input[index])
        if(not self.dictionary.word_lookup(word)):
            if(self.dictionary.word_lookup(word + input[index + 1])):
                word = word + input[index+1]
                index+=1
            else:
                return None
        i = index
        # if last character in input string
        if(i == len(input) - 1):
            return len(input)
        while i < len(input) -1 and self.dictionary.word_lookup(word):
            print("word: " +word)
            i+=1
            word += input[i]
            print("appended word: " + word)
            print(self.dictionary.word_lookup(word))
        print("word to add: " + word)
        # exit conition was i < len(input) 
        if(i == len(input) - 1):
            # if was a word
            if(self.dictionary.word_lookup(word)):
                return len(input)
            else:
                # word was not a valid word
                return len(input) - 1
        return index + len(word) - 1
    
        

if (__name__ == "__main__"):
    d = dictionary("simplified_2014.txt")
    string = "北京在中国北方广州在中国南方"
    print(d.word_lookup(string))
    parser = parser("simplified_2014.txt")
    print(  parser.separate_words(string))
    print("北京　在　中国　北方；　广州　在　中国　南方")


