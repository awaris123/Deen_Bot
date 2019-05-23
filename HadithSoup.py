# IMPORTS #
##############################
import tweepy
import time
import random
from pymongo import MongoClient
import pymongo


#  Mongo DB Connection
client = pymongo.MongoClient("mongodb+srv://awaris:(fekaA1999)@hadith-deu8y.mongodb.net/test?retryWrites=true")
db = client.test
cursor = db.inventory.find({})

# Twitter OAuth tokens
auth = tweepy.OAuthHandler("xbQ6UutSMxBSH0mulveNonzAA",
                           "LkPw21RkBytGp1ZjU4xSkhgDLXg3m7IDR6L6byG4mX8LqidWDq")
auth.set_access_token("1036502449668980736-1OXOStNRQogRIYruMfZl6UtJzqWhp4",
                      "BjY8YFafxDKtV6juNDll6iSBx9mICew2yTzpNuDKRJo4t")
api = tweepy.API(auth)


# Helper Functions

def build_hadith(narrator, hadithText, bookTitle):
    string = ""
    string += "\n" + narrator
    string += "\n" + hadithText
    string += "\n" + bookTitle
    return string


def isValid(narr, hadithText, book):
    return (not narr.isspace() and not hadithText.isspace() and not book.isspace())

def CharCount(hadith):
    num = 0
    for _ in hadith:
        num += 1
    return num


minute = 60
hour = 60 * minute
day = 24 * hour

tweets = list()
invalid_flags = {"chain of transmitters","similar hadith","other traditions"}




valid = True
while True:
    randIndex = random.randint(0,40720)

    narrator, text, title = cursor[randIndex]['narrator'], cursor[randIndex]['text'],cursor[randIndex]['title']
    tweet = build_hadith(narrator, text, title)

    for flag in invalid_flags:
        if flag in tweet:
            valid = False
            break

    if isValid(narrator,text,title) and CharCount(tweet) < 281 and valid:
        api.update_status(tweet)
        time.sleep(day/4)
