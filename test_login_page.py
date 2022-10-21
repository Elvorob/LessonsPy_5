import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
link = driver.get('https://www.saucedemo.com/')

def test_title():
    title_from_site = driver.title
    assert title_from_site == 'Swag Labs'

def test_login_from():
    # user_name = driver.find_element(By.CSS_SELECTOR, "input#user-name")
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')
    time.sleep(2)

    # password = driver.find_element(By.XPATH, "input[contains(@placeholder, 'password')]")
    password = driver.find_element(By.ID, "password")
    password.send_keys('secret_sauce')
    time.sleep(2)

    # button_login = driver.find_element(By.XPATH, '//input[@name="login-button"]')
    button_login = driver.find_element(By.NAME, 'login-button')
    button_login.click()
    time.sleep(2)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Wrong site!!!'

    driver.quit()


