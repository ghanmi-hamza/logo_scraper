from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import Base_URL

class Urls:
    def __init__(self) -> None:
        self.driver = None
        pass
    def get_browser(self):
        options = webdriver.firefox.options.Options()
        #options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\hamza\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe", options=options)

    def get_url_from_page(self, url):
        self.driver.get(url)
        res = []
        elements = self.driver.find_elements_by_xpath(".//a[@class= 'listing-details__title__link']")
        for e in elements:
            res.append(e.get_attribute('href'))
        return res

    def get_urls(self, n):
        urls = []
        for i in range(1, n+1):
            urls.append(self.get_url_from_page(Base_URL.format(i)))
        return urls



"""class Logo_Page:
    def __init__(self) -> None:
        pass"""
