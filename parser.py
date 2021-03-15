
from dictionary import dictionary
class parser:
    def __init__(self,source):
        self.dictionary = dictionary(source)

if (__name__ == "__main__"):
    d = dictionary("simplified_2014.txt")
    print(d.word_lookup("没有"))
    parser = parser("simplified_2014.txt")

