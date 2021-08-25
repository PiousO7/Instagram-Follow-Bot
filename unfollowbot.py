from selenium import webdriver
import os
from dotenv import load_dotenv
import time

load_dotenv()


class UnfollowBot:
    def __init__(self):

        self.chrome_driver_path = "E:\Softwares\Chrome Driver (python prject)/chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.driver.get("https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav")

        time.sleep(3)
        self.username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.username.send_keys(os.getenv("USER_ID"))

        self.password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password_input.send_keys(os.getenv("PASSWORD"))

        self.login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        self.login_button.click()

        time.sleep(3)
        self.instagram_logo = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img')
        self.instagram_logo.click()
        time.sleep(3)
        try:
            not_now = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            not_now.click()
        finally:
            time.sleep(3)
            username = self.driver.find_element_by_link_text(os.getenv("USER_ID"))
            username.click()

            time.sleep(2)
            following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
            following.click()

            time.sleep(1)
            keep_following = True
            while keep_following:
                follow_button = self.driver.find_elements_by_css_selector("li button")
                time.sleep(1)
                for i in follow_button:
                    time.sleep(1)
                    index = follow_button.index(i)
                    if index in range(0, 3):
                        pass
                    else:
                        if index % 8 == 0:
                            time.sleep(2)
                            scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div')
                            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                            time.sleep(2)
                        i.click()
                        time.sleep(1)
                        unfollow_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[1]')
                        time.sleep(1)
                        unfollow_button.click()
                        keep_following = False

