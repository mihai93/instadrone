# encoding=utf8  
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
# usernameField.send_keys('boutiquecannabiscanada')
# usernameField.send_keys(u"\uD840\uDC00")

text = u"😀😁'😂'😇😺"
text = text.replace("'", "\\'")  # escape single quotes
text = text.encode('utf-8')  # needed to make format function work

driver.execute_script(
    "arguments[0].value = '{data}'".format(
    	data=text
    ), usernameField)
