from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from settings import *


driver = webdriver.Firefox()
driver.delete_all_cookies()
url = 'https://login.taobao.com/'
driver.get(url)
input = driver.find_element_by_xpath('//i[@id="J_Quick2Static"]')
ActionChains(driver).move_to_element(input).perform()
input.click()
time.sleep(2)

username = driver.find_element_by_xpath('//input[@id="TPL_username_1"]')
password = driver.find_element_by_xpath('//input[@id="TPL_password_1"]')
login_button = driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]')
check = driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')

ActionChains(driver).move_to_element(username).perform()
time.sleep(2)
username.send_keys(USERNAME)
time.sleep(2)

ActionChains(driver).move_to_element(password).perform()
time.sleep(2)
password.send_keys(PASSWORD)
time.sleep(2)

try:
    ActionChains(driver).move_to_element(check).perform()
    time.sleep(1)
    ActionChains(driver).click_and_hold(check).perform()
    time.sleep(0.8)
    ActionChains(driver).move_by_offset(298,0).release().perform()
    time.sleep(1)
    ActionChains(driver).move_to_element(login_button).perform()
    time.sleep(1)
    login_button.click()
    time.sleep(2)
    driver.refresh()
    Cookie = ''
    for cookie in driver.get_cookies():
        Cookie = Cookie + cookie.get('name') + ':' + cookie.get('value') +';'
    print(Cookie[:-1])
except:
    pass
