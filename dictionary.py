
"""
    Dictionary Class
    Arguments: (str) source: name of file with list of words to use as dictionary
"""
class dictionary:
    def __init__(self,source):
        self.source = source
        self.word_list = self.read_word_list(source)
    """
        Reads the 
    """
    def read_word_list(self,source):
        returned = []
        file = open(self.source, 'r', encoding = "utf8")
        for word in file:   # every line in the file will be one word
            returned.append(word.rstrip())
        return returned
    def word_lookup(self,string):
        for word in self.word_list:
            # if string is a word in the dictionary
            if(word == string):
                return True
        # word not found, return none
        return False




"""
    Arguments:
        (str) file_title: title of text file to get from.
                Specified to parse through specific data set from korpusdownload
        (str) output: what to name output text file, must include .txt
    Creates a text file with a list
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