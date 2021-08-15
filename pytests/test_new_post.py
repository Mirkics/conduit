# New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv

opt = Options()
opt.headless = True


def test_new_posts():

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    # driver.set_window_size(1000, 600, 600)
    try:
        # Oldal betöltése
        driver.get("http://localhost:1667/")
        time.sleep(3)

        # Sign in process

        def sign_in(email, pwd):

            # user login teszt adatok
            login_data = ['testuser1@example.com', 'Abcd123$', 'testuser1']

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

        def new_post(title, about, text, tag):
            driver.find_element_by_xpath("//a[@href='#/editor']").click()
            time.sleep(5)
            driver.find_element_by_xpath("//input[@placeholder='Article Title']").send_keys(title)
            driver.find_element_by_xpath("//input[starts-with(@placeholder,'What')]").send_keys(about)
            driver.find_element_by_xpath("//textarea[starts-with(@placeholder,'Write')]").send_keys(text)
            driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys(tag)
            time.sleep(5)
            driver.find_element_by_xpath("//button[@class='btn btn-lg pull-xs-right btn-primary']").click()
            time.sleep(5)

            with open('posts.csv') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',')
                next(csvreader)
                for row in csvreader:
                    print(row)
                    new_post(row[0], row[1], row[2], row[3])

    finally:
        driver.close()
