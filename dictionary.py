
"""
    Dictionary Class
    Arguments: (str) source
"""
class dictionary:
    def __init__(self,source):
        self.source = source

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
    create_word_dictionary("zho-mo_web_2015_10K-words.txt","traditional_2014.txt")