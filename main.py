#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import platform
import maskpass
import argparse
import time

parser = argparse.ArgumentParser()
#cli arguments: -u USERNAME -p PASSWORD
parser.add_argument("-u", "--username",dest ="username", default = None, help="User name")
parser.add_argument("-p", "--password",dest = "password", default = None, help="Password")
args = parser.parse_args()

OrionURL = 'https://dacs-prd.utshare.utsystem.edu/psp/DACSPRD/?cmd=start'

chromeDriver = ''
if platform == "linux" or platform == "linux2":
    chromeDriver = 'chromedriver'
elif platform == "win32":
    chromeDriver = 'chromedriver.exe'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
ser = Service(chromeDriver)
driver = webdriver.Chrome(service=ser, options=chrome_options)

#webscraping test:
#soup = BeautifulSoup(driver.page_source, 'html.parser')
#results = soup.find_all('input')
#print(results)

#access login page
driver.get(OrionURL)

#login
username = driver.find_element(By.ID, 'netid')
if(args.username is None):
    newUsername = input('Enter Username: ')
    username.send_keys(newUsername)
else:
    username.send_keys(args.username)

password = driver.find_element(By.ID, 'password')
if(args.password is None):
    newPassword = maskpass.askpass(mask="")
    password.send_keys(newPassword)
else:
    password.send_keys(args.password)

driver.find_element(By.ID, 'submit').click()

wait = WebDriverWait(driver, 30).until(EC.url_matches('dacs-prd'))

#Navigate to Schedule Planner

#Homepage nav
driver.find_element(By.ID, 'HOMEPAGE_SELECTOR$PIMG').click()
#Student center
driver.find_element(By.XPATH, "//*[contains(text(), 'UTD Student Center')]").click()
#Navigate to manage classes
driver.find_element(By.ID, 'win0divPTNUI_LAND_REC_GROUPLET$15').click()
time.sleep(2)
#Go to Schedule Planner
driver.find_element(By.ID, 'win6divPTGP_STEP_DVW_PTGP_STEP_BTN_GB$2').click()
#schedulerPlanner = driver.find_element(By.XPATH, "//*[contains(text(), 'Scheduler Planner')]")
#schedulerPlanner = driver.find_element(By.XPATH, "//button[.//span[text()='Scheduler Planner']]")
time.sleep(2)
#Access Schedule Planner page
driver.find_element(By.ID, 'PRJCS_DERIVED_PRJCS_LAUNCH_CS').click()




