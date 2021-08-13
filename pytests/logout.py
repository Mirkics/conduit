# TC002 - User log out
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

try:
    def test_sign_in(email, password):
        driver.get("http://localhost:1667/#/")
        driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input').send_keys(
            'first@gmail.com')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input').send_keys('First12345')
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
        time.sleep(8)

    def test_logout():
        logout_btn = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a/text()')
        logout_btn.click()

    assert text == 'Sign up'
    time.sleep(5)
    test_sign_in('first@gmail.com', 'First12345')
    time.sleep(5)
    test_logout()
    time.sleep(3)

finally:
    driver.close()