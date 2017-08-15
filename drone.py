# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import time
from mobilebrowser import MobileBrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import emoji
import sys  
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

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

		usernameField = self.driver.find_element_by_xpath("//input[@name='username']")
		usernameField.send_keys('boutiquecannabiscanada')
		# usernameField.send_keys('charleyjest1')

		passwordField = self.driver.find_element_by_xpath("//input[@name='password']")
		passwordField.send_keys('mng9ui3w')
		# passwordField.send_keys('test123')

		loginButton = self.driver.find_element_by_xpath("//button[text()='Log in']")
		loginButton.click()

	def post(self, fileName, text):
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

		# click next btn
		nextXPath = "//button[text()='Next']"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(nextXPath))
		nextButton = self.driver.find_element_by_xpath(nextXPath)
		nextButton.click()

		captionXPath = '//textarea[contains(@placeholder, "Write a caption")]'
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(captionXPath))
		captionArea = self.driver.find_element_by_xpath(captionXPath)
		#convert to unicode
		# text = "28 GRAM GIVEAWAY 🔥 🍯  💎 💯\nCOMING UP ON AUGUST 28TH #28gOnThe28th\n14g Shatter 🍯  🐝  and 14g CBD Crystalline 💎 💎  💯\nKeep your 👀  peeled cause we're going to be posting a series of photos and they'll be a new chance to enter with every post!\n👇  EACH THING BELOW COUNTS FOR AT LEAST 1 ENTRY 👇\n1️⃣. Repost this picture\n2️⃣. In the repost, write @boutiquecannabiscanada and @boutiquecannabisofficial and caption the tag #28gOnThe28th\n3️⃣. In the repost, tag any and all friends you'd smoke this with (1 tag equals 1 entry, no duplicate tags)\n4️⃣. On this picture, comment below and tag friends you'd smoke it with (again no duplicates)\n6️⃣. DM us pictures/video you'd like us to repost to this page, we love original content 🔥 🔥"
	

		# text = text.replace("'", "\\'")  # escape single quotes
		text = text.encode('utf-8')  # needed to make format function work
		captionArea.click()
		time.sleep(1)
		self.driver.execute_script("arguments[0].value = arguments[1]", captionArea, text)
		pyautogui.typewrite(' ')
		time.sleep(1)

		shareButton = self.driver.find_element_by_xpath("//button[text()='Share']")
		shareButton.click()

	def commentPost(self, comment):
		profileXPath = "//div[contains(@class, 'Profile')]"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(profileXPath))
		profileButton = self.driver.find_element_by_xpath(profileXPath)
		profileButton.click()

		self.wait.until(lambda driver: self.driver.find_element_by_xpath("//*[contains(text(), ' posts')]"))
		postsElement = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div/div[2]')
		postsElement.click()
		
		commentXPath = "//span[contains(@class, 'Comment')]"
		self.wait.until(lambda driver: self.driver.find_element_by_xpath(commentXPath))
		commentBtn = self.driver.find_element_by_xpath(commentXPath)
		commentBtn.click()

		commentAreaXPath = '//textarea[contains(@placeholder, "Add a comment")]'
		commentArea = self.driver.find_element_by_xpath(commentAreaXPath)
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

	fileName = '1.jpg'
	# text = "28 GRAM GIVEAWAY 🍯  💎  ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nThis is the 3RD post! 3RD chance to enter!\n14g Shatter 🍯  and 14g CBD Crystalline 💎 \n👇  CONTEST RULES (MUST fullfill 1️⃣  - 3️⃣ )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nThe more friends you tag, the better your chances of winning 😀\nDM us anything you'd like to repost, we love original content 👌\nWith ❤️  from @boutiquecannabiscanada 👀 "
	text = "28 GRAM GIVEAWAY 🍯 💎 ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nPRIZE 👉 14g Shatter 🍯🐝 and 14g CBD Crystalline 💎💎 👇  CONTEST RULES (MUST complete all three )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nMore friends you tag, the better your chances of winning 😀\nDM us anything to repost, we love original content 👌\nWith ❤️ from @boutiquecannabiscanada 👀"
	comment = "•\n•\n•\n•\n•\n#cbd #shatter #cbdcrystalline #giveaway #giveaways #follow #like #love #highlife #canadian #cannabis #dispensary #dabs #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #420 #710 #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life"

	# drone = InstaDrone()
	# drone.login()
	# drone.post(fileName, text)
	# drone.commentPost(comment)
    # drone.halt()

	sched.add_job(my_job, 'date', run_date='2017-08-15 07:10:00', kwargs={'fileName': fileName, 'caption': text, 'comment': comment})
	sched.add_job(my_job, 'date', run_date='2017-08-15 12:10:00', kwargs={'fileName': fileName, 'caption': text, 'comment': comment})
	sched.start()
