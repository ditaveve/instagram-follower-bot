from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium import webdriver

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        load_dotenv()

    def login(self):
        self.driver.get(os.getenv("URL"))

        email_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        email_box.click()
        email_box.send_keys(os.getenv("EMAIL"))

        pass_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        pass_box.click()
        pass_box.send_keys(os.getenv("PASSWORD"))

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        save_info_popup = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='naan-popup-dismiss']")))
        save_info_popup.click()

        cookies_popup = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='naan-popup-dismiss']")))
        cookies_popup.click()
        

    def find_followers(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/button")))
        search_button.click()

        make_search = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/aside/div[2]/input")))
        make_search.click()
        make_search.send_keys(os.getenv("SIMILAR_ACCOUNT") + Keys.ENTER)

        followers = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a")))
        followers.click()

    def follow(self):
        pass