# TC010 - Global feed is filled with data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import csv
import pprint
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 500, 500)

# Enter the data to be uploaded
email = 'testuser1@example.com'
username = 'testuser1'
pwd = 'Abcd123$'

# Fields xpath
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
pwd_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
username_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
sign_button_x = '//*[@id="app"]/nav/div/ul/li[2]/a'
sign_in_btn_x = '//*[@id="app"]/div/div/div/div/form/button'
pagination_x = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/nav/ul'
article_preview = '//*[@class="article-preview"]'
page_btn = '//*[@class="page-link"]'

def find(xpath):
    find = driver.find_element_by_xpath(xpath)
    return find

extracted_date = []

try:
    # Load page
    URL = driver.get("http://localhost:1667/")
    time.sleep(3)

    # Driver find
    def find(xpath):
        find = driver.find_element_by_xpath(xpath)
        return find

    # Sign in
    def sign_in(email, pwd):
        sign_button = find(sign_button_x)
        sign_button.click()
        find(email_x).send_keys(email)
        find(pwd_x).send_keys(pwd)
        sign_in_btn = find(sign_in_btn_x)
        sign_in_btn.click()
        time.sleep(2)

    sign_in(email, pwd)
    time.sleep(2)

    # Global feed
    pages = driver.find_elements_by_class_name('page-link')
    for p in range(len(pages)):
        pages[p].click()
        time.sleep(1)
        articles = driver.find_elements_by_xpath('//div[@class="article-preview"]')
        print(f"{p + 1}. oldal bejegyzései: {len(articles)} db")
        time.sleep(1)
        for a in articles:
            # data_row = {}
            title = a.find_element_by_tag_name('h1').text
            date = a.find_element_by_class_name('date').text
            print(title, date)

finally:
    pass
    # driver.close()