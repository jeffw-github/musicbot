#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, sys, time, requests, praw, re

filename=open('AuthFiles/tweepyConfig.txt','r')
f = filename.readlines()
CONSUMER_KEY = f[0].rstrip('\n')
CONSUMER_SECRET = f[1].rstrip('\n')
ACCESS_KEY = f[2].rstrip('\n')
ACCESS_SECRET = f[3].rstrip('\n')
filename.close()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 


def authenticateReddit():
	print('Authenticating...')
	reddit = praw.Reddit('./AuthFiles/musicbot')
	return reddit

def post(reddit):
	# deleteAll()
	i = 0
	for item in reddit.subreddit('trap').hot(limit = 25):
		match = re.findall("https?:\/\/(?:www\.)?(soundcloud)?(spotify)?\.com\/.*", item.url)
		if match:
			print('Posting...')
			api.update_status(item.url)
			time.sleep(30)
		# i += 1
		# if i == 15:
		# 	break

def deleteAll():
	for status in tweepy.Cursor(api.user_timeline).items():
	    try:
	        api.destroy_status(status.id)
	    except:
       		pass

def main():
	reddit = authenticateReddit()
	post(reddit)
	

if __name__ == '__main__':
	main()


