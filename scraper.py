from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import time
import re

class Urls:
    def __init__(self) -> None:
        self.driver = None
        pass
    def get_browser(self):
        options = webdriver.firefox.options.Options()
        #options.headless = True
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\hamza\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe", options=options)

    def get_url1(self, url):
        self.driver.get(url)
        res = []
        elements = self.driver.find_elements_by_xpath(".//div[@class= 'content-listing__item']//a")
        for e in elements:
            res.append(e.get_attribute('href'))
        return res

    def get_url2(self, n):
        urls = []
        for i in range(n):
            urls.append(self.get(url))


    def get_urls(self,n):
        for i in range(n):


class Logo_Page:
    def __init__(self) -> None:
        pass
