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

#python3
# from importlib import reload

# defines whether to use test or actual login
TEST_MODE = False

# class Post:
# 	def __init__(self, title):
#         self.id = id(self)
#         self.title = title
#         self.fileName = fileName
#         self.caption = caption
#         self.comment = comment
#         self.scheduledTime = scheduledTime

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

	def post(self, fileName, caption):
		# click camera btn
		cameraXPath = "//div[contains(@class, 'Camera')]"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(cameraXPath))
		cameraButton = self.driver.find_element_by_xpath(cameraXPath)
		cameraButton.click()

		sleep(randint(1,3))

		# select file in browser
		sleep(0.5)
		pyautogui.typewrite(fileName)
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
		caption = caption.encode('utf-8')  # needed to make format function work
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

	def commentPost(self, comment):
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

		comment = comment.encode('utf-8')  # needed to make format function work
		sleep(1)
		self.driver.execute_script("arguments[0].value = arguments[1]", commentArea, comment)
		pyautogui.typewrite(' ')
		sleep(1)

		pyautogui.keyDown('enter')
		pyautogui.keyUp('enter')

	def halt(self):
		print('shutting down...')
		sleep(3)
		self.mobileBrowser.tearDown()

def my_job(fileName=None, caption=None, comment=None):
    drone = InstaDrone()
    drone.login()
    drone.post(fileName, caption)
    drone.commentPost(comment)
    drone.halt()

if __name__ == "__main__":
	sched = BlockingScheduler()

	fileName = ['1.jpg', '2.jpeg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.JPG', '8.jpg', '9.jpg', '10.JPG']
	# text = "28 GRAM GIVEAWAY 🍯  💎  ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nThis is the 3RD post! 3RD chance to enter!\n14g Shatter 🍯  and 14g CBD Crystalline 💎 \n👇  CONTEST RULES (MUST fullfill 1️⃣  - 3️⃣ )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nThe more friends you tag, the better your chances of winning 😀\nDM us anything you'd like to repost, we love original content 👌\nWith ❤️  from @boutiquecannabiscanada 👀 "
	caption = [
			"28 GRAM GIVEAWAY 🍯 💎 ❤️\nEVERY POST IS A NEW CHANCE TO WIN!\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nPRIZE 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎 👇  CONTEST RULES (MUST complete all three )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nMore friends you tag, the better your chances of winning 😀\nDM us anything to repost, we love original content 👌\nWith ❤️ from @boutiquecannabiscanada 👀",
			"MADE IT TO 1K FOLLOWERS! ❤️  \nAs a thank you to all our followers we're running a sale on our website right now, use code: FUNAUG  ❤️  \nPeep @boutiquecannabiscanada 👀",
			"Some OC from @triscuit.farms 😍 \nGiveaway going on right now 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎\n Check out our bio @boutiquecannabiscanada 👀  \nand all girls page @boutiquecannabisofficial 👀",
			"Shout out to @cannaprincess1990 😍 \nGiveaway going on right now 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎\n Check out our bio @boutiquecannabiscanada 👀  \nand all girls page @boutiquecannabisofficial 👀",
			"🤔🤔🤔 GUESS the STRAIN & TAG A FRIEND to WIN $100 store credit 🎁🎁🎁 drop by every week for our weekly #guesswhatwednesdays giveaway!! Shout out to @triscuit.farms Peep us @boutiquecannabiscanada 👀",
			"#GUESSWHATWEDNESDAY WINNER @dylanthiessen52 🎁 🎁  There were multiple correct guesses, so we picked the first ! Come back next week, they'll be more prizes and more winners 👈 💯 \n🎁 🎁  Giveaway going on right now 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎  Check out @boutiquecannabiscanada 👀",
			"Check out our delicious edibles 👅 😛 😋 💦  Peep our bio @boutiquecannabiscanada",
			"September 2nd at @theplanetparadise is going to be an amazing evening 🎀 thank you to everyone who's contributing ❤️ @boutiquecannabiscanada 👀",
			"Canada's most alluring women, Boutique Cannabis Girls. \nCheck out: @boutiquecannabiscanada @boutiquecannabiscanada @boutiquecannabiscanada @boutiquecannabiscanada @boutiquecannabiscanada \nBoutique Cannabis girl: @kwbabyy @mzkaylzz @allthingsamandaa @j.desireexo @apriliciouss @marishika_ \nShooter: @jasegraphics\nMUA: @swankmakeup",
			"Wise words from Carl Sagan 😂 😂 What's everyone smoking on today?"
	]
	comment = [
				"\n•\n•\n•\n•\n•\n#guesswhatwednesday #bud #buds #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life",
				"\n•\n•\n•\n•\n•\n#cbd #shatter #cbdcrystalline #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life",
				"\n•\n•\n•\n•\n•\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls",
				# for budz for breasts
				"\n•\n•\n•\n•\n•\n#weedconvention #fundraiser #fuckcancer #cancer #highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #maryjane #buds #giveaway",
				"\n•\n•\n•\n•\n•\n#Boutiquecannabis #boutiquecannabisgirls #weedgirls #girlswhosmokeweed #follow4follow #love #girlswithtattoos #instagood #cute #photooftheday #tbt #followme #girl #beautiful #happy #picoftheday #instadaily #fitgirls #girlswholift #amazing #Sexy #fashion #igers #fun #summer #instalike #bestoftheday #smile #like4like #instamood"
	]

	# drone = InstaDrone()
	# drone.login()
	# drone.post(fileName[0], caption[0])
	# drone.commentPost(comment[1])
	# drone.halt()

    # guess what wed
	# sched.add_job(my_job, 'date', run_date='2017-08-16 18:30:30', kwargs={'fileName': fileName[4], 'caption': caption[4], 'comment': comment[0]})
	# 28 gram giveaway
	sched.add_job(my_job, 'date', run_date='2017-08-19 16:19:00', kwargs={'fileName': fileName[0], 'caption': caption[0], 'comment': comment[1]})
	# carl sagan
	sched.add_job(my_job, 'date', run_date='2017-08-19 19:00:00', kwargs={'fileName': fileName[9], 'caption': caption[9], 'comment': comment[2]})
	# boutique canna girl 
	# sched.add_job(my_job, 'date', run_date='2017-08-19 15:05:40', kwargs={'fileName': fileName[8], 'caption': caption[8], 'comment': comment[4]})
	# edible
	# sched.add_job(my_job, 'date', run_date='2017-08-17 17:59:00', kwargs={'fileName': fileName[6], 'caption': caption[6], 'comment': comment[2]})
	# budz 4 breasts
	# sched.add_job(my_job, 'date', run_date='2017-08-18 13:00:00', kwargs={'fileName': fileName[7], 'caption': caption[7], 'comment': comment[3]})
	sched.start()
