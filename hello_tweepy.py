import tweepy
import time

auth = tweepy.OAuthHandler("xbQ6UutSMxBSH0mulveNonzAA", "LkPw21RkBytGp1ZjU4xSkhgDLXg3m7IDR6L6byG4mX8LqidWDq" )
auth.set_access_token("1036502449668980736-1OXOStNRQogRIYruMfZl6UtJzqWhp4","BjY8YFafxDKtV6juNDll6iSBx9mICew2yTzpNuDKRJo4t")

api = tweepy.API(auth)

filename = open("helloworld.txt",'r')
f = filename.readlines()
filename.close()

hour = 3600 # Hours in Seconds
day = 24*hour # Day
count = 0
mess = ""
for line in f:
	mess += line

	count += 1
	if count % 3 == 0:
		numChar = 0
		for char in mess:
			numChar += 1
		if numChar < 281:
			# api.update_status(mess)
			print(mess)
		mess = ""
	  # Tweet every day





