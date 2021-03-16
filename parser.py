
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

            if(i2 == None):
                print("NONE")
                returned.append("/?" + input[i] + "?/")  # character not found in dictionary
                i2 = i
                continue
            returned.append(input[i:i2])       # word is input[i:i2], add to list
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
        while i < len(input) -1 and self.dictionary.word_lookup(word):
            i+=1
            word += input[i]
        return index + len(word) 
    
        

if (__name__ == "__main__"):
    d = dictionary("simplified_2014.txt")
    string = "你叫"
    print(d.word_lookup(string))
    parser = parser("simplified_2014.txt")
    print(  parser.separate_words(string)
)

