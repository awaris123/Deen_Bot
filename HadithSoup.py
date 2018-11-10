# IMPORTS #
##############################
import requests
from bs4 import BeautifulSoup
from HadithObj import HadithObj
##############################

# DOWNLOADS WEBSITE HTML AND CREATES REFERENCE FOR EACH HADITH BOOK AND STORES IN LIST HADITHBOOKS #
##############################################################################
webPage = requests.get("https://sunnah.com/")

dataSet = BeautifulSoup(webPage.content,"html.parser")

hadithBooks = dataSet.find_all(class_ = "collection_title")
###############################################################################

#  NESTED FOR-LOOP TO ITERATE THROUGH EACH HADITH BOOK AND PARSE INFO#
###############################################################################
for book in hadithBooks:
    
    # CREATES A LIST OF ALL TAGS WITH LINK TO HADITH BOOK PAGE STORES IN VAR ROUTE #
    #########################################
    BookCollection = (list(book.children))
    tag = book.find("a",href = True)
    route = tag['href']
    bookTitle = route[1:len(route)]
    firstChar = bookTitle[0].upper()
    bookTitle = firstChar + bookTitle[1:len(bookTitle)]
    #########################################

    # DOWNLOADS PAGE FOR EACH HADITH BOOK AND CREATES LIST OF SUBSECTIONS/TOPICS AND STORES IN LIST HADITHSECTIONS #
    #################################################################
    bookWebPage = requests.get("https://sunnah.com"+route) 
    Sections = BeautifulSoup(bookWebPage.content,"html.parser")
    hadithSections = Sections.find_all(class_ = "book_titles")
    #################################################################

    # NESTED FOR-LOOP THAT ITERATES THROUGH EACH HADITH SECTION AND STORES LINKS FOR HADITH IN LIST TAGS, STORES LINK IN VAR SUBROUTE #
    ################################################
    for section in hadithSections:
        tags = section.find_all("a",href = True)
        for tag2 in tags:
            subRoute = tag2['href']
    #################################################

            # DOWNLOADS PAGE FOR EACH SPECIFIC HADITH, STORES ALL HADITH COMPONENTS IN VAR HADITHCOLLECTIONS #
            ####################################################################################
            subHadithwebPage = requests.get("https://sunnah.com"+subRoute)
            subHadithSections = BeautifulSoup(subHadithwebPage.content,"html.parser")
            hadithCollections = subHadithSections.find_all(class_ = "actualHadithContainer")
            ####################################################################################

            # FOR-LOOP TO ITERATE THROUGH HADITH ELEMENTS #
            for collection in hadithCollections:
                # STORES HADITH ELEMENTS IN VAR HADITH #
                ##########################################################
                hadith = collection.find(class_ = "englishcontainer")
              
                
                ##########################################################
              
                # STORES NARRATION ELEMENT FROM HADITH IN VAR NARRARTOR #
                ############################################################
                narrator = hadith.find(class_ = "english_hadith_full")
                narrator = narrator.find(class_ = "hadith_narrated")
                if narrator is not None:
                    if narrator.get_text() is not None:
                        narrator = narrator.get_text()
                    else:
                        narrator
                else:
                    narrator = "missing data"
                ############################################################

                # STORES HADITH TEXT ELEMENT FROM HADITH IN VAR HADITHTEXT #
                ###############################################################
                hadithText = hadith.find(class_="english_hadith_full")
                hadithText = hadithText.find(class_="text_details")
                if hadithText is not None:
                    if hadithText.get_text() is not None:
                        hadithText = hadithText.get_text()
                    else:
                        hadithText = "missing data"
                else:
                    hadithText = "missing data"
                ################################################################

                h = HadithObj(narrator,hadithText,bookTitle)
            
              
                print(h.str())
                print(h.isValid())