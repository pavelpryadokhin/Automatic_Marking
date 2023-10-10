import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

xpath_ETU = '/html/body/div/div/div[2]/div/div/div[2]/p/div/button'
xpath_login = '/html/body/div/div[1]/div/div[2]/div/form/div[1]/div/div/input'
xpath_password = '/html/body/div/div[1]/div/div[2]/div/form/div[2]/div/div/input'
xpath_IN = '/html/body/div/div[1]/div/div[2]/div/form/div[4]/div[2]/div/button'
xpath_authorization = '/html/body/div/div[1]/div/div[2]/div/div[4]/div/div[2]/form/button'
# xpath_mark = '/html/body/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div'
xpath_mark = '/html/body/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/button'

def located(browser, xpath):
    return WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))


def mark_etu(login, password):
    service = Service(executable_path='/usr/sbin/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/117.0.5938.92 Safari/537.36')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    browser = webdriver.Chrome(service=service, options=options)

    stealth(browser, languages=['en-US', 'en'], vendor='Google Inc.', platform='Win32', webgl_vendor='Intel Inc.',
            renderer='Intel Iris OpenGl Engine', fix_hairline=True)
    flag = True
    try:
        browser.get('https://digital.etu.ru/attendance/auth')
        located(browser, xpath_ETU).click()
        browser.find_element('xpath', xpath_login).send_keys(login)
        browser.find_element('xpath', xpath_password).send_keys(password)
        located(browser, xpath_IN).click()
        located(browser, xpath_authorization).click()
        browser.find_element('xpath', xpath_authorization).click()
        located(browser, xpath_mark).click()
        browser.save_screenshot('mark.png')
    except Exception:
        flag = False
    finally:
        browser.quit()
    return flag
