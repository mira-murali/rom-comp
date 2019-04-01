from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException,NoSuchWindowException
import requests, time, random, sys
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options  

def start_chrome_browser():
	chrome_options = Options()  
	#chrome_options.add_argument("--headless") 
	chrome_options.add_argument("--start-maximized")
	driver = webdriver.Chrome('/home/loki/Downloads/chromedriver_linux64/chromedriver',   chrome_options=chrome_options)
	return driver

def find_all_links(driver):
	full_files = driver.find_elements_by_partial_link_text(".full.npz")
	all_files = driver.find_elements_by_partial_link_text(".npz")
	files_to_be_downloaded = [file for file in all_files if file not in full_files]
	return files_to_be_downloaded

driver = start_chrome_browser()
driver.get("https://console.cloud.google.com/storage/browser/quickdraw_dataset/sketchrnn")
time.sleep(15)

files_to_be_downloaded = find_all_links(driver)
downloaded = []
while len(downloaded)!=len(files_to_be_downloaded):
	for file in files_to_be_downloaded:
		if file not in downloaded:
			file.click()
			time.sleep(10)
			downloaded.append(file)
	files_to_be_downloaded = find_all_links(driver)
