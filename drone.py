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
import emoji
import sys  
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# defines whether to use test or actual login
TEST_MODE = True

class InstaDrone:

	def __init__(self):
		reload(sys)  
		sys.setdefaultencoding('utf8')

		self.mobileBrowser = MobileBrowser()
		self.mobileBrowser.setUp()

		self.driver = self.mobileBrowser.getDriver()
		self.wait = WebDriverWait(self.driver,10)

	def login(self):
		self.driver.get('https://www.instagram.com')

		loginButton = self.driver.find_element_by_link_text('Log in')
		loginButton.click()

		# enter username
		usernameField = self.driver.find_element_by_xpath("//input[@name='username']")

		if TEST_MODE:
			usernameField.send_keys('charleyjest1')
		else:
			usernameField.send_keys('boutiquecannabiscanada')

		# enter password
		passwordField = self.driver.find_element_by_xpath("//input[@name='password']")

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

		# select file in browser
		time.sleep(1)
		pyautogui.typewrite(fileName)
		time.sleep(0.5)
		pyautogui.keyDown('enter')
		pyautogui.keyUp('enter')

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

		# enter caption
		captionXPath = '//textarea[contains(@placeholder, "Write a caption")]'
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(captionXPath))
		captionArea = self.driver.find_element_by_xpath(captionXPath)
	
		# convert to unicode
		# text = text.replace("'", "\\'")  # escape single quotes
		caption = caption.encode('utf-8')  # needed to make format function work
		captionArea.click()
		time.sleep(1)
		self.driver.execute_script("arguments[0].value = arguments[1]", captionArea, caption)
		pyautogui.typewrite(' ')
		time.sleep(1)

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

		# get most recent post
		mostRecentPostXPath = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div/div[2]'
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(mostRecentPostXPath))
		postsElement = self.driver.find_element_by_xpath(mostRecentPostXPath)
		postsElement.click()
		
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
		time.sleep(1)
		self.driver.execute_script("arguments[0].value = arguments[1]", commentArea, comment)
		pyautogui.typewrite(' ')
		time.sleep(1)

		pyautogui.keyDown('enter')
		pyautogui.keyUp('enter')

	def halt(self):
		print('shutting down...')
		time.sleep(3)
		self.mobileBrowser.tearDown()

def my_job(fileName=None, caption=None, comment=None):
    drone = InstaDrone()
    drone.login()
    drone.post(fileName, caption)
    drone.commentPost(comment)
    drone.halt()

if __name__ == "__main__":
	sched = BlockingScheduler()

	fileName = ['1.jpg', '2.jpeg', '3.jpg']
	# text = "28 GRAM GIVEAWAY 🍯  💎  ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nThis is the 3RD post! 3RD chance to enter!\n14g Shatter 🍯  and 14g CBD Crystalline 💎 \n👇  CONTEST RULES (MUST fullfill 1️⃣  - 3️⃣ )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nThe more friends you tag, the better your chances of winning 😀\nDM us anything you'd like to repost, we love original content 👌\nWith ❤️  from @boutiquecannabiscanada 👀 "
	caption = [
			"28 GRAM GIVEAWAY 🍯 💎 ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nPRIZE 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎 👇  CONTEST RULES (MUST complete all three )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nMore friends you tag, the better your chances of winning 😀\nDM us anything to repost, we love original content 👌\nWith ❤️ from @boutiquecannabiscanada 👀",
			"MADE IT TO 1K FOLLOWERS! ❤️  \nAs a thank you to all our followers we're running a sale on our website right now, use code: FUNAUG  ❤️  \nPeep @boutiquecannabiscanada 👀",
			"Some OC from @triscuit.farms 😍 \nGiveaway going on right now 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎\n Check out our bio @boutiquecannabiscanada 👀  \nand all girls page @boutiquecannabisofficial 👀"
	]
	comment = [
				"\n•\n•\n•\n•\n•\n#cbd #shatter #cbdcrystalline #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life",
				"\n•\n•\n•\n•\n•\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls"
	]

	# drone = InstaDrone()
	# drone.login()
	# drone.post(fileName[2], caption[1])
	# drone.commentPost(comment[1])
    # drone.halt()

	# sched.add_job(my_job, 'date', run_date='2017-08-15 14:28:25', kwargs={'fileName': fileName[0], 'caption': caption[0], 'comment': comment[0]})
	# sched.add_job(my_job, 'date', run_date='2017-08-15 16:54:00', kwargs={'fileName': fileName[2], 'caption': caption[2], 'comment': comment[1]})
	# sched.start()
