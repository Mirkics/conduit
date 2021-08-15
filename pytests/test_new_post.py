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

    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # login datas
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # User fields
    email_f = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    username_f = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    pwd_f = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')

    # Buttons find
    sign_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    sign_in_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    new_art_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    publ_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    home_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a')


    # Sign in

    def sign_in(email, pwd):

        sign_btn.click()
        email_f.send_keys(email)
        pwd_f.send_keys(pwd)
        sign_in_btn.click()
        time.sleep(2)

    sign_in(email, pwd)
    time.sleep(5)

    assert username == username_f.text
    print(username)
    time.sleep(2)

    try:
        def create_post(row):

            new_art_btn.click()
            print(row)

            with open('posts.csv') as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader)
                for row in csvreader:
                    title_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
                    title_field.send_keys(row[0])
                    about_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
                    about_field.send_keys(row[1])
                    write_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]'
                                                       '/textarea')
                    write_field.send_keys(row[2])
                    tags_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]'
                                                      '/div/div/ul/li/input')
                    tags_field.send_keys(row[3])

            publ_btn.click()
            driver.back()

        # def check_post(row):
        #     home_btn.click()  # Home button click
        #     post_f = driver.find_element_by_xpath('//div[@class="info"]/a').text
        #     post_f.send_keys(row[0])
        #     print(row[0])
        #     driver.back()

            create_post(row)
            #check_post(row)

        assert driver.find_element_by_xpath('//button/span').text == ' Delete Article'
        assert driver.find_element_by_xpath('//form/div/textarea[@placeholder="Write a comment..."]')

        # assert '//div[@class="info"]/a' == row[0]
        time.sleep(2)

    finally:
        pass
        driver.close()
