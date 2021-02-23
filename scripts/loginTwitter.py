from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

loginTarget="https://twitter.com/login"

import scripts.credential as cre

def getLodInDriver():
    driver=webdriver.Chrome("chromedriver.exe")
    driver.get(loginTarget)

    try:
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "session[username_or_email]"))
        )
        email.send_keys(cre.email)
        time.sleep(1)

        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "session[password]"))
        )
        password.send_keys(cre.password)
        time.sleep(1)

        loginBt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//div[@data-testid="LoginForm_Login_Button"]'))
        )
        loginBt.click()
        time.sleep(1)

    except TimeoutException as te:
        print("can't get element")


    print("input")
    return driver

if __name__ == '__main__':
    getLodInDriver()