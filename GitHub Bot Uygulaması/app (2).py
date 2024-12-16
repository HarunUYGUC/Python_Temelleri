from selenium import webdriver
from userinfo import username, password
from selenium.webdriver.common.keys import Keys
import time

class Github:
    chrome_driver_path = "/Users/sadikturan/Drivers/chromedriver"

    def __init__(self):
        self.browser = webdriver.Chrome(Github.chrome_driver_path)
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get(self.baseUrl + "login")
        self.browser.find_element_by_name("login").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password)
        self.browser.find_element_by_name("commit").click()

    def findRepositories(self,keyword):
        self.browser.get(self.baseUrl)
        searchInput = self.browser.find_element_by_name('q')
        searchInput.send_keys(keyword)
        searchInput.send_keys(Keys.ENTER)

        # print(self.browser.page_source)

        repos = self.browser.find_elements_by_css_selector('.repo-list-item')

        for repo in repos:
            anchor = repo.find_elements_by_tag_name('a')[0]
            paragraf = repo.find_elements_by_tag_name('p')[0]
            repoName = anchor.text
            repoLink = anchor.get_attribute('href')
            description = paragraf.text

            r = {
                "name": repoName,
                "link": repoLink,
                "description": description
            }

            print(r)

    def __del__(self):
        time.sleep(4)
        self.browser.close()


app = Github()

# app.signIn()
# app.getFollowers()
app.findRepositories('python')