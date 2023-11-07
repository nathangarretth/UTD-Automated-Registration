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
from datetime import date, datetime

parser = argparse.ArgumentParser()
#cli arguments: -u USERNAME -p PASSWORD
parser.add_argument("-u", "--username",dest ="username", default = None, help="User name")
parser.add_argument("-p", "--password",dest = "password", default = None, help="Password")
parser.add_argument("-f", "--firefox",dest = "firefox", default = None, help="Firefox")
parser.add_argument("-ho", "--hour",dest = "hour", default = None, help="Hour")
parser.add_argument("-m", "--minute",dest = "minute", default = None, help="Minute")
args = parser.parse_args()

OrionURL = 'https://dacs-prd.utshare.utsystem.edu/psp/DACSPRD/?cmd=start'

if(args.firefox):
    driver = webdriver.Firefox()
else:
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

#wait until duo auth
wait = WebDriverWait(driver, 30).until(EC.url_matches('dacs-prd'))

#Navigate to Schedule Planner

#Homepage nav
time.sleep(8)
driver.find_element(By.ID, 'HOMEPAGE_SELECTOR$PIMG').click()
time.sleep(8)
#Student center
driver.find_element(By.XPATH, "//*[contains(text(), 'UTD Student Center')]").click()
time.sleep(4)
#Navigate to manage classes
manageClasses = driver.find_element(By.XPATH, "//*[text()='Manage My Classes']")
#print(manageClasses.get_attribute('innerHTML'))
print(manageClasses)
manageClasses.click()
time.sleep(5)
#Go to Schedule Planner
driver.find_element(By.XPATH, "//*[text()='Scheduler Planner']").click()
#driver.find_element(By.ID, 'win6divPTGP_STEP_DVW_PTGP_STEP_BTN_GB$2').click()
#schedulerPlanner = driver.find_element(By.XPATH, "//*[contains(text(), 'Scheduler Planner')]")
#schedulerPlanner = driver.find_element(By.XPATH, "//button[.//span[text()='Scheduler Planner']]")
time.sleep(2)
#Access Schedule Planner page
driver.find_element(By.ID, 'PRJCS_DERIVED_PRJCS_LAUNCH_CS').click()
time.sleep(10)
#switch to new window and refresh
Windows = driver.window_handles
driver.switch_to.window(Windows[1])

#define register
def register():
    driver.find_element(By.XPATH, "//*[text()='Shopping Cart']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[text()='Register']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[text()='Continue']").click()
    time.sleep(4)


while True:
    time.sleep(45)
    currTime = datetime.now()
    print('hour ' + str(currTime.hour) + ' minute ' + str(currTime.minute))
    if(currTime.hour == int(args.hour)):
        print('niceee')
        if(currTime.minute > int(args.minute)):
            print('registeringggg!')
            register()
            break
    time.sleep(7)
    

