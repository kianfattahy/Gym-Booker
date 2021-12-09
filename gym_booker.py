#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import *

#place chromedriver in the same directory as this program
chromedriver_location = './chromedriver'
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://hnd-p-ols.spectrumng.net/mcgill/Home.aspx?/Members/Default.aspx')
# user and pass -- need to be set here one time
username = ''
password = ''

# store the XPaths in variables
first_page = '//*[@id="img_GRX"]'
list_view = '//*[@id="ctl00_pageContentHolder_lnkGriedView"]'
tomorrow = '//*[@id="pnlSelection"]/table[1]/tbody/tr[6]/td[2]/table/tbody/tr/td[2]/span/label'

t = open('workout.txt', 'r')
text = t.read()
print(text)
workout = text
workout_slot = '//*[@id="' + workout + '"]/div[4]'
t.close()

#rewrites the id to set it up as the appropriate workout for the next day
#incrementing by one ensures the same time workout for the next day in the table on the website
f = open('workout.txt', 'w')
f.write(str(int(workout) + 1))
f.close()




enroll = '//*[@id="divClassDetails"]/div[2]/div[1]/span[1]/div/input'
covid = '//*[@id="btnWaiverAgree"]'

user_field = '//*[@id="ctl00_pageContentHolder_loginControl_UserName"]'
pass_field = '//*[@id="ctl00_pageContentHolder_loginControl_Password"]'

login_button = '//*[@id="ctl00_pageContentHolder_loginControl_Login"]'
register = '//*[@id="ctl00_pageContentHolder_btnContinueCart"]'



def login():
    # choose slot and go thru to sign in
    driver.find_element_by_xpath(first_page).click()

    #wait for it to become clickable
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
    workout_slot))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
    enroll))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
    covid))).click()



    # username
    driver.find_element_by_xpath(user_field).click()
    driver.find_element_by_xpath(user_field).send_keys(username)

    # password
    driver.find_element_by_xpath(pass_field).click()
    driver.find_element_by_xpath(pass_field).send_keys(password)

    # login button
    driver.find_element_by_xpath(login_button).click()

    # register
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                register))).click()


login()











