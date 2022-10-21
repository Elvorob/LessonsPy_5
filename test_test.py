import time
from webbrowser import BaseBrowser
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://suninjuly.github.io/cats.html')
time.sleep(5)

a = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]').click()
time.sleep(5)

b = driver.find_element(By.XPATH,'//p[text()="Bullet cat"]').text
assert b == "Bullet catt", "wrong"
time.sleep(5)