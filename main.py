import time
from selenium import webdriver
from selenium_stealth import stealth

xpath_ETU = '/html/body/div/div/div[2]/div/div/div[2]/p/div/button'
xpath_login = '/html/body/div/div[1]/div/div[2]/div/form/div[1]/div/div/input'
xpath_password = '/html/body/div/div[1]/div/div[2]/div/form/div[2]/div/div/input'
xpath_IN = '/html/body/div/div[1]/div/div[2]/div/form/div[4]/div[2]/div/button'
xpath_authorization = '/html/body/div/div[1]/div/div[2]/div/div[4]/div/div[2]/form/button'
xpath_mark = '/html/body/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/button'

login = 'mrpavel23ooo@mail.ru'
password = 'v234praw'

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/117.0.5938.92 Safari/537.36')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)

stealth(browser, languages=['en-US', 'en'], vendor='Google Inc.', platform='Win32', webgl_vendor='Intel Inc.',
        renderer='Intel Iris OpenGl Engine', fix_hairline=True)

browser.get('https://digital.etu.ru/attendance/auth')
time.sleep(5)
browser.find_element('xpath', xpath_ETU).click()
browser.find_element('xpath', xpath_login).send_keys(login)
browser.find_element('xpath', xpath_password).send_keys(password)
time.sleep(3)
browser.find_element('xpath', xpath_IN).click()
time.sleep(5)
browser.find_element('xpath', xpath_authorization).click()
time.sleep(5)
try:
    browser.find_element('xpath', xpath_mark).click()
    time.sleep(3)
    browser.save_screenshot('mark.png')
except:
    print('failed')


browser.quit()


