#!/usr/bin/python
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import os
import logging

logger = logging.getLogger('MyWebDriver')

class MyWebDriver:
    def __init__(self, browser_name, server_info = "../../Driver/"):
        self.browser_name = browser_name
        self.server_info = server_info
        # Initialize FireFox Web Driver
        if browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox()
        
        # Initialize Chrome Web Driver
        elif browser_name.lower() == "chrome":
            chrome_driver = server_info + "chromedriver"
            os.environ["webdriver.chrome.driver"] = chrome_driver
            self.driver = webdriver.Chrome(chrome_driver)
        
        # Initialize Safari Web Driver
        elif browser_name.lower() == "safari":
            self.driver = webdriver.Safari(server_info + "safari")
        
        # Initialize IE Web Driver
        else:
            self.driver = webdriver.Ie(server_info + "iedriverserver.exe");
        self.driver.maximize_window();
    
    def navigate_to_url(self, url):
        self.driver.get(url)
    
    def set_implicite_wait(self, time_out):
        self.implicit_wait = time_out
        self.driver.implicitly_wait(self.implicit_wait)
    
    def create_explicit_wait(self, time_out):
        self.explicit_wait = time_out
        self.wait = ui.WebDriverWait(self.driver, self.explicit_wait)
    
    def maximize_browser(self):
        self.driver.maximize_window();

if __name__ == "__main__":
    driver = MyWebDriver("IE")
    driver.driver.get("https://tinhte.vn")