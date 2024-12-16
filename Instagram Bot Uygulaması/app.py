from selenium import webdriver
from userInfo import username, password
from selenium.webdriver.common.keys import Keys
import time

class Instagram:

    driver_path = "/Users/sadikturan/Drivers/chromedriver"
    # driver_path = "C:\Driver\chromedriver"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.driver_path)

    def signIn(self):
        pass

    def getFollowers(self):
        pass

    def followUser(self, username):
        pass

    def unFollowUser(self, username):
        pass

    def __del__(self):
        time.sleep(10)
        self.browser.close()

app = Instagram(username, password)

app.signIn()
app.getFollowers()
app.followUser('abc')
app.unFollowUser('abc')