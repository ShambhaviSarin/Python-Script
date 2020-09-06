#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("https://app.pluralsight.com/)