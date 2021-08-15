# Sign up with not existing username

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


opt = Options()
opt.headless = False


def test_login():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    time.sleep(2)

    try:

        driver.get("http://localhost:1667/")
        time.sleep(3)

        test_user_1 = ["testuser1", "testuser1@example.com", "Abcd123$"]

        def sign_up(user, email, pwd):
            sign_up_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a')

            user_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
            email_addr = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')

            signup_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

            sign_up_btn.click()
            time.sleep(2)
            user_name.send_keys(test_user_1[0])
            email_addr.send.keys(test_user_1[1])
            password.send.keys(test_user_1[2])
            signup_btn.click()
            time.sleep(2)

            sign_up(user, email, pwd)
            time.sleep(3)

            assert driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a') == test_user_1[0]

    finally:
        driver.close()