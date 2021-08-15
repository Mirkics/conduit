# Blog bejegyzés módosítása
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False


def test_blog_change():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
    driver.set_window_size(1000, 600, 600)

    try:
        # Oldal betöltése
        driver.get("http://localhost:1667/")
        time.sleep(3)

        # Feltöltendő adatok megadása
        email = 'testuser2@example.com'
        pwd = 'Abcd123$'

        # Post mezők xpath
        title_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
        about_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
        write_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
        tags_xp = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'

        # Teszt adatok
        title_2 = 'Blog mod'
        about_2 = 'Blog'
        write_2 = 'Ez nem mese'
        tags_2 = 'Rémálom'

        # Driver find

        def find(xpath):

            find = driver.find_element_by_xpath(xpath)
            return find

        # Sign in
        def sign_in(email, pwd):
            sign_button = find('//*[@id="app"]/nav/div/ul/li[2]/a')
            sign_button.click()
            find('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(email)
            find('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys(pwd)
            sign_in_btn = find('//*[@id="app"]/div/div/div/div/form/button')
            sign_in_btn.click()
            time.sleep(2)

        sign_in(email, pwd)
        time.sleep(3)

        # Find one of my post
        find('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)

        # Post modification
        def edit():
            find('//*[@id="app"]/nav/div/ul/li[4]/a').click()  # username click
            time.sleep(2)
            find('//*[@id="app"]/div/div[2]/div/div/div[1]/ul/li[1]/a').click()  # my title click
            time.sleep(2)
            find('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a/h1').click()  # post title click
            time.sleep(2)
            find('//*[@id="app"]/div/div[1]/div/div/span/a').click()  # edit article button click
            time.sleep(2)
            find(title_xp).clear()
            find(title_xp).send_keys(title_2)
            find(about_xp).clear()
            find(about_xp).send_keys(about_2)
            find(write_xp).clear()
            find(write_xp).send_keys(write_2)
            tags_btn = find('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li[1]/div[2]/i[2]')
            tags_btn.click()
            find(tags_xp).send_keys(tags_2)
            publish_btn = find('//*[@id="app"]/div/div/div/div/form/button')
            publish_btn.click()

        edit()
        print(edit)
        time.sleep(2)

        # Controll
        assert (title_2 in find('//*[@id="app"]/div/div[1]/div/h1').text)
        assert (write_2 in find('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/p').text)
        assert (tags_2 in find('//*[@id="app"]/div/div[2]/div[1]/div/div[2]').text)
        print(title_2, write_2, tags_2)

    finally:
        driver.close()
