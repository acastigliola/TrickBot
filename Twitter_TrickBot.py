####################################
##TrickBot v1.0  Twitter Deployment
##
## Written by Angelo Castigliola III
####################################

from __future__ import absolute_import, print_function

import tweepy
import time

# Import ChatterBot Libraries.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="CONSUMER KEY"
consumer_secret="CONSUMER SECRET"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="ACCESS TOKEN"
access_token_secret="ACCESS TOKEN SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

#Read the timeline.
timeline = api.home_timeline()
for tweet in timeline:
	print(f"{tweet.user.name} said {tweet.text}")
	# Get a response to the input tweet above 'I would like to book a flight.'
	print("---------------------------------------------")
	print("Sending Tweet To L0ra")
	print("---------------------------------------------")
	response = chatbot.get_response(tweet.text)
	print("L0ra said:",response)
	#Reply to tweet.
	status = str(tweet.user.name) + ": " + str(response)
	print("---------------------------------------------")
	print("Sending Tweet:",status)
	api.update_status(status)
	#Sleep
	print("Sleeping for 1 minute...")
	print("------------------------------------------------------------------------------")
	time.sleep(60)
