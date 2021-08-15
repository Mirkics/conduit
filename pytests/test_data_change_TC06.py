# Meglévő adat módosítása

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = True


def test_data_change():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    # driver.set_window_size(1000, 600, 600)

    try:
        # Oldal betöltése
        driver.get("http://localhost:1667/")
        time.sleep(3)

        def sign_in(email, pwd):
            # user login teszt adatok
            login_data = ['testuser2@example.com', 'Abcd123$', 'testuser2']

            # User fields
            email_f = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
            pwd_f = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')

            # Buttons find
            sign_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
            sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

            sign_btn.click()
            email_f.send_keys(login_data[0])
            pwd_f.send_keys(login_data[1])
            sign_in_btn.click()
            time.sleep(2)

            sign_in(email, pwd)
            time.sleep(5)

            assert driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a') == login_data[2]

        # user_name = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').get_attribute('value')

        def change_data(bio):

            bio_data = 'I like ice-cream'
            settings = driver.find_element_by_xpath("//a[@href='#/settings']")
            settings.click()  # click the settings
            time.sleep(1)

            driver.find_element_by_xpath("// textarea").clear()  # clear text data

            driver.find_element_by_xpath("// textarea").send_keys(bio_data)
            driver.find_element_by_xpath("//button").click()    # update settings button click

            driver.find_element_by_xpath("//div[contains(text(),'Update successful!')]")
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            time.sleep(1)

            change_data(bio)

            assert driver.find_element_by_xpath("//textarea").get_attribute("value") == bio_data

            user_name = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
            user_name.click()
            user_head_text = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/p,')

            assert user_head_text == bio_data

    finally:
        driver.close()
