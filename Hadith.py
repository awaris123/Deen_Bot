class Hadith:
    """ Hadith Class to store components """

    def __init__(self, narrator="", hadithText="", bookTitle=""):
        self.narrator = narrator
        self.hadithText = hadithText
        self.bookTitle = bookTitle

    def attr(self):
        dict = {
        "narrator" : self.narrator,
        "text" : self.hadithText,
        "title" : self.bookTitle
        }
        return dict
