#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, sys, time, requests, praw, re

def authenticateTwitter():
	filename=open('tweepyConfig.txt','r')
	f = filename.readlines()
	filename.close()
	CONSUMER_KEY = f[0].rstrip('\n')
	CONSUMER_SECRET = f[1].rstrip('\n')
	ACCESS_KEY = f[2].rstrip('\n')
	ACCESS_SECRET = f[3].rstrip('\n')
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api
 


def authenticateReddit():
	print('Authenticating...')
	reddit = praw.Reddit('musicbot')
	return reddit

def post(reddit, api):
	# deleteAll()

	for item in reddit.subreddit('trap').hot(limit = 25):
		match = re.findall("https?:\/\/(?:.*\.)?(soundcloud)?(spotify)?\.com\/.*", item.url)
		if match:
			print('Posting...')
			api.update_status("From r/trap " + item.url)
			time.sleep(30)

	for item in reddit.subreddit('hiphopheads').hot(limit = 25):
		match = re.findall("https?:\/\/(?:.*\.)?(soundcloud)?(spotify)?\.com\/.*", item.url)
		if match:
			print('Posting...')
			api.update_status("From r/hiphopheads " + item.url)
			time.sleep(30)

	for item in reddit.subreddit('indieheads').hot(limit = 25):
		match = re.findall("https?:\/\/(?:.*\.)?(soundcloud)?(spotify)?\.com\/.*", item.url)
		if match:
			print('Posting...')
			api.update_status("From r/indieheads " + item.url)
			time.sleep(30)

	for item in reddit.subreddit('electronicmusic').hot(limit = 25):
		match = re.findall("https?:\/\/(?:.*\.)?(soundcloud)?(spotify)?\.com\/.*", item.url)
		if match:
			print('Posting...')
			api.update_status("From r/electronicmusic " + item.url)
			time.sleep(30)


def deleteAll():
	for status in tweepy.Cursor(api.user_timeline).items():
	    try:
	        api.destroy_status(status.id)
	    except:
       		pass

def main():
	reddit = authenticateReddit()
	api = authenticateTwitter()
	post(reddit, api)
	

if __name__ == '__main__':
	main()


