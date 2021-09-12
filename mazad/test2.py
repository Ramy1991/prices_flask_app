from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from lxml import html
import os
from pywinauto.application import Application as app
from pywinauto import mouse as mouse1, keyboard
import time
from random import randrange

from datetime import datetime
import mouse

# left click


# app.menu_select('menu->Open Dashboard')
# Hubstaff.Hubstaff.menu_select('Open Dashboard')
# mouse.move(-200, 200, absolute=False, duration=0.2)
# mouse.click('left')


executable_path = r'C:\Users\ramyg\Downloads\chromedriver_win32\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = executable_path
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('start-maximized')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

chrome_options.add_experimental_option('useAutomationExtension', False)


# chrome_options.add_argument('headless')

driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path)
driver.get('http://shops.syaanh.com/login')

driver.find_element_by_xpath('//*[@id="email"]').send_keys('ramy.zaghloul@mzadqatar.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('BDZuKtqUwaL2b3fd')
driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div/div[2]/form/div[4]/div/button').click()
driver.get('http://shops.syaanh.com/admin/default/jqadm/search/product?lang=en')

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
driver.get('https://ebdaadt.atlassian.net/browse/CON-21')

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
time.sleep(1)
driver.get('https://app.slack.com/client/T8N1GPQS1/D01T8951LLS')

driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get(
    'https://mzad.awsapps.com/auth/?client_id=6b9615ec01be1c8d&redirect_uri=https%3A%2F%2Fwebmail.mail.us-east-1.awsapps.com%2Fworkmail%2F')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="wdc_username"]').send_keys('ramy.zaghloul')
driver.find_element_by_xpath('//*[@id="wdc_password"]').send_keys('Pass@@1991')
driver.find_element_by_xpath('//*[@id="wdc_login_button"]').click()

driver.execute_script("window.open('about:blank', 'tab5');")
driver.switch_to.window("tab5")

driver.get('https://docs.google.com/spreadsheets/d/1jFuSRtZYkx02XTVOZltnBKtrXGbGAlPHhgBPwMSgs2Y/edit#gid=420486138')
driver.execute_script("window.open('about:blank', 'tab6');")

driver.switch_to.window("tab6")
driver.get('https://docs.google.com/spreadsheets/d/1LTyaf2EtFO08BN8cunbPEgNSfZ-zQJsWQMfnBfEKUII/edit#gid=22035314')
tab = ['tab2', 'tab3', 'tab4', 'tab5', 'tab6']

app = app().start(r"C:\Program Files\Hubstaff\HubstaffClient.exe")

mouse1.click(button='left', coords=(1698, 353))
mouse1.click(button='left', coords=(1772, 150))

print(randrange(3))
while True:
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(60 * 3 + randrange(60 * 9))
    driver.switch_to.window("tab2")
    time.sleep(60 * 4 + randrange(60 * 8))
    driver.switch_to.window("tab3")
    time.sleep(60 * 3 + randrange(60 * 9))
    driver.switch_to.window("tab4")
    time.sleep(60 * 2 + randrange(60 * 10))
    driver.switch_to.window("tab5")
    time.sleep(60 * 4 + randrange(60 * 8))
    driver.switch_to.window("tab6")
    time.sleep(60 * 3 + randrange(60 * 9))

    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # # mouse.click('left')
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(2)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # driver.switch_to.window("tab2")
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # # mouse.click('left')
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(2)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # driver.switch_to.window("tab3")
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # mouse.click('left')
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(2)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # driver.switch_to.window("tab4")
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # # mouse.click('left')
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(2)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # # mouse.click('left')
    # driver.switch_to.window("tab5")
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # mouse.click('left')
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(2)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # # mouse.click('left')
    # driver.switch_to.window("tab6")
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(2)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(100, -100, absolute=False, duration=0.2)
    # time.sleep(1)
    # mouse.move(-100, 100, absolute=False, duration=0.2)
    # mouse.click('left')
    # driver.switch_to.window(driver.window_handles[0])
