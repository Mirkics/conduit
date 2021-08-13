from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False


def test_conduit_cookie():

    def test_cookie():
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
        driver.get("http://localhost:1667/#/")
        accept_btn = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
        time.sleep(5)
        assert accept_btn.is_enabled()
        time.sleep(5)
        accept_btn.click()
        time.sleep(3)
        driver.close()

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
        driver.get("http://localhost:1667/#/")
        time.sleep(5)
        btn_list = driver.find_elements_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
        assert len(btn_list) == 0

        driver.quit()
