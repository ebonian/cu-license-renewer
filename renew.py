from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService

from datetime import datetime, timedelta

def init_driver() -> webdriver.Chrome:
    chrome_options = Options()
    options = [
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--remote-debugging-port=9222",
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions"
    ]

    for option in options:
        chrome_options.add_argument(option)

    return webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)

def login( driver: webdriver.Chrome, username: str, password: str):
    driver.get('https://licenseportal.it.chula.ac.th/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//input')))

    username_input = driver.find_element(By.ID, 'UserName')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'Password')
    password_input.send_keys(password)

    signin_button = driver.find_element(By.XPATH, '//button')
    signin_button.click()

def logout( driver: webdriver.Chrome):
    driver.get('https://licenseportal.it.chula.ac.th/Auth/Logout')


def borrow( driver: webdriver.Chrome, select_value: str):
    driver.get('https://licenseportal.it.chula.ac.th/Home/Borrow')
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'ExpiryDateStr')))
    
    select_element = driver.find_element(By.ID, 'ProgramLicenseID')
    select = Select(select_element)
    select.select_by_value(select_value)
    
    save_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    save_button.click()