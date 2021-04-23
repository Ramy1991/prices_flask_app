from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from lxml import html
import os
import time
from datetime import datetime
import mouse


# left click

mouse.move(-200, 200, absolute=False, duration=0.2)
mouse.click('left')


executable_path = r'C:\Users\ramyg\Downloads\chromedriver_win32 (1)\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = executable_path
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
driver.get('http://shops.syaanh.com/login')

driver.find_element_by_xpath('//*[@id="email"]').send_keys('ramy.zaghloul@mzadqatar.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('BDZuKtqUwaL2b3fd')
driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div/div[2]/form/div[4]/div/button').click()

time.sleep(3)

# driver.switch_to.window(driver.window_handles[0])
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://ebdaadt.atlassian.net/browse/CON-109')
driver.find_element_by_xpath('//*[@id="username"]').send_keys('ramy.zaghloul@mzadqatar.com')
driver.find_element_by_xpath('//*[@id="login-submit"]/span/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]').send_keys('RAmy@@1991')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-submit"]/span/span').click()
time.sleep(3)

# driver.get(
#     'https://aid-frontend.prod.atl-paas.net/atlassian-id/front-end/5.0.224')

driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get('https://ebdaadt.slack.com/')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="email"]').send_keys('ramy.zaghloul@mzadqatar.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Pass@@1991')
driver.find_element_by_xpath('//*[@id="signin_btn"]').click()
time.sleep(3)
link = driver.find_element_by_xpath('//*[@id="page_contents"]/div/div/div[2]/p/a').get_attribute('href')
driver.get(link)

driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get(
    'https://mzad.awsapps.com/auth/?client_id=6b9615ec01be1c8d&redirect_uri=https%3A%2F%2Fwebmail.mail.us-east-1.awsapps.com%2Fworkmail%2F')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="wdc_username"]').send_keys('ramy.zaghloul')
driver.find_element_by_xpath('//*[@id="wdc_password"]').send_keys('Pass@@1991')
driver.find_element_by_xpath('//*[@id="wdc_login_button"]').click()

tab = ['tab2', 'tab3', 'tab4']
while True:
    mouse.move(-200, 200, absolute=False, duration=0.2)
    mouse.click('left')
    time.sleep(9)
    driver.switch_to.window("tab2")
    mouse.move(200, -200, absolute=False, duration=0.2)
    mouse.click('left')
    time.sleep(6)
    driver.switch_to.window("tab3")
    mouse.move(-200, 200, absolute=False, duration=0.2)
    mouse.click('left')
    time.sleep(5)
    driver.switch_to.window("tab4")
    time.sleep(10)
    mouse.move(200, -200, absolute=False, duration=0.2)
    mouse.click('left')
    driver.switch_to.window(driver.window_handles[0])
