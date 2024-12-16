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
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name('username')
        passwordInput = self.browser.find_element_by_name('password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(4)

        if self.browser.find_element_by_class_name('cmbtv'):
            el = self.browser.find_element_by_class_name('cmbtv')
            el.find_element_by_tag_name('button').click()

        time.sleep(4)

        if self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'):
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_class_name("k9GMp").find_element_by_tag_name("a").click()
        time.sleep(2)
        followers = self.browser.find_element_by_class_name("PZuss").find_elements_by_tag_name("li")
        for user in followers:
            link = user.find_element_by_tag_name("a").get_attribute("href")
            print(link)

    def followUser(self, username):
        pass

    def unFollowUser(self, username):
        pass

    def __del__(self):
        time.sleep(10)
        # self.browser.close()

app = Instagram(username, password)

app.signIn()
app.getFollowers()
app.followUser('abc')
app.unFollowUser('abc')