#Search for Candidates
#https://developers.upwork.com/?lang=python#public-profiles_search-for-freelancers

#Modifying Selenium Variable
# http://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

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
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd

#wr=open('output.csv','w')
timestamp=datetime.now()
path_to_chromedriver = r"C:\Development\chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
#======
#Submitting Job
#======

#=========Login==============

def checkcaptcha(params):
    # try:
    #     #look for "Captcha" request
    #     danger=browser.find_element_by_class_name('alert-danger')
    #     raw_input("Need to bypass Captcha")
    #
    # except:
    try:
        recap=browser.find_element_by_class_name("g-recaptcha")
        raw_input("Need to bypass Captcha")
    except:
        pass

    try:
        if "Log" in browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div/h1[1]').text:
            login(params)
    except:
        pass

def login(params):
    url=r"https://www.upwork.com/ab/account-security/login"
    url=r"https://www.upwork.com/ab/jobs-home/1189733"
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
    username=params[0]
    password=params[1]
    ui.WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "login_username")))
    id=browser.find_element_by_id('login_username')
    id.send_keys(username)
    pw=browser.find_element_by_id('login_password')
    pw.send_keys(password)
    #click
    browser.find_element_by_tag_name('button').click()

    checkcaptcha(params)

    try:
        browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div[1]/div/a')
        browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div[2]/div[2]/div/div/div/table')
    except:
        browser.find_element_by_xpath('//*[@id="skinny-nav"]/ul[2]/li[4]/a/span[1]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="skinny-nav"]/ul[2]/li[4]/ul/li[2]/ul/li[2]/a/div/div').click()
        time.sleep(1)
        checkcaptcha(params)

        #ActionChains(browser).move_to_element(hover).click(click).perform()

    # browser.get('https://www.upwork.com/ab/jobs-home/1189733')
    ui.WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "twist-table")))
    a=1

#=============
# POST JOB DEDICATED
#=============

def postJob():
    postjoburl = r'https://www.upwork.com/c/1189733/jobs/new?enterprise=no'
    browser.get(postjoburl)

    jobtype="Writing"

    time.sleep(1)
    #ui.Select(browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/button')).select_by_value(jobtype).click()
    #project type
    browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/button').click()
    time.sleep(1)
    #writing
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
#copywriting values
#//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/ul/li[3]/a
#post job popup
#/html/body/div[5]/div/div/div[2]/div[2]/div/label/span

#message members about a job
def messageMember():
    a=1

#search members from list
def findMembers(df,start,stop):
    #https://www.upwork.com/freelancers/_~01ff203de58fed31fb/
    df['worked']=''
    df['jobs']=''
    df['earned']=''
    df['accolade']=''
    df['success']=''
    df['availability']=''


    for index, row in df[start:stop].iterrows():
        #print row['c1'], row['c2']
        freeurl=row['id']
        # list = open(r"C:\Development\0117-DaiAnalysis\Upwork\freelancelist.txt",'r')
        browser.get(freeurl)
        time.sleep(1)

        #search for ratings elements adn stuff..
        try:
            rising=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[2]/h5/top-rated/div/span').text
        except:
            try:
                rising=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[2]/h5[2]/top-rated/div/span[1]').text
            except:
                rising=''
        # //*[@id="oProfilePage"]/div[2]/section[2]/h5/top-rated/div/span #rising talent
        # //*[@id="oProfilePage"]/div[2]/section[2]/h5[2]/top-rated/div/span[1] #toprated with high job success
        # //*[@id="oProfilePage"]/div[2]/section[2]/h5[2]/top-rated/div/span[1]

        #success

        try:
            success=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[2]/h5[1]/o-job-success/div/div/span').text
        except:
            success=""

        #Availability
        availsec=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/div[3]')
        availdivs=availsec.find_elements_by_tag_name('div')
        availtext=''
        for div in availdivs:
            line=div.text
            availtext+=line

        availtext=''.join(availtext.splitlines())
        #work history

        # //*[@id="oProfilePage"]/div[2]/section[2]/div
        # //*[@id="oProfilePage"]/div[2]/section[2]/div #with rising talent
        # //*[@id="oProfilePage"]/div[2]/section[2]/div
        workhistorysect=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[2]/div')
        workdivs=workhistorysect.find_elements_by_tag_name('div')
        worked="" # 16 hours worked
        jobs="" # 18 jobs
        earned="" # $900+ earned
        for div in workdivs:
            line=div.text.split(" ")
            if 'worked' in line:
                worked=line[0]
            if 'job' in line:
                jobs=line[0]
            if 'earned' in line:
                earned=line[0]

        time.sleep(1)

        #find invite element
        browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[1]/div[1]/div/button/span').click()
        time.sleep(2)

        #invite.click()
        time.sleep(1)
        textbox=browser.find_element_by_xpath('//*[@id="interview-invitation-popup-message"]')
        textbox.clear()
        textbox.send_keys("TESTING POPUP")
        browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/form/div/button').click()

        # df.loc[index,'new']=1
        df[index,'worked']=worked
        df[index,'jobs']=jobs
        df[index,'earned']=earned
        df[index,'accolade']=rising
        df[index,'success']=success
        df[index,'availability']=availtext

# def getrandom(file,number):
#     df=pd.read_csv(file)
#     sample=df.sample(number)
#     sample.to_csv("2_24_sampele_"+str(number)+".csv")
#     return sample


params=['ajkrell@yahoo.com','gogogo123!']

p1=["low.jennifer.miller0921@gmail.com","ra123456"]
amount=12

p1=["high.jennifer.miller0921@gmail.com","ra123456"]
amount=24

p1=["gjm206yvrg@hotmail.com","ra123456"]
amount=18

# login(params)
# create_job(amount)
file=r"C:\Users\amac\Documents\Development\0117-DaiAnalysis\Upwork\2_24_sampele_75.csv"
file=r"C:\Users\amac\Documents\Development\0117-DaiAnalysis\Upwork\2_24_sampele_10.csv"
number=75
start=0 #indicates where in the file to start reading
stop=25 #does not get row 25
#if you split this by 3, you would want to start at 24 and 49

#getrandom(file,number)

# #Read a csv as a dictionary
# reader = csv.DictReader(open(file, 'rb'))
# dict_list = []
# for line in reader:
#     dict_list.append(line)


df=pd.read_csv(file)
login(params)
findMembers(df,start,stop)


#review messages from members?
