class HadithObj(object):

    def __init__(self,narrator,hadithText,bookTitle):
        self.narrator = narrator
        self.hadithText = hadithText
        self.bookTitle = bookTitle

    def str(self):
        string = "========================================================================================================================="
        string += "\n" + self.narrator
        string += "\n" + self.hadithText
        string += "\n" + self.bookTitle
        string += "\n" + "========================================================================================================================="
        return string

    def str2(self):
        string = ""
        string += "\n" + self.narrator
        string += "\n" + self.hadithText
        string += "\n" + self.bookTitle
        return string
    def isValid(self):
        return (self.hadithText.isspace() is not True) 
    
    def CharCount(self):
        num = 0
        for _ in self.str2():
            num += 1
        return num
