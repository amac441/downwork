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

import time

#wr=open('output.csv','w')
timestamp=datetime.now()
path_to_chromedriver = r"chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
#======
#Submitting Job
#======

#=========Login==============

def checkcaptcha(params=[]):
    # try:
    #     #look for "Captcha" request
    #     danger=browser.find_element_by_class_name('alert-danger')
    #     raw_input("Need to bypass Captcha")
    #
    # except:
    try:
        recap=browser.find_element_by_class_name("g-recaptcha")
        raw_input("Press Enter when Captcha bypassed")
    except:
        pass

    try:
        if "Log" in browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div/h1[1]').text:
            login(params)
    except:
        pass

def login(params,browser=browser):
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
        try:
            browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/h1')
        except:
            try:
                browser.find_element_by_xpath('//*[@id="skinny-nav"]/ul[2]/li[4]/a/span[1]').click()
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="skinny-nav"]/ul[2]/li[4]/ul/li[2]/ul/li[2]/a/div/div').click()
                time.sleep(1)
            except:
                pass

        checkcaptcha(params)

        #ActionChains(browser).move_to_element(hover).click(click).perform()

    time.sleep(2)
    # browser.get('https://www.upwork.com/ab/jobs-home/1189733')
    #ui.WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "twist-table")))
    #a=1

#=============
# POST JOB DEDICATED
#=============

def create_job(amount,create='T',negot="not negotiable"):
    postjoburl = r'https://www.upwork.com/c/1189733/jobs/new?enterprise=no'
    browser.get(postjoburl)

    jobtype="Writing"

    time.sleep(3)
    #ui.Select(browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/button')).select_by_value(jobtype).click()

    #project type
    #//*[@id="PostForm_categoryDropdown"]/div/div/button/span[1]
    try:
        browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/button').click()
        time.sleep(1)
        #writing
        element_to_hover_over=browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/a')#.click()
        #article and blog
        submenue=browser.find_element_by_xpath('//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/ul/li[2]/a')#.click()
        time.sleep(1)
        ActionChains(browser).move_to_element(element_to_hover_over).click(submenue).perform()
    except:
        pass

    #data
    title="Looking for Writer of Blog Article on the Pros and Cons of Freelancing"
    description=u'''I seek a writer to create an original blog article for me on the topic of the pros and cons of freelancing.
        \nThis will be done on a ghost writing basis. Research and writing will be involved. Please use links for source information.The content will focus on what the available literature says about the advantages and disadvantages of freelancing.If appropriate, possibly include small segment of one freelancer’s personal experience.
        \nThe target audience is people in the general public considering freelance work who desire more information.The style is to be informal, interesting, and engaging. Language is English (American). Suggestions for images are a plus but not required.
        \nEstimated length: 800-1000 words\nEstimated length of time for project: 5 hours (to include one re-edit)\nDeadline: March 10, 2017
        \nSuggested hourly rate: $18 (It is %s.)\nAverage hourly rate I have paid on Upwork: $%s
        ''' % (negot, amount)

    skills = ['Article Writing','Blog Writing', 'Content Writing', 'Internet Research']

    #Title
    browser.find_element_by_xpath('//*[@id="PostForm_title"]').send_keys(title)
    browser.find_element_by_xpath('//*[@id="PostForm_description"]').send_keys(description)
    #WebElement.send_keys(Keys.RETURN);
    browser.find_element_by_xpath('//*[@id="PostForm_employmentType"]/div[1]/label').click()
    try:
        skillslabel=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/form/div/div/div[2]/div/div/div[6]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/input')
    except:
        try:
            skillslabel=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/form/div/div/div[2]/div/div/div[5]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/input')
        except:
            skills=[]
            print "NO SKILLS"
                                                      
    for skill in skills:
        skillslabel.send_keys(skill)
        time.sleep(3)
        skillslabel.send_keys(Keys.RETURN)
        #skillslabel.click()
        time.sleep(1)
        skillslabel.send_keys(Keys.RETURN)

    #intermediate tier
    browser.find_element_by_xpath('//*[@id="PostForm_contractorTier"]/div/div[2]/div').click()

    #less than 1 week
    browser.find_element_by_xpath('//*[@id="PostForm_duration"]/div/div[5]/div').click()

    #less than 30 hrs
    browser.find_element_by_xpath('//*[@id="PostForm_engagementType"]/div/div[2]/div').click()
    #browser.find_element_by_xpath('//*[@id="PostForm_questions"]/div[1]/div/div/div[1]/textarea').send_keys(screening)

    #only invites
    browser.find_element_by_xpath('//*[@id="PostForm_access"]/div[3]').click()

    #qualificatinos
    browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/button').click()

    typ1=browser.find_element_by_xpath('//*[@id="PostForm_qualifications_freelancerType"]')
    indp=browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/div/div[1]/div[2]/div/div/ul/li[2]')
    time.sleep(1)
    ActionChains(browser).move_to_element(typ1).click(indp).perform()

    typ2=browser.find_element_by_xpath('//*[@id="PostForm_qualifications_jobSuccessScore"]')
                                        #//*[@id="PostForm_qualifications_jobSuccessScore"]
    indp=browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/div/div[2]/div[2]/div/div/ul/li[1]')
    
    time.sleep(1)
    ActionChains(browser).move_to_element(typ2).click(indp).perform()

    typ3=browser.find_element_by_xpath('//*[@id="PostForm_qualifications_oDeskHours"]')
    indp=browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/div/div[4]/div[2]/div/div/ul/li[2]')
    time.sleep(1)
    ActionChains(browser).move_to_element(typ3).click(indp).perform()

    #no cover letter
    browser.find_element_by_xpath('//*[@id="PostForm_coverLetterRequired"]/div/label/span').click()

    #post job

    raw_input("Waiting for Manual")
    browser.find_element_by_xpath('//*[@id="PostForm_actions_post"]').click()
        

#browser.find_element_by_xpath('
#copywriting values
#//*[@id="PostForm_categoryDropdown"]/div/div/ul/li[6]/ul/li[3]/a
#post job popup
#/html/body/div[5]/div/div/div[2]/div[2]/div/label/span


#search members from list
def findMembers(df2,start,stop,messagetext,amount,create="T",negot='not negotiable'):
    #https://www.upwork.com/freelancers/_~01ff203de58fed31fb/
    df=df2[start:stop].copy()
    df['worked']=''
    df['jobs']=''
    df['earned']=''
    df['accolade']=''
    df['success']=''
    df['availability']=''
    df['messaged']=""
    df['job_in_progres']=''
    df['scraped_rate']=''

    for index, row in df.iterrows():
        #print row['c1'], row['c2']
        freeurl=row['id']
        # list = open(r"C:\Development\0117-DaiAnalysis\Upwork\freelancelist.txt",'r')
        browser.get(freeurl)
        time.sleep(3)

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
            success=''

        try:
            rate=browser.find_element_by_xpath('//*[@id="optimizely-header-container-default"]/div[1]/div[1]/div/div[2]/h2/div/span/span[1]').text
        except:
            rate=''
        
        #Availability
        try:
            availsec=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/div[3]')
            availdivs=availsec.find_elements_by_tag_name('div')
            availtext=''
            for div in availdivs:
                line=div.text
                availtext+=line
        except:
            pass

        availtext=''.join(availtext.splitlines())
        #work history

        # //*[@id="oProfilePage"]/div[2]/section[2]/div
        # //*[@id="oProfilePage"]/div[2]/section[2]/div #with rising talent
        # //*[@id="oProfilePage"]/div[2]/section[2]/div
        worked="" # 16 hours worked
        jobs="" # 18 jobs
        earned="" # $900+ earned
        try:
            workhistorysect=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[2]/div')
            workdivs=workhistorysect.find_elements_by_tag_name('div')
            for div in workdivs:
                line=div.text
                linesplit=line.split(" ")
                if 'worked' in line:
                    worked=linesplit[0]
                if 'job' in line:
                    #CHECK JOBS
                    jobs=linesplit[0]
                if 'earned' in line:
                    earned=linesplit[0]
        except:
            pass

        #in progress
        prognum=0
        try:
            progstr=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/div[2]').text
            prognum=int(progstr.split(" ",1)[0])
        except:
            try:
                jobsdiv=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/ul')
                for j in jobsdiv.find_element_by_class_name('li'):
                    prog=j.find_element_by_class_name('em').text
                    if "in progress" in prog:
                        prognum+=1
            except:
                prognum=0


        time.sleep(1)

        #find invite element
        try:
            browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[1]/div[1]/div/button/span').click()
        except:
            pass
        time.sleep(2)

        #invite.click()
        textbox=browser.find_element_by_xpath('//*[@id="interview-invitation-popup-message"]')
        textbox.clear()
        first=row['name'].split(" ",1)[0].title()
        textbox.send_keys(messagetext % (first, negot, str(amount)))
        time.sleep(1)

        #SEND MESSAGE
        if create=="T":
            try:
                browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/form/div/button').click()
                #MARK AS SENT
                df.set_value(index,'messaged',"Y")
            except:
                df.set_value(index,'messaged',"N")
        else:
            df.set_value(index,'messaged',"NA")

        # df.loc[index,'new']=1
        df.set_value(index,'worked',worked)
        df.set_value(index,'jobs',jobs)
        df.set_value(index,'earned',earned)
        df.set_value(index,'accolade',rising)
        df.set_value(index,'success',success)
        df.set_value(index,'availability',availtext)
        df.set_value(index,'scraped_rate',rate)
        df.set_value(index,'job_in_progress',str(prognum))

    #CHANGE OUTFILE
    return df

# def getrandom(file,number):
#     df=pd.read_csv(file)
#     sample=df.sample(number)
#     sample.to_csv("2_24_sampele_"+str(number)+".csv")
#     return sample

#===================

import datetime
import time
ts = time.time()

def proposals(proplist,browser=browser):
    # proplist=[]
    for prop in proplist:
        time.sleep(1)
        list = proplist[prop]
        url=list[-1]
        #get proposal URL
        if url!='Withdrew':
            browser.get(url)
            time.sleep(2)
            checkcaptcha()
            amt=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[3]/h1').text
            list.append(amt)
            proplist[prop]=list

    return proplist

def read_message(browser=browser):
    url=r'https://www.upwork.com/messages/'
    browser.get(url)
    time.sleep(1)
    checkcaptcha()

    proposals={}
    # //*[@id="room-nav"]/div[2]/div/div/div[3]/div/ul
    try:
        table=browser.find_element_by_xpath('*[@id="room-main-body"]/div[2]/ui-view/div/table/tbody')
        table=browser.find_element_by_xpath('//*[@id="room-nav"]/div[2]/div/div/div[3]/div/ul')

    except:
        try:
            table=browser.find_element_by_xpath('//*[@id="room-nav"]/div[2]/div/div/ul')
        except:
            print "No Interviews Table"
            sys.exit(1)

    #interview=browser.find_element_by_xpath('*[@id="room-nav"]/div[2]/div/div/div[3]/div')
    for item in table.find_elements_by_tag_name('li'):
        name=item.find_element_by_class_name('room-list-name-span').text
        name=name.split("\n",1)[1]
        item.click()
        time.sleep(2)

        #messages=browser.find_element_by_xpath('//*[@id="story-box"]/div[1]/div/div[2]/div[2]/div')
        textdiv=browser.find_element_by_xpath('//*[@id="story-box"]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/div/div/div/span')
        # messagedate=...
        messagetime=browser.find_element_by_xpath('//*[@id="story-box"]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div/span/a/span').get_attribute('title')
        message=textdiv.text
        message=availtext='--'.join(message.splitlines())
        #proposal link
        try:
            proposal_url=textdiv.find_element_by_tag_name('a').get_attribute("href")
        except:
            proposal_url="No Proposal URL"

        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #name
        #name=browser.find_element_by_xpath('//*[@id="story-box"]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/span')

        #{Name:[data],Name:[data]}
        proposals[name]=[name,messagetime,message,proposal_url]

    return proposals

import csv
import os
if __name__ == "__main__":

    print os.getcwd()
    start_time = time.time()

    print "Starting Script"
    try:
        number = sys.argv[1]
    except:
        print "Provide inputs: [number - specifying which accounts to go after] [optional: runtype (create,iterate,read-T,F)] [optional:inputfile location] [optional: splitby - how many rows to read]"
        sys.exit(1)

    try:
        type=sys.argv[2].split('-')
        try:
            create=type[1] #T or F
        except:
            create='F'

        type=type[0]
    except:
        print ("Reading Messages")
        type='read'

    try:
        inputfile=sys.argv[3]
    except:
        print ("Using Input.csv")
        inputfile="input.csv"

    # inputcsv = open(inputfile,'r')
    # input = csv.reader(inputcsv)
    # next(input, None)  # skip the headers
    input = pd.read_csv(inputfile)

    userow=input[input.id==int(number)].values.tolist()[0]
    baseline=input[input.id==int(0)].values.tolist()[0]
    params=[userow[1],userow[2]]
    amount=str(userow[3])

    invitemessagetext=userow[4].encode('utf-8')
    if invitemessagetext.lower()=="same":
        invitemessagetext=baseline[4].encode('utf-8')

    file=userow[5]
    if file.lower()=="same":
        file=baseline[5]

    outfile=userow[6]
    if outfile.lower()=="same":
        outfile=baseline[6]

    negot=str(userow[7])

    invitemessagetext='''Hello %s!
    \nI'd like to invite you to apply to my job that entails writing a blog article (800-1000 words; ~5 hours). Please review the job post and apply if you're available.
    \n--Suggested hourly rate: $18 (It is %s)\n--Average hourly rate I have paid on Upwork: $%s\nSunny'''

    # params=['ajkrell@yahoo.com','gogogo123!']
    # p1=["low.jennifer.miller0921@gmail.com","ra123456."]
    # amount1=12
    # p2=["high.jennifer.miller0921@gmail.com","ra123456."]
    # amount2=24
    # #https://www.upwork.com/ab/jobs-home/3336361
    # #p3=["hcyq10ar27@hotmail.com","729noox9tq"]
    # p3=["gjm206yvrg@hotmail.com","t4egxir54j"]
    # amount3=18
    # file=r"2_24_sampele_75.csv"
    # #file="2_24_sampele_10.csv"

    dfresource=pd.read_csv(file)

    start=(int(number)-1)*25
    stop = int(number)*25
    if start<0:
        start=0
        stop=25


    if type=="iterate":
        #csvname=r"C:\Users\amac\Documents\GoogleDrive\Washu\01-17-Dai\Upwork\UpworkShared\Filled_Run_02_25_all.csv"
        dfout = pd.read_csv(outfile)

        # row_iterator = input.iterrows()
        # _, last = row_iterator.next()  # take first item from row_iterator

        for index,row in input.iterrows():
            num=int(row['id'])
            if num!=0:
                row=list(row)
                browser = webdriver.Chrome(executable_path = path_to_chromedriver)
                params=[row[1],row[2]]
                login(params,browser)
                proplist=read_message(browser)
                proplist2=proposals(proplist,browser)
                df2=dfout[num-1:num*25] #slice df
                for p in proplist2:
                    try:
                        name = p.split(' ',1)
                        fname=name[0]
                        lname=name[1][0] #first initial
                        name2=fname+" "+lname
                        dfindex=df2[df2.name.str.contains(name2)].index
                        dfout.loc[dfindex,'MessageTime']=proplist[p][1]
                        dfout.loc[dfindex,'MessageText']=proplist[p][2] #text
                        dfout.loc[dfindex,'ProposalAmount']=proplist[p][4] #amount
                        a=1
                    except:
                        pass
                browser.close()

        try:
            dfout.to_csv("Final_"+outfile+".csv",encoding='utf-8')
        except:
            dfout.to_csv("Final_"+outfile+".csv",sep='\t',encoding='utf-8')


    elif type=="submit" or type=="create":
        login(params)
        if type=="create":
            create_job(amount,create,negot)
            print("--- %s seconds ---" % (time.time() - start_time))
            raw_input("Enter to Send Messages: Start "+ str(start) + " Stop "+ str(stop) + " Amount " + str(amount))

        #login(params)
        dfresource['login']=params[0]
        dfresource['password']=params[1]
        dataframe=findMembers(dfresource,start,stop,invitemessagetext,amount,create,negot)
        dataframe.to_csv("3-1_"+outfile)
        print("--- %s seconds ---" % (time.time() - start_time))

    elif type=='read':
        login(params)
        proplist=read_message()
        proplist2=proposals(proplist)
        f=open('proposals'+number+'.txt','w')
        f.write(str(proplist2))
        f.close()
        #read responses
    raw_input("Press Enter to close browser ")
    browser.close()

#review messages from members?
