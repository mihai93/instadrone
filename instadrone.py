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

IMAGE_PATH = 'images'

# defines whether to use test or actual login
TEST_MODE = False

class InstaDrone:
    def __init__(self):
        if sys.version[0] == '2':
            reload(sys)
            sys.setdefaultencoding("utf-8")

        self.mobileBrowser = MobileBrowser()
        self.mobileBrowser.setUp()

        self.driver = self.mobileBrowser.getDriver()
        self.wait = WebDriverWait(self.driver, 10)

        logger = logging.getLogger()
        logger.addHandler(logging.StreamHandler())

    def login(self):
        self.driver.get('https://www.instagram.com')

        loginButton = self.driver.find_element_by_link_text('Log in')
        loginButton.click()

        # enter username
        usernameField = self.driver.find_element_by_xpath("//input[@name='username']")

        sleep(randint(1, 3))

        if TEST_MODE:
            usernameField.send_keys('charleyjest1')
        else:
            usernameField.send_keys('boutiquecannabiscanada')

        # enter password
        passwordField = self.driver.find_element_by_xpath("//input[@name='password']")

        sleep(randint(1, 3))

        if TEST_MODE:
            passwordField.send_keys('test123')
        else:
            passwordField.send_keys('mng9ui3w')

        # click login button
        loginButton = self.driver.find_element_by_xpath("//button[text()='Log in']")
        loginButton.click()

    def post(self, post):
        # click camera btn
        cameraXPath = "//div[contains(@class, 'Camera')]"
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(cameraXPath))
        cameraButton = self.driver.find_element_by_xpath(cameraXPath)
        cameraButton.click()

        sleep(randint(1, 3))

        # go to images folder
        sleep(0.25)
        pyautogui.typewrite(IMAGE_PATH)
        sleep(0.25)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        # select file in browser
        sleep(0.25)
        pyautogui.typewrite(post.image)
        sleep(0.25)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        sleep(randint(1, 3))

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

        sleep(randint(1, 3))

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

        sleep(randint(1, 3))

        # share file
        shareXPath = "//button[text()='Share']"
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(shareXPath))
        shareButton = self.driver.find_element_by_xpath(shareXPath)
        shareButton.click()

        self.commentPost(post)

        print('Successfully posted: ' + post.title)

    def commentPost(self, post):
        # go to Profile
        profileXPath = "//div[contains(@class, 'Profile')]"
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(profileXPath))
        profileButton = self.driver.find_element_by_xpath(profileXPath)
        profileButton.click()

        sleep(randint(1, 3))

        # get most recent post
        mostRecentPostXPath = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div[1]/div[1]/a/div/div[2]'
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(mostRecentPostXPath))
        postsElement = self.driver.find_element_by_xpath(mostRecentPostXPath)
        postsElement.click()

        sleep(randint(1, 3))

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