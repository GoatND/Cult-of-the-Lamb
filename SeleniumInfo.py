#Imports
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Initial Selenium
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') 
options.add_argument('--ignore-ssl-errors')
options.add_argument('headless')
options.add_argument('disable-gpu')
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=options)
browser.maximize_window()

