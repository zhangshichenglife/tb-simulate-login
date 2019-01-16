from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from mlogin_param import *
from settings import *


url = 'https://h5.m.taobao.com/?'
dcap = dict(DesiredCapabilities.FIREFOX)
dcap['firefox.page.settings.userAgent'] = 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/29.0 Firefox/29.0'
driver = webdriver.Firefox()
# driver.delete_all_cookies()
driver.get(url)
time.sleep(5)
ele = driver.find_element_by_xpath('//span[@class="tb-toolbar-iconfont tb-toolbar-icon-my"]')
ele.click()
time.sleep(5)
frame = driver.find_element_by_xpath("//iframe[1]")
driver.switch_to.frame(frame)
time.sleep(5)
user = driver.find_element_by_xpath('//input[@id="username"]')
user.send_keys(USERNAME) # input username
time.sleep(5)
pwd = driver.find_element_by_xpath('//input[@id="password"]')
pwd.send_keys(PASSWORD) #input password
time.sleep(5)
login = driver.find_element_by_xpath('//button[@id="btn-submit"]')
login.click()
time.sleep(2)


try:
    dialog = driver.find_element_by_xpath('//div[@class="km-dialog-buttons"]/span')
    dialog.click()
    time.sleep(2)
    # js = "var url = 'https://cf.aliyun.com/nvc/nvcAnalyze.jsonp?a=' + param1 + '&callback=callback';var superagent = require('superagent'); superagent.get(url)"
    # driver.execute_script(js)
    # time.sleep(5)
    checkbut = driver.find_element_by_xpath('//div[@class="sm-ico-wave"]')
    ActionChains(driver).move_to_element(checkbut).perform()
    time.sleep(3)
    checkbut.click()
    pwd1 = driver.find_element_by_xpath('//input[@id="password"]')
    pwd1.send_keys(PASSWORD) # input password
    time.sleep(5)
    login1 = driver.find_element_by_xpath('//button[@id="btn-submit"]')
    login1.click()
    time.sleep(2)
    driver.refresh()
    cookies = driver.get_cookies()
    Cookie = ''
    for cookie in cookies:
        Cookie = Cookie + cookie.get('name') + ':' + cookie.get('value') + ';'
    Cookie = Cookie[:-1]
    print(Cookie)
except:
    pass
