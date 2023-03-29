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
time.sleep(10)
new_date = driver.find_element(By.CLASS_NAME, "steamchartsshell_MenuGroup_2X7eT steamchartsshell_Weekly_jC5Vq")
for i in new_date:
    print(i)
new_date.click()
time.sleep(10)
subprocess.call('TASKKILL /F /IM chrome.exe', shell=True)


print(new_date)


##  id="steam_charts_root_content"

