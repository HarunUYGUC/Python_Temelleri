from selenium import webdriver
from userinfo import username, password
import time

class Github:
    chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_driver_path)
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password

    def __del__(self):
        time.sleep(4)
        self.browser.close()


app = Github()

# app.signIn()
# app.getFollowers()
# app.findRepositories('python')