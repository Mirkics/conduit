# Adat listázás
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = True


def test_logout():

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

        def data_list():

            article_title = driver.find_elements_by_xpath("//h1")
            titles_of_articles = []
            for i in article_title:
                titles_of_articles.append(i.text)
            assert len(titles_of_articles) == len(article_title)
            # print(titles_of_articles)

        data_list()
        time.sleep(3)

    finally:
        driver.close()
