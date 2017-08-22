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

# defines whether to use test or actual login
TEST_MODE = True

class InstaDrone:

	def __init__(self):
		if sys.version[0] == '2':
		    reload(sys)
		    sys.setdefaultencoding("utf-8")

		self.mobileBrowser = MobileBrowser()
		self.mobileBrowser.setUp()

		self.driver = self.mobileBrowser.getDriver()
		self.wait = WebDriverWait(self.driver,10)

		logger = logging.getLogger()
		logger.addHandler(logging.StreamHandler())

	def login(self):
		self.driver.get('https://www.instagram.com')

		loginButton = self.driver.find_element_by_link_text('Log in')
		loginButton.click()

		# enter username
		usernameField = self.driver.find_element_by_xpath("//input[@name='username']")

		sleep(randint(1,3))

		if TEST_MODE:
			usernameField.send_keys('charleyjest1')
		else:
			usernameField.send_keys('boutiquecannabiscanada')

		# enter password
		passwordField = self.driver.find_element_by_xpath("//input[@name='password']")

		sleep(randint(1,3))

		if TEST_MODE:
			passwordField.send_keys('test123')
		else:
			passwordField.send_keys('mng9ui3w')

		#click login button
		loginButton = self.driver.find_element_by_xpath("//button[text()='Log in']")
		loginButton.click()

	def post(self, post):
		# click camera btn
		cameraXPath = "//div[contains(@class, 'Camera')]"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(cameraXPath))
		cameraButton = self.driver.find_element_by_xpath(cameraXPath)
		cameraButton.click()

		sleep(randint(1,3))

		# select file in browser
		sleep(0.5)
		pyautogui.typewrite(post.fileName)
		sleep(0.5)
		pyautogui.keyDown('enter')
		pyautogui.keyUp('enter')

		sleep(randint(1,3))

		# wait until file is uploaded before continuing
		nextXPath = "//button[text()='Next']"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(nextXPath))

		# if image is not square, expand view to view entire image
		expandXPath = "//span[contains(@class, 'Expand')]"
		expandButton = self.driver.find_elements_by_xpath(expandXPath)
		if expandButton:
			expandButton[0].click()

		# click next button
		nextButton = self.driver.find_element_by_xpath(nextXPath)
		nextButton.click()

		sleep(randint(1,3))

		# enter caption
		captionXPath = '//textarea[contains(@placeholder, "Write a caption")]'
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(captionXPath))
		captionArea = self.driver.find_element_by_xpath(captionXPath)
	
		# convert to unicode
		# text = text.replace("'", "\\'")  # escape single quotes
		caption = post.caption.encode('utf-8')  # needed to make format function work
		captionArea.click()
		sleep(1)
		self.driver.execute_script("arguments[0].value = arguments[1]", captionArea, caption)
		pyautogui.typewrite(' ')
		sleep(1)

		sleep(randint(1,3))

		# share file
		shareXPath = "//button[text()='Share']"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(shareXPath))
		shareButton = self.driver.find_element_by_xpath(shareXPath)
		shareButton.click()

		self.commentPost(post)

		print('Successfully posted: ' + post.title + ' at time: ' + post.scheduledTime)

	def commentPost(self, post):
		# go to Profile
		profileXPath = "//div[contains(@class, 'Profile')]"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(profileXPath))
		profileButton = self.driver.find_element_by_xpath(profileXPath)
		profileButton.click()

		sleep(randint(1,3))

		# get most recent post
		mostRecentPostXPath = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div/div[2]'
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(mostRecentPostXPath))
		postsElement = self.driver.find_element_by_xpath(mostRecentPostXPath)
		postsElement.click()

		sleep(randint(1,3))
		
		# enter comment
		commentXPath = "//span[contains(@class, 'Comment')]"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(commentXPath))
		commentBtn = self.driver.find_element_by_xpath(commentXPath)
		self.driver.execute_script("arguments[0].scrollIntoView()", commentBtn)
		commentBtn.click()

		commentAreaXPath = '//textarea[contains(@placeholder, "Add a comment")]'
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(commentAreaXPath))
		commentArea = self.driver.find_element_by_xpath(commentAreaXPath)
		self.driver.execute_script("arguments[0].scrollIntoView()", commentArea)
		# commentArea.send_keys(comment)

		comment = post.comment.encode('utf-8')  # needed to make format function work
		sleep(1)
		self.driver.execute_script("arguments[0].value = arguments[1]", commentArea, comment)
		pyautogui.typewrite(' ')
		sleep(1)

		pyautogui.keyDown('enter')
		pyautogui.keyUp('enter')

		print('Successfully commented on post: ' + post.title)

	def halt(self):
		print('Mobile browser tear down...')
		sleep(3)
		self.mobileBrowser.tearDown()

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
		self.fileName = None
		self.caption = None
		self.comment = None
		self.scheduledTime = None
		posts.append(self)

if __name__ == "__main__":
	sched = BlockingScheduler()
	caption = [
			"Canada's most alluring women, Boutique Cannabis Girls. \nCheck out: @boutiquecannabiscanada @boutiquecannabiscanada @boutiquecannabiscanada @boutiquecannabiscanada @boutiquecannabiscanada \nBoutique Cannabis girl: @kwbabyy @mzkaylzz @allthingsamandaa @j.desireexo @apriliciouss @marishika_ \nShooter: @jasegraphics\nMUA: @swankmakeup"
	]
	comment = [
				"\n•\n•\n•\n•\n•\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls",
				"\n•\n•\n•\n•\n•\n#boutiquecannabis #boutiquecannabisgirls #weedgirls #girlswhosmokeweed #follow4follow #love #girlswithtattoos #instagood #cute #photooftheday #tbt #followme #girl #beautiful #happy #picoftheday #instadaily #fitgirls #girlswholift #amazing #Sexy #fashion #igers #fun #summer #instalike #bestoftheday #smile #like4like #instamood"
	]

	guestWhatWednesdayPost = Post("Guess what wednesday")
	guestWhatWednesdayPost.fileName = None
	guestWhatWednesdayPost.caption = "🤔🤔🤔 GUESS the STRAIN & TAG A FRIEND to WIN $100 store credit 🎁🎁🎁 drop by every week for our weekly #guesswhatwednesdays giveaway!! Shout out to @triscuit.farms Peep us @boutiquecannabiscanada 👀"
	guestWhatWednesdayPost.comment = "\n•\n•\n•\n•\n•\n#guesswhatwednesday #bud #buds #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life"
	guestWhatWednesdayPost.scheduledTime = None

	giveawayPost = Post("28 gram giveaway")
	giveawayPost.fileName = '28GramGiveaway.jpg'
	giveawayPost.caption = 	"28 GRAM GIVEAWAY 🍯 💎 ❤️\nONLY 300 CONTESTANTS SO FAR! EVERY POST IS A NEW CHANCE TO WIN!\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nPRIZE 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎 👇  CONTEST RULES (MUST complete all three )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nMore friends you tag, the better your chances of winning 😀\nDM us anything to repost, we love original content 👌\nWith ❤️ from @boutiquecannabiscanada 👀"
	giveawayPost.comment = 	"\n•\n•\n•\n•\n•\n#cbd #shatter #cbdcrystalline #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life"
	# giveawayPost.scheduledTime = '2017-08-22 12:18:00' # format: '2017-08-19 20:16:40'

	budzForBreastsPost = Post("Budz for breasts")
	budzForBreastsPost.fileName = 'BudzForBreasts.jpg'
	budzForBreastsPost.caption = "September 2nd at @theplanetparadise is going to be an amazing evening 🎀 thank you to everyone who's contributing ❤️ @boutiquecannabiscanada 👀"
	budzForBreastsPost.comment = "\n•\n•\n•\n•\n•\n#weedconvention #fundraiser #fuckcancer #cancer #highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #maryjane #buds #giveaway"
	budzForBreastsPost.scheduledTime = '2017-08-22 14:15:30'

	firstGirlPost = Post("First girl post")
	firstGirlPost.fileName = 'girl1.jpg'
	firstGirlPost.caption = "👯Two is always better than one 😉 \nCanada's most alluring women, Boutique Cannabis Girls. \nCheck out: @boutiquecannabiscanada 👀 @boutiquecannabisofficial \nBoutique Cannabis girl: @kwbabyy \nShooter: @jasegraphics\nMUA: @swankmakeup"
	firstGirlPost.comment = "\n•\n•\n•\n•\n•\n#boutiquecannabis #boutiquecannabisgirls #girls #model #girlswhosmokeweed #weedgirls #girlswithtattoos #cute #picoftheday #beautiful #photooftheday #instagood #fun #smile #pretty #follow #hot #instagramers #potd #eyes #beauty #fit #girlswholift #girlswhosquat #fitness #instafit #canadianbabes #canadiangirls #sexy #booty"
	# firstGirlPost.scheduledTime = '2017-08-20 13:30:30'

	genericPost = Post("generic")
	genericPost.comment = "\n•\n•\n•\n•\n•\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls"
	# genericPost.scheduledTime = '2017-08-20 23:53:00'

	# drone = InstaDrone()
	# drone.login()
	# drone.post(guestWhatWednesdayPost)
	# drone.commentPost(guestWhatWednesdayPost)
	# drone.halt()

	for post in posts:
		if post.scheduledTime != None:
			print('Scheduling: ' + post.title + ' for time: ' + post.scheduledTime)
			sched.add_job(autopost, 'date', run_date=post.scheduledTime, kwargs={'post': post})

	sched.start()
