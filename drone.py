# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import time
from mobilebrowser import MobileBrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException        
from selenium.webdriver.common.keys import Keys
import pyautogui
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from random import randint
from time import sleep
import logging
import os
import sys
from pymongo import MongoClient

from InstaDrone import InstaDrone

def createPosts():
	guestWhatWednesdayPost = Post("Guess what wednesday")
	guestWhatWednesdayPost.image = 'GWW-Aug23.jpg'
	guestWhatWednesdayPost.caption = "🤔🤔🤔 SPECIAL WEEK! REPOST this picture and get a chance to WIN $100 store credit 	and as always... GUESS the STRAIN & TAG A FRIEND to WIN $100 store credit 🎁🎁🎁 drop by every week for our weekly #guesswhatwednesdays giveaway!! Peep us @boutiquecannabiscanada 👀"
	guestWhatWednesdayPost.comment = "\n•\n•\n•\n•\n•\n#guesswhatwednesday #bud #buds #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life"
	# guestWhatWednesdayPost.scheduledTime = '2017-08-23 01:29:45'

	guessWhatWedWinnerPost = Post("Guess what winner")
	guessWhatWedWinnerPost.image = 'GuessWhatWinnerAug23.jpg'
	guessWhatWedWinnerPost.caption = "#GUESSWHATWEDNESDAY WINNER is @smoketogether_staytogether2213 ! 🎁🎁 She wins for doing a repost, unfortunately nobody guessed correctly, the strain was CBD Sunkiss.  👉 The other $100 will be given away next Wednesday, so the prize will be even larger! Come back next Wednesday 💯  ❤️ GIVEAWAY GOING ON! PRIZE 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎 Check out: @boutiquecannabiscanada 👀"
	guessWhatWedWinnerPost.comment = "\n•\n•\n•\n•\n•\n#guesswhatwednesday #bud #buds #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life"
	guessWhatWedWinnerPost.scheduledTime = None

	giveawayPost = Post("28 gram giveaway")
	giveawayPost.image = '28GramGiveaway.jpg'
	giveawayPost.caption = "28 GRAM GIVEAWAY 🍯 💎 ❤️\nONLY 300 CONTESTANTS SO FAR! EVERY POST IS A NEW CHANCE TO WIN!\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nPRIZE 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎 👇  CONTEST RULES (MUST complete all three )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nMore friends you tag, the better your chances of winning 😀\nDM us anything to repost, we love original content 👌\nWith ❤️ from @boutiquecannabiscanada 👀"
	giveawayPost.comment = "\n•\n•\n•\n•\n•\n#cbd #shatter #cbdcrystalline #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life"
	giveawayPost.scheduledTime = '2017-08-23 22:46:10'  # format: '2017-08-19 20:16:40'

	budzForBreastsPost = Post("Budz for breasts")
	budzForBreastsPost.image = 'BudzForBreasts.jpg'
	budzForBreastsPost.caption = "September 2nd at @theplanetparadise is going to be an amazing evening 🎀 thank you to everyone who's contributing ❤️ @boutiquecannabiscanada 👀"
	budzForBreastsPost.comment = "\n•\n•\n•\n•\n•\n#weedconvention #fundraiser #fuckcancer #cancer #highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #maryjane #buds #giveaway"
	# budzForBreastsPost.scheduledTime = '2017-08-23 01:03:30'

	firstGirlPost = Post("First girl post")
	firstGirlPost.image = 'girl1.jpg'
	firstGirlPost.caption = "👯Two is always better than one 😉 \nCanada's most alluring women, Boutique Cannabis Girls. \nCheck out: @boutiquecannabiscanada 👀 @boutiquecannabisofficial \nBoutique Cannabis girl: @kwbabyy \nShooter: @jasegraphics\nMUA: @swankmakeup"
	firstGirlPost.comment = "\n•\n•\n•\n•\n•\n#boutiquecannabis #boutiquecannabisgirls #girls #model #girlswhosmokeweed #weedgirls #girlswithtattoos #cute #picoftheday #beautiful #photooftheday #instagood #fun #smile #pretty #follow #hot #instagramers #potd #eyes #beauty #fit #girlswholift #girlswhosquat #fitness #instafit #canadianbabes #canadiangirls #sexy #booty"
	# firstGirlPost.scheduledTime = '2017-08-20 13:30:30'

	genericPost = Post("generic")
	genericPost.comment = "\n•\n•\n•\n•\n•\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls"

def autopost(post=None):
    drone = InstaDrone()
    drone.login()
    drone.post(post)
    # drone.commentPost(post)
    drone.halt()
    print('Successfully autoposted ' + post.title)

posts = []

class Post:
	def __init__(self, title):
		self.id = id(self)
		self.title = title
		self.image = None
		self.caption = None
		self.comment = None
		self.postNow = False
		self.scheduledTime = None
		posts.append(self)


if __name__ == "__main__":
	comment = [
				"\n•\n•\n•\n•\n•\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls",
				"\n•\n•\n•\n•\n•\n#boutiquecannabis #boutiquecannabisgirls #weedgirls #girlswhosmokeweed #follow4follow #love #girlswithtattoos #instagood #cute #photooftheday #tbt #followme #girl #beautiful #happy #picoftheday #instadaily #fitgirls #girlswholift #amazing #Sexy #fashion #igers #fun #summer #instalike #bestoftheday #smile #like4like #instamood"
	]

	sched = BlockingScheduler()
	createPosts()

	for post in posts:
		if post.scheduledTime != None:
			print('Scheduling: ' + post.title + ' for time: ' + post.scheduledTime)
			sched.add_job(autopost, 'date', run_date=post.scheduledTime, kwargs={'post': post})
		else:
			drone = InstaDrone()
			drone.login()
			drone.post(post)
			drone.halt()

	sched.start()