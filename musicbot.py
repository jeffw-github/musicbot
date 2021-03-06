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
	# print('Authenticating...')
	reddit = praw.Reddit('musicbot')
	return reddit

def post(reddit, api):
	# deleteAll(api)

	subreddits = ['indieheads', 'hiphopheads', 'electronicmusic', 'trap']

	for sr in subreddits:
		for item in reddit.subreddit(sr).hot(limit = 15):
			match = re.findall("https?:\/\/(?:.*\.)?(soundcloud)?(spotify)?\.com\/.*", item.url)
			if match:
				print('Posting...')
				postText = item.title + " (r/" + sr + ") " + item.url

				# shorten title with post text over 140 by adding ..
				# twitter counts all url as 23 characters
				if len(postText) - len(item.url) + 23 > 140:
					lenToRemove = len(postText) - 140
					postText = item.title[:lenToRemove + 2] + ".." + " (r/" + sr + ") " + item.url
				try:
					api.update_status(postText)
					print('Posted!')
				except:
					# TODO: see what exception is being passed
					print(Exception)
					pass
				time.sleep(30)


def deleteAll(api):
	for status in tweepy.Cursor(api.user_timeline).items():
	    try:
	        api.destroy_status(status.id)
	    except:
       		pass

def main():
	reddit = authenticateReddit()
	api = authenticateTwitter()
	while True: 
		post(reddit, api)
		time.sleep(86400)
	


if __name__ == '__main__':
	main()
