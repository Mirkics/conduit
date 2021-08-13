# TC005 - New blog post
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv


def test_new_post():

    opt = Options()
    opt.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
    driver.set_window_size(1000, 600, 600)

    # Load page
    driver.get("http://localhost:1667/")
    time.sleep(3)

    # login datas
    email = 'testuser1@example.com'
    username = 'testuser1'
    pwd = 'Abcd123$'

    # User xpath
    email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
    username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
    pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'

    # Fields xpath
    title_f = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
    about_f = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
    write_f = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
    tags_f = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
    post_f = '//*[@class="article-preview"]'

    # Button xpath
    sign_btn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    sign_inbtn = '//*[@id="app"]/div/div/div/div/form/button'
    new_artbtn = '//*[@id="app"]/nav/div/ul/li[2]/a'
    publish = '//*[@id="app"]/div/div/div/div/form/button'
    home_btn = '//*[@id="app"]/nav/div/ul/li[1]/a'

    # Driver find
    def find(xpath):

        find = driver.find_element_by_xpath(xpath)
        return find

    # Sign in
    def sign_in(email, pwd):

        sign_button = find(sign_btn)
        sign_button.click()
        find(email_x).send_keys(email)
        find(pwd_x).send_keys(pwd)
        sign_in_btn = find(sign_inbtn)
        sign_in_btn.click()
        time.sleep(2)

    sign_in(email, pwd)
    time.sleep(5)

    assert username == find(username_x).text
    # print(username)
    time.sleep(2)

    try:
        def create_post(row):
            find(new_artbtn).click()
            print(row)
            find(title_f).send_keys(row[0])
            find(about_f).send_keys(row[1])
            find(write_f).send_keys(row[2])
            find(tags_f).send_keys(row[3])
            find(publish).click()
            driver.back()

        def check_post(row):
            find(home_btn).click()  # Home button click
            find(post_f).send_keys(row[0])
            print(row[0])
            driver.back()

        # Add new post
        def new_post():

            with open('../text/post.csv') as csvfile:
                csvreader = csv.reader(csvfile)
                next(csvreader)
                for row in csvreader:
                    create_post(row)
                    check_post(row)

        time.sleep(2)

    finally:
        pass
        driver.close()
