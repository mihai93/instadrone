# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import time
from mobilebrowser import MobileBrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui
import emoji
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

mobileBrowser = MobileBrowser()
mobileBrowser.setUp()

driver = mobileBrowser.getDriver()
wait = WebDriverWait(driver,10)

driver.get('https://www.instagram.com')

loginButton = driver.find_element_by_link_text('Log in')
loginButton.click()

usernameField = driver.find_element_by_xpath("//input[@name='username']")
# usernameField.send_keys('boutiquecannabiscanada')
usernameField.send_keys('charleyjest1')

passwordField = driver.find_element_by_xpath("//input[@name='password']")
# passwordField.send_keys('mng9ui3w')
passwordField.send_keys('test123')

loginButton = driver.find_element_by_xpath("//button[text()='Log in']")
loginButton.click()

# click camera btn
cameraXPath = "//div[contains(@class, 'Camera')]"
wait.until(lambda driver: driver.find_element_by_xpath(cameraXPath))
cameraButton = driver.find_element_by_xpath(cameraXPath)
cameraButton.click()

# select file in browser
time.sleep(1)
pyautogui.typewrite('1.jpg')
time.sleep(0.5)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

# click next btn
nextXPath = "//button[text()='Next']"
wait.until(lambda driver: driver.find_element_by_xpath(nextXPath))
nextButton = driver.find_element_by_xpath(nextXPath)
nextButton.click()

captionXPath = '//textarea[contains(@placeholder, "Write a caption")]'
wait.until(lambda driver: driver.find_element_by_xpath(captionXPath))
captionArea = driver.find_element_by_xpath(captionXPath)
#convert to unicode
# text = "28 GRAM GIVEAWAY 🔥 🍯  💎 💯\nCOMING UP ON AUGUST 28TH #28gOnThe28th\n14g Shatter 🍯  🐝  and 14g CBD Crystalline 💎 💎  💯\nKeep your 👀  peeled cause we're going to be posting a series of photos and they'll be a new chance to enter with every post!\n👇  EACH THING BELOW COUNTS FOR AT LEAST 1 ENTRY 👇\n1️⃣. Repost this picture\n2️⃣. In the repost, write @boutiquecannabiscanada and @boutiquecannabisofficial and caption the tag #28gOnThe28th\n3️⃣. In the repost, tag any and all friends you'd smoke this with (1 tag equals 1 entry, no duplicate tags)\n4️⃣. On this picture, comment below and tag friends you'd smoke it with (again no duplicates)\n6️⃣. DM us pictures/video you'd like us to repost to this page, we love original content 🔥 🔥"
# text = "28 GRAM GIVEAWAY 🍯  💎  ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\nThis is the 3RD post! 3RD chance to enter!\n14g Shatter 🍯  and 14g CBD Crystalline 💎 \n👇  CONTEST RULES (MUST fullfill 1️⃣  - 3️⃣ )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nThe more friends you tag, the better your chances of winning 😀\nDM us anything you'd like to repost, we love original content 👌\nWith ❤️  from @boutiquecannabiscanada 👀 "
text = "Shout out to @hardlyhigh for the pic 😍 \nIf you have anything you want us to repost, DM us 😀 💯\nCheck out our bio and website @boutiquecannabiscanada 👀\n.\n.\n.\n.\n.\n.\n#highlife #canadian #cannabis #dispensary #dabs #chronnoisseurschoice #rosin #weed #weedporn #cannabiscommunity #pot #cloudsovercanada #710society #bud #budtenders #420 #710 #iloveweed #weedstagram #stonernation #hightimes #ganja #bakedinbc #terps #thc #710life #maryjane #buds #shatter #420girls"

# text = text.replace("'", "\\'")  # escape single quotes
text = text.encode('utf-8')  # needed to make format function work
captionArea.click()
time.sleep(1)
driver.execute_script("arguments[0].value = arguments[1]", captionArea, text)
pyautogui.typewrite(' ')
time.sleep(1)

shareButton = driver.find_element_by_xpath("//button[text()='Share']")
shareButton.click()

time.sleep(3)

mobileBrowser.tearDown()
