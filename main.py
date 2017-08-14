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
wait = WebDriverWait(driver,100)

driver.get('https://www.instagram.com')

loginButton = driver.find_element_by_link_text('Log in')
loginButton.click()

usernameField = driver.find_element_by_xpath("//input[@name='username']")
usernameField.send_keys('boutiquecannabiscanada')
# usernameField.send_keys('charleyjest1')

passwordField = driver.find_element_by_xpath("//input[@name='password']")
passwordField.send_keys('mng9ui3w')
# passwordField.send_keys('test123')

loginButton = driver.find_element_by_xpath("//button[text()='Log in']")
loginButton.click()

time.sleep(8)

cameraButton = driver.find_element_by_xpath("//div[contains(@class, 'Camera')]")
cameraButton.click()

time.sleep(3)

pyautogui.keyDown('down')
pyautogui.keyUp('down')

time.sleep(0.5)

pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

time.sleep(3)

nextButton = driver.find_element_by_xpath("//button[text()='Next']")
nextButton.click()

time.sleep(2)

textArea = driver.find_element_by_xpath('//textarea[contains(@placeholder, "Write a caption")]')
#convert to unicode
text = "28 GRAM GIVEAWAY 🔥 🍯  💎 💯\nCOMING UP ON AUGUST 28TH #28gOnThe28th\n14g Shatter 🍯  🐝  and 14g CBD Crystalline 💎 💎  💯\nKeep your 👀  peeled cause we're going to be posting a series of photos and they'll be a new chance to enter with every post!\n👇  EACH THING BELOW COUNTS FOR AT LEAST 1 ENTRY 👇\n1️⃣. Repost this picture\n2️⃣. In the repost, write @boutiquecannabiscanada and @boutiquecannabisofficial and caption the tag #28gOnThe28th\n3️⃣. In the repost, tag any and all friends you'd smoke this with (1 tag equals 1 entry, no duplicate tags)\n4️⃣. On this picture, comment below and tag friends you'd smoke it with (again no duplicates)\n6️⃣. DM us pictures/video you'd like us to repost to this page, we love original content 🔥 🔥"
text = "28 GRAM GIVEAWAY 🍯  💎  ❤️\nCOMING UP ON AUGUST 28TH #28gOnThe28th\n14g Shatter 🍯  and 14g CBD Crystalline 💎 \n👇  CONTEST RULES (MUST fullfill 1️⃣  - 3️⃣ )👇\n1️⃣. FOLLOW @boutiquecannabiscanada 👀 \n2️⃣. REPOST this picture, make sure to tag us \n3️⃣. LIKE & COMMENT below, tag friends you'd smoke with 💨\nThe more friends you tag, the better your chances of winning 😀\nDM us anything you'd like to repost, we love original content 👌\nWith ❤️  from @boutiquecannabiscanada 👀 "

# text = text.replace("'", "\\'")  # escape single quotes
text = text.encode('utf-8')  # needed to make format function work
textArea.click()
time.sleep(1)
driver.execute_script("arguments[0].value = arguments[1]", textArea, text)
pyautogui.typewrite(' ')
time.sleep(2)

shareButton = driver.find_element_by_xpath("//button[text()='Share']")
shareButton.click()
