
"""
    Dictionary Class:
        Holds a list (word_list) of words as its word bank. Only words that the program recognizes
        are within this word list. Can perfom a word lookup to see if a word is within the given dictionary.
    Arguments: (str) source: name of file with list of words to use as dictionary
"""
class dictionary:
    """
             Upon initiation, construct word list to use as dictionary.
        Arguments:
            source: (str) name of file that contains list of words. 
    """
    def __init__(self,source):
        self.source = source
        self.word_list = self.read_word_list(source)
    """
        Reads the file that holds all of the words for the dictionary.
        File should be formatted such that every line has one word, and
        only that word until the next line.

        Arguments:
            source: (str): name of file that contains list of words (must incluse .txt at end)

        Returns:
            str[] of all lines in the source text file, with each line in the file being its own word
    """
    def read_word_list(self,source):
        returned = []
        file = open(self.source, 'r', encoding = "utf8")
        for word in file:   # every line in the file will be one word
            returned.append(word.rstrip())
        return returned

    """
        Iterates through word_list to see if a word is present in the dictionary, returns
        True if the word is found, false otherwise

        Arguments:
            string: (str) word to look up in dictionary

        Returns:
            True if the string is in word_list, False if it is not.
    """
    def word_lookup(self,string):
        for word in self.word_list:
            # if string is a word in the dictionary
            if(word == string):
                return True
        # word not found, return none
        return False


"""
    create_word_dictionary():
            Creates a text file with a list of words from the data set given from korpus. 
            Used to create simpilfied_2014.txt and macau_2015.txt. Input file should be inputted such that
            there are at least 2 columns of data, with the word being the sescond one
    Arguments:
        (str) file_title: title of text file to get from.
                Specified to parse through specific data set from korpusdownload
        (str) output: what to name output text file, must include .txt
"""
def create_word_dictionary(file_title,output):
    words = []
    file = open(file_title, encoding = "utf8")
    for line in file:
        split = line.split()
        words.append(split[1] + "\n")
        #print(line)
    file.close()

    wordFile = open(output, 'w', encoding = "utf8")
    wordFile.writelines(words)
    wordFile.close()




if( __name__ == '__main__'):
    dictionary = dictionary("simplified_2014.txt")
    print(dictionary.word_list)