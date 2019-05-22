# IMPORTS #
##############################
import requests
from bs4 import BeautifulSoup
import tweepy
import time
import random
from pymongo import MongoClient
import pymongo
from Hadith import Hadith




client = pymongo.MongoClient("mongodb+srv://awaris:(fekaA1999)@hadith-deu8y.mongodb.net/test?retryWrites=true")
db = client.test



def isValid(hadithText):
    return (hadithText.isspace() is not True)

def CharCount(narrator, hadithText, bookTitle):
    num = 0
    for _ in build_hadith(narrator, hadithText, bookTitle):
        num += 1
    return num



tweets = list()
invalid_flags = {"chain of transmitters","similar hadith","other traditions"}

##############################
auth = tweepy.OAuthHandler("xbQ6UutSMxBSH0mulveNonzAA",
                           "LkPw21RkBytGp1ZjU4xSkhgDLXg3m7IDR6L6byG4mX8LqidWDq")
auth.set_access_token("1036502449668980736-1OXOStNRQogRIYruMfZl6UtJzqWhp4",
                      "BjY8YFafxDKtV6juNDll6iSBx9mICew2yTzpNuDKRJo4t")
api = tweepy.API(auth)
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
                        narrator = "Narrator Unknown"
                else:
                    narrator = "Narrator Unknown"
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

                obj = Hadith(narrator, hadithText, bookTitle)
                tweets.append(obj.attr())
print(len(tweet))
# db.inventory.insert_many(tweets)
