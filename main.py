import time
from mobilebrowser import MobileBrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui

mobileBrowser = MobileBrowser()

mobileBrowser.setUp()

driver = mobileBrowser.getDriver()

driver.get('https://www.instagram.com')

loginButton = driver.find_element_by_link_text('Log in')
loginButton.click()

usernameField = driver.find_element_by_xpath("//input[@name='username']")
usernameField.send_keys('charleyjest1')

passwordField = driver.find_element_by_xpath("//input[@name='password']")
passwordField.send_keys('test123')

loginButton = driver.find_element_by_xpath("//button[text()='Log in']")
loginButton.click()

time.sleep(5)

cameraButton = driver.find_element_by_xpath("//div[contains(@class, 'Camera')]")
cameraButton.click()

time.sleep(1)

pyautogui.press('enter')

time.sleep(3)

nextButton = driver.find_element_by_xpath("//button[text()='Next']")
nextButton.click()

time.sleep(2)

textArea = driver.find_element_by_xpath('//textarea[contains(@placeholder, "Write a caption")]')
textArea.send_keys('test caption')

shareButton = driver.find_element_by_xpath("//button[text()='Share']")
shareButton.click()

# wait = WebDriverWait(driver, 10).until(EC.alert_is_present())

# alert = driver.switchTo().alert()
# alert.accept()

# # fileName = "/Users/mihai.listov/Desktop/ig_pics/winner-08-10-2017.jpg"
# # alert.send_keys(fileName);

# # mobileBrowser.tearDown()
