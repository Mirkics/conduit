# TC008 - Saját blog bejegyzés törlése

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


opt = Options()
opt.headless = False


def test_delete_blog():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    #driver.set_window_size(1000, 600, 600)

    try:
        # Oldal betöltése
        driver.get("http://localhost:1667/")
        time.sleep(3)

        # Sign in process

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

        # Find a posts
        post_list = []
        posts = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]')
        post_list = [len(posts)]

        def delete_post(post1):

            username = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
            username.click()  # click the username on menu

            # Post mező xpath
            article = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1')
            article.click()
            del_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/button/span')
            del_btn.click()
            time.sleep(2)

            delete_post(post1)

        posts = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]')
        post_list2 = [len(posts)]

        assert len(post_list) != post_list2

    finally:
        driver.close()
