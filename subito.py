from email.mime import image
from importlib.resources import path
from msvcrt import getwch
from numpy import delete
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests
import time
import wget
import os
import os
import csv
import random as rd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui
chrome_options = webdriver.ChromeOptions()
df = pd.read_excel (r'sincronizzati.xlsx')
proxies = {
   'http': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
   'https': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
}
proxy_url = "https:176.120.193.111:55443"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_url,
    'sslProxy': proxy_url,
    'noProxy': ''})
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
options = Options()
options.add_argument("start-maximized")
# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service()
driver = webdriver.Chrome(desired_capabilities=capabilities,options=chrome_options)
def login(username,password):
    email = driver.find_element(By.ID,"username")
    email.send_keys(username)
    password1 = driver.find_element(By.ID,'password')
    password1.send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[contains(@class,'LoginForm_input-wrapper-but')]/button[@type='submit']").click()
def image_download(url):
    URL = url
    picture_req = requests.get(URL)       
    if picture_req.status_code == 200:
        with open("image.jpg", 'wb') as f:
            f.write(picture_req.content)
def delete_image(image_no):
    image_no = image_no
    driver.find_element(By.XPATH,'//div[@id="fileList"]/descendant::div[@class="remove"][{}]' .format(image_no)).click()
def placeadd():
    for i in range(len(df)):
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='index-module_button-add__uLc1X']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//img[@alt="Motori"]/parent::div').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//p[text()="Accessori auto"]/parent::div').click()
        driver.implicitly_wait(10)
    #selection condition item
        condition = Select(driver.find_element(By.NAME,'item_condition'))
        condition.select_by_index(df['condizione'][i])
        driver.implicitly_wait(10)
        # select images
        try:
            path = os.getcwd()
            path = path.replace("\\","/")
            image_download(df['imm1'][i])
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys('{}/image.jpg' .format(path))
            time.sleep(2)
            image_download(df['imm2'][i])
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys('{}/image.jpg' .format(path))
            delete_image(3)
            driver.implicitly_wait(10)
            image_download(df['imm3'][i])
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys('{}/image.jpg' .format(path))
            delete_image(5)
            driver.implicitly_wait(10)
            delete_image(4)
            driver.implicitly_wait(10)
            image_download(df['imm4'][i])
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys('{}/image.jpg' .format(path))
            delete_image(6)
            driver.implicitly_wait(10)
            delete_image(5)
            driver.implicitly_wait(10)
            image_download(df['imm5'][i])
            driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys('{}/image.jpg' .format(path))
            delete_image(6)
            driver.implicitly_wait(10)
        except:
            pass
    #sending title
        title = driver.find_element(By.ID,'subject')
        title.send_keys(df['titolo'][i])
    # sending text
        text = driver.find_element(By.ID,'body')
        text.send_keys(df['descrizione'][i])
        time.sleep(2)
    # adding price
        price = driver.find_element(By.ID,'price')
        price.send_keys(str(df['prezzo_vendita'][i]))
    #adding common
        common = driver.find_element(By.ID,'town')
        try:
            common.clear()
        except:
            pass
        common.send_keys(df['luogo'][i])
    # adding address
        
        address = driver.find_element(By.ID,'address')
        address.send_keys(df['luogo'][i])
        
    # Phone number

        phone_no = df['telefono'][i]
        phone_no = phone_no.replace(" ", "")
        phone = driver.find_element(By.ID,'phone')
        try:
            phone.clear()
        except:
            pass
        phone.send_keys(phone_no)
        time.sleep(5)
        driver.find_element(By.ID,'btnAiSubmit').click()
        time.sleep(6)
        driver.find_element(By.ID,'btnConfirm').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
if __name__ == "__main__":
    driver.get("https://areariservata.subito.it/login_form")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"didomi-notice-agree-button").click()
    driver.implicitly_wait(10)
            #user name                password
    login('maqsoomahmed98@gmail.com','maqsoom1')
    placeadd()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='index-module_button-add__uLc1X']").click()