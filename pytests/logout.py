# TC002 - User log out
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

def test_sign_in():

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

    # login adatok
    email = 'testuser2@example.com'
    pwd = 'Abcd123$'


    try:
        #def test_sign_in(email, pwd):
        driver.get("http://localhost:1667/#/")
        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()  # menu sign in button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(pwd)
        sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        sign_in_btn.click()
        time.sleep(5)

        assert driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == 'testuser2'
        #assert driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').is_enabled()
        # assert sign_in_btn.is_disabled()

        #def test_logout():
        logout_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a/i')
        assert logout_btn.is_enabled()
        logout_btn.click()
        time.sleep(3)

        sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        assert sign_in_btn.is_enabled()

        time.sleep(2)
        # test_sign_in('testuser2@example.com', 'Abcd123$')
        # time.sleep(5)
        # test_logout()
        # time.sleep(3)

    finally:
        driver.close()
