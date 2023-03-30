from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time


driver = webdriver.Chrome()
driver.get('https://store.steampowered.com/charts/topselling/RU')
time.sleep(5)
dates = driver.find_element(By.CLASS_NAME, "steamchartsshell_Weekly_jC5Vq")
new_date = dates.find_elements(By.TAG_NAME, "a")
new_date[0].click()
#new_date.click()
time.sleep(1)
subprocess.call('TASKKILL /F /IM chrome.exe', shell=True)


print(new_date)


##  id="steam_charts_root_content"

