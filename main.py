#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import argparse

parser = argparse.ArgumentParser()
#cli arguments: -u USERNAME -p PASSWORD
parser.add_argument("-u", "--username",dest ="username", help="User name")
parser.add_argument("-p", "--password",dest = "password", help="Password")
args = parser.parse_args()

OrionURL = 'https://dacs-prd.utshare.utsystem.edu/psp/DACSPRD/?cmd=start'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
ser = Service("chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=chrome_options)

#webscraping test:
#soup = BeautifulSoup(driver.page_source, 'html.parser')
#results = soup.find_all('input')
#print(results)

#access login page
driver.get(OrionURL)

#login
username = driver.find_element(By.ID, 'netid')
username.send_keys(args.username)
password = driver.find_element(By.ID, 'password')
password.send_keys(args.password)

form = driver.find_element(By.ID, 'submit')
form.click()

