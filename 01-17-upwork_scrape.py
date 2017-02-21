#Search for Candidates
#https://developers.upwork.com/?lang=python#public-profiles_search-for-freelancers

#Extract and Randomize

##Create Job
#def createJob():
#    #take in CSV - email, jobs

#    #submit

#    #storeURL

#def messageCandidates():
#    #look at extraction

#    #message candidates about specific Job

##Revew Responses

from selenium import webdriver
import time
import string, sys
import csv
from datetime import datetime
#wr=open('output.csv','w')
timestamp=datetime.now()
path_to_chromedriver = r"E:\Development\chromedriver.exe"

#======
#Submitting Job
#======

#=========Login==============
url=r"https://www.upwork.com/ab/account-security/login"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.get(url)
time.sleep(4)    

##browser.switch_to_frame(browser.find_elements_by_tag_name("iframe")[0])
#recap=browser.find_element_by_class_name("g-recaptcha")
## move the driver to the first iFrame 
#browser.switch_to_frame(browser.find_elements_by_tag_name("iframe")[0])       
## *************  locate CheckBox  **************
#CheckBox = browser.find_element_by_id("recaptcha-anchor")
#time.sleep(1)
#CheckBox.click()

username='ajkrell@yahoo.com'
password='gogogo123!'

from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

ui.WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "login_username")))
id=browser.find_element_by_id('login_username')
id.send_keys(username)
pw=browser.find_element_by_id('login_password')
pw.send_keys(password)
#click
browser.find_element_by_tag_name('button').click()

try:
    #look for "Captcha" request
    danger=browser.find_element_by_class_name('alert-danger')
    raw_input("Need to bypass Captcha")

except:
    try:
        recap=browser.find_element_by_class_name("g-recaptcha")
        raw_input("Need to bypass Captcha")
    except:
        pass

#=============
# POST JOB DEDICATED
#=============

postjoburl = r'https://www.upwork.com/c/1189733/jobs/new?enterprise=no'
browser.get(postjoburl)

jobtype="Writing"

time.sleep(1)
#ui.Select(browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/button')).select_by_value(jobtype).click()
#project type
browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/button').click()
time.sleep(1)
#writing
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

element_to_hover_over=browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/a')#.click()
#copywrite
submenue=browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/ul/li[3]/a')#.click()
time.sleep(1)
ActionChains(browser).move_to_element(element_to_hover_over).click(submenue).perform()

#Title
browser.find_element_by_xpath('//*[@id="PostForm_title"]').send_keys('Test')
browser.find_element_by_xpath('//*[@id="PostForm_description"]').send_keys('Test2')
#WebElement.send_keys(Keys.RETURN);
browser.find_element_by_xpath('//*[@id="PostForm_employmentType"]/div[1]/label').click()
skillslabel=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/form/div/div/div[2]/div/div/div[6]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/input')
skillslabel.send_keys("Test")
skillslabel.send_keys(Keys.RETURN)
time.sleep(1)
skillslabel.send_keys("Test2")
skillslabel.send_keys(Keys.RETURN)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="PostForm_contractorTier"]/div/div[1]/div').click()
browser.find_element_by_xpath('//*[@id="PostForm_duration"]/div/div[3]/div').click()
browser.find_element_by_xpath('//*[@id="PostForm_engagementType"]/div/div[2]/div').click()
browser.find_element_by_xpath('//*[@id="PostForm_questions"]/div[1]/div/div/div[1]/textarea').send_keys("Test Screening Question")
#browser.find_element_by_xpath('


a=1
#copywriting values
#//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/ul/li[3]/a


#post job popup
#/html/body/div[5]/div/div/div[2]/div[2]/div/label/span