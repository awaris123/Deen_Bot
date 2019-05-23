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


def isValid(hadithText):
    return (hadithText.isspace() is not True)

def CharCount(hadith):
    num = 0
    for _ in hadith:
        num += 1
    return num



day = 86400 #
tweets = list()
invalid_flags = {"chain of transmitters","similar hadith","other traditions"}




valid = True
while True:
    randIndex = random.randint(0,40200)
    try:
        tweet = build_hadith(cursor[randIndex]['narrator'], cursor[randIndex]['text'],cursor[randIndex]['title'])

        for flag in invalid_flags:
            if flag in tweet:
                valid = False
                break

        if not isValid(tweet) or CharCount(tweet) > 280:
            valid = False

        if valid:
            api.update_status(tweet)
            time.sleep(day/4)

    except IndexError:
        pass
