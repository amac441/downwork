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
import datetime
now = datetime.datetime.now()
dater=str(now.year)+"_"+str(now.month)+"_"+str(now.day)


#==================

fp = webdriver.FirefoxProfile()
path_modify_header = 'modify_headers-0.7.1.1-fx.xpi'
fp.add_extension(path_modify_header)
fp.set_preference("modifyheaders.headers.count", 1)
fp.set_preference("modifyheaders.headers.action0", "Add")
fp.set_preference("modifyheaders.headers.name0", "firefox") # Set here the name of the header
fp.set_preference("modifyheaders.headers.value0", "20.1") # Set here the value of the header
fp.set_preference("modifyheaders.headers.enabled0", True)
fp.set_preference("modifyheaders.config.active", True)
fp.set_preference("modifyheaders.config.alwaysOn", True)
browser = webdriver.Firefox(firefox_profile=fp)

#==================

#wr=open('output.csv','w')
#timestamp=datetime.now()
path_to_chromedriver = r"chromedriver.exe"
#browser = webdriver.Firefox()  #Chrome(executable_path = path_to_chromedriver)
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
    ui.WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.ID, "login_username")))
    id=browser.find_element_by_id('login_username')
    id.send_keys(username)
    pw=browser.find_element_by_id('login_password')
    pw.send_keys(password)
    #click
    time.sleep(5)

    #browser.find_element_by_tag_name('button').click()

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

def find_freelancers():
    url=r'https://www.upwork.com/ab/profiles/search/'
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[1]/freelancer-facet-search/freelancer-search/freelancer-search-form/div/div[1]/div').click()
    #$1 dollar earned
    browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[1]/freelancer-facet-search/freelancer-search/facet-panel/div/div[1]/div[1]/facet-input-radio-list/div/div[2]/label/input').click()
    #last worked
    browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[1]/freelancer-facet-search/freelancer-search/facet-panel/div/div[2]/div[4]/facet-input-radio-list/div/div[2]/label/input').click()
    #categories
    browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[1]/freelancer-facet-search/freelancer-search/facet-panel/div/div[2]/div[1]/facet-input-category/div/div[4]/a').click()

    raw_input('Finished Searching')

    #freelancer list
    list=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[2]')
    people=list.find_element_by_tag_name('article')
    # list.find_element_by_class_name()
    for p in people:
        image=p.find_element_by_class_name('col-md-10 p-0-right text-center')
        div=image.find_element_by_tag_name('div')
        # driver.find_element_by_xpath('//input[@node-type="searchInput"]')
        # driver.find_elements_by_xpath('.//span[contains(text(), "Author")]/a')
        imageurl=div.get_attribute('data-photo-url')

        content=p.find_elements_by_class_name('col-md-9')
        namediv=content.find_element_by_tag_name('a')
        name=namediv.text
        profileurl=namediv.get_attribute('href')

        title=content.find_element_by_tag_name('strong').text
        print(name,profileurl,title)
        details=content.find_element_by_class_name('m-0-bottom')
        detailslist=['wage','earned','success(opt)','location']
        detailsvals=[]
        for d in details.find_elements_by_class_name('col-md-3'):
            t = d.text
            print(t)
            detailsvals.append(t)

        description = content.find_element_by_xpath('//p[@data-qa="tile_description"]').text

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

    skills = ['Article Writing','Blog Writing', 'Content Writing']

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

    try:
        typ1=browser.find_element_by_xpath('//*[@id="PostForm_qualifications_freelancerType"]').click()
        time.sleep(1)
        indp=browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/div/div[1]/div[2]/div/div/ul/li[2]').click()
        time.sleep(1)
        ActionChains(browser).move_to_element(typ1).click(indp).perform()
    except:
        pass

    try:
        typ2=browser.find_element_by_xpath('//*[@id="PostForm_qualifications_jobSuccessScore"]').click()
                                            #//*[@id="PostForm_qualifications_jobSuccessScore"]
        time.sleep(1)
        indp=browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/div/div[2]/div[2]/div/div/ul/li[1]').click()
        time.sleep(1)
        ActionChains(browser).move_to_element(typ2).click(indp).perform()
    except:
        pass

    try:
        typ3=browser.find_element_by_xpath('//*[@id="PostForm_qualifications_oDeskHours"]').click()
        time.sleep(1)
        indp=browser.find_element_by_xpath('//*[@id="PostForm_qualifications"]/div/div[4]/div[2]/div/div/ul/li[2]').click()
        time.sleep(1)
        ActionChains(browser).move_to_element(typ3).click(indp).perform()
    except:
        pass
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

def progress():
    progs=[]
    urls=open('urls.txt','r')
    for url in urls:
        browser.get(url.replace("\n",''))
        time.sleep(3)
        prognum=0
        try:
            progstr=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/div[2]').text
            if progstr=='':
                a=b

            prognum=int(progstr.split(" ",1)[0])

        except:
            try:
                                                       #//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/ul                                                   #//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/ul
                jobsdiv=browser.find_element_by_class_name("list-unstyled")
                #jobsdiv=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/ul')
                jd=jobsdiv.find_elements_by_tag_name('li')
                for j in jd:
                    prog=j.find_element_by_tag_name('em').text
                    if "Job in progress" in prog:
                        prognum+=1
            except:
                pass

        progs.append(prognum)

    urls.close()
    return progs

#search members from list
def findMembers(df2,start,stop,messagetext,amount,create="T",negot='not negotiable',mod=11):
    #https://www.upwork.com/freelancers/_~01ff203de58fed31fb/
    df=df2[start:stop].copy()
    df['worked']=''
    df['jobs']=''
    df['earned']=''
    df['accolade']=''
    df['success']=''
    df['availability']=''
    df['messaged']=""
    df['job_in_progress']=''
    df['scraped_rate']=''
    df['language']=''
    df['college']=''
    df['country']=''

    f=open('catcherrors.txt','w')
    f.write("url,worked,jobs,earned,accolade,success,availability,messaged,job_in_progress,scraped_rate,language,college,country")
    count=0

    for index, row in df.iterrows():
        count+=1
        print(count)
        if count%10<mod:
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

            try:
                language=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/o-profile-languages/div/ul/li/div/span[1]').text
            except:
                language=""

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
                try:
                    progstr=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/div[2]').text
                    if progstr=='':
                        a=b

                    prognum=int(progstr.split(" ",1)[0])

                except:
                    try:
                        jobsdiv=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/ul')

                    except:
                        try:
                            jobsdiv=browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[1]/div[2]/o-profile-assignments/div/div/div[2]/div/ul')

                        except:
                            pass

                jd=jobsdiv.find_elements_by_tag_name('li')
                for j in jd:
                    prog=j.find_element_by_tag_name('em').text
                    if "in progress" in prog:
                        prognum+=1
            except:
                print ("Error getting Jobs in Progress")

            college = ''
            try:
                clg=browser.find_element_by_xpath('//o-profile-education[@items="vpd.education"]')
                lists = clg.find_elements_by_tag_name('li')
                for l in lists:
                    college = l.text
                    college = college.encode('ascii', 'replace')
                    a=1

            except:
                pass

            time.sleep(1)

            #find invite element
            try:
                browser.find_element_by_xpath('//*[@id="oProfilePage"]/div[2]/section[1]/div[1]/div/button/span').click()
            except:
                pass
            time.sleep(2)

            #invite.click()
            try:
                textbox=browser.find_element_by_xpath('//*[@id="interview-invitation-popup-message"]')
                textbox.clear()
                first=row['name'].split(" ",1)[0].title()
                textbox.send_keys(messagetext % (first, negot, str(amount)))
                time.sleep(1)
            except:
                if create=="T":
                    raw_input("Message Popup Not Sent")
                else:
                    print "Skipping it "+freeurl

            #SEND MESSAGE
            if create=="T":
                try:
                    browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/form/div/button').click()
                                    #MARK AS SENT
                    df.set_value(index,'messaged',"Y")
                except:
                    try:
                        browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/form/div/button').click()
                                        #MARK AS SENT
                        df.set_value(index,'messaged',"Y")
                    except:
                        df.set_value(index,'messaged',"N")
            else:
                df.set_value(index,'messaged',"NA")

            try:
                country=browser.find_element_by_xpath("//span[@itemprop='country-name']").text
            except:
                country=''

            # if prognum==0:
            #     progrum=''
            # else:
            #     prognum=str(prognum)

            # df.loc[index,'new']=1
            df.set_value(index,'worked',worked)
            df.set_value(index,'jobs',jobs)
            df.set_value(index,'earned',earned)
            df.set_value(index,'accolade',rising)
            df.set_value(index,'success',success)
            df.set_value(index,'availability',availtext)
            df.set_value(index,'scraped_rate',rate)
            df.set_value(index,'job_in_progress',prognum)
            df.set_value(index,'language',str(language))
            df.set_value(index,'college',college)
            df.set_value(index,'country',country)

            try:
                f.write(",".join([freeurl,worked,jobs,earned,rising,success,availtext,rate,str(prognum),language,college]))
            except:
                pass

        else:
            a=1

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
        url=list[-2]
        name=list[-1].split(' ',1)[0]
        #get proposal URL
        if url!='Withdrew' and "No Proposal" not in url:
            try:
                browser.get(url)
                time.sleep(4)
                checkcaptcha()
                amt=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[3]/h1').text
                list.append(amt)
                proplist[prop]=list
            except:
                print "Reading Prop URL broken " + url
    return proplist

def read_message(browser=browser,ms='',decline=False):
    url=r'https://www.upwork.com/messages/'
    browser.get(url)
    time.sleep(3)
    checkcaptcha()
    time.sleep(2)
    proposals={}
    # //*[@id="room-nav"]/div[2]/div/div/div[3]/div/ul
    try:
        table=browser.find_element_by_xpath('*[@id="room-main-body"]/div[2]/ui-view/div/table/tbody')
        table=browser.find_element_by_xpath('//*[@id="room-nav"]/div[2]/div/div/div[3]/div/ul')

    except:
        try:
            table=browser.find_element_by_xpath('//*[@id="room-nav"]/div[2]/div/div/ul')
        except:
            # try = browser.find_element_by_xpath('//*[@id="room-nav"]/div[2]/div/div/ul')

            print "No Interviews Table"
            sys.exit(1)

    #interview=browser.find_element_by_xpath('*[@id="room-nav"]/div[2]/div/div/div[3]/div')
    act = webdriver.common.action_chains.ActionChains(browser)

    for item in table.find_elements_by_tag_name('li'):
        name=item.find_element_by_class_name('room-list-name-span').text
        fname=name.split("\n",1)[1]
        item.click()
        time.sleep(2)

        if decline==True:
            name=fname.split(' ',1)[0]
            name=name.title()
            mes=ms % name
            # act.send_keys(mes)
            # act.perform()
            # if name!="Samira" and name!='Atta':
            #     try:
            #         browser.find_element_by_xpath('//*[@id="story-box"]/div[2]/eo-rooms-composer/div/form/div/span[2]/div/button').click()
            #     except:
            #         pass

            try:
                time.sleep(2)
                try:
                    msgb=browser.find_element_by_class_name('msg-composer-area')
                    msgbox=msgb.find_element_by_tag_name("textarea")
                    msgbox.send_keys(mes)
                except:
                    try:
                        msgbox=browser.find_element_by_class_name('msg-composer-input')
                        msgbox.send_keys(mes)
                    except:
                        pass
                #msgbox=browser.find_element_by_xpath('//*[@id="story-box"]/div[2]/eo-rooms-composer/div/form/div/span[1]/div/div[2]/textarea')
                time.sleep(2)
                #click
                if fname!="Will Xu":# and name!='Atta' and name!="Jennifer" and name!="Will":
                    try:
                        browser.find_element_by_xpath('//*[@id="story-box"]/div[2]/eo-rooms-composer/div/form/div/span[2]/div/button').click()
                    except:
                        pass
                time.sleep(2)
            except:
                pass


        #messages=browser.find_element_by_xpath('//*[@id="story-box"]/div[1]/div/div[2]/div[2]/div')
        try:

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


            #get profile URL
            namediv=browser.find_elements_by_xpath("//div[@class='story-wrapper']")[-1]
            namediv.find_element_by_tag_name('eo-story-header').click()
            time.sleep(2)
            dr = browser.find_element_by_class_name('dropdown-menu')
            profileA = dr.find_elements_by_xpath("//li[@ng-if='user.profile']")
            for link in profileA:
                try:
                    profile_url = link.find_element_by_tag_name('a').get_attribute('href')
                except:
                    pass

            #{Name:[data],Name:[data]}
            try:
                proposals[profile_url]=[name,messagetime,message,proposal_url,name]
            except:
                proposals={}
        except:
            pass

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

    #====================================
    #1 details <file>
    #====================================
    if type=='details':
        params=['ellywood06@gmail.com','kRCdWssNT3']
        login(params)
        count=1
        dfresource=pd.read_csv(inputfile)
        start=0
        stop=2000
        invitemessagetext="test %s %s %s"
        amount=10
        create='F'
        negot='F'

        # with open(inputfile, ‘rb’) as f:
        # reader = csv.reader(f)
        # for row in reader:
        mod=11   #if mode less than 11
        dataframe=findMembers(dfresource,start,stop,invitemessagetext,amount,create,negot,mod)
	
		
        dataframe.to_csv(dater+"_manual_details.csv")
        raw_input("Done with Details")
        browser.close()
        sys.exit(0)


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

    invitemessagetext='''Hello %s!\nI'd like to invite you to apply to my job that entails writing a blog article (800-1000 words; ~5 hours). Please review the job post and apply if you're available.\n--Suggested hourly rate: $18 (It is %s)\n--Average hourly rate I have paid on Upwork: $%s\nJennifer'''

    dfresource=pd.read_csv(file)

    start=(int(number)-1)*25
    stop = int(number)*25
    if start<0:
        start=0
        stop=25

    if type=="decline":
        mes="Dear %s, thank you very much for accepting my invitation. I appreciate your time! Unfortunately, " \
            "I have to cancel the project. I am sorry for the inconvenience."

        for index,row in input.iterrows():
            num=int(row['id'])
            if num!=0:
                row=list(row)
                browser = webdriver.Firefox(firefox_profile=fp)

                # browser = webdriver.Firefox()  #Chrome(executable_path = path_to_chromedriver)
                params=[row[1],row[2]]
                login(params,browser)
                try:
                    proplist=read_message(browser,mes,True)
                except:
                    try:
                        raw_input('Retry? ')
                        proplist=read_message(browser,mes,True)
                    except:
                        pass

    if type=="iterate":
        #csvname=r"C:\Users\amac\Documents\GoogleDrive\Washu\01-17-Dai\Upwork\UpworkShared\Filled_Run_02_25_all.csv"
        dfout = pd.read_csv(outfile)

        # row_iterator = input.iterrows()
        # _, last = row_iterator.next()  # take first item from row_iterator

        for index,row in input.iterrows():

            try:
                num=int(row['id'])
            except:
                num=0

            if num!=0:

                row=list(row)
                print "Reading Input Row "+ str(num) + " " + str(row[1])
                browser = webdriver.Firefox(firefox_profile=fp)

                # browser = webdriver.Firefox()  #Chrome(executable_path = path_to_chromedriver)
                params=[row[1],row[2]]
                login(params,browser)
                try:
                    proplist=read_message(browser)
                    proplist2=proposals(proplist,browser)
                except:
                    try:
                        raw_input('Retry? ')
                        proplist=read_message(browser)
                        proplist2=proposals(proplist,browser)
                    except:
                        print 'twice crashed - writing what we have'

                propout = open('proput.txt','w')
                propout.write(str(proplist2))
                propout.close()

                df2=dfout[num-1:num*25] #slice df
                for p in proplist2:
                    try:
                        # pr = p.split("\n")[1]
                        # name = pr.split(' ',1)
                        # fname=name[0]
                        # lname=name[1][0] #first initial
                        # name2=fname+" "+lname
                        dfindex=df2[df2.id.str.contains(p)].index
                        dfout.loc[dfindex,'MessageTime']=proplist[p][1]
                        dfout.loc[dfindex,'MessageText']=proplist[p][2] #text
                        dfout.loc[dfindex,'ProposalAmount']=proplist[p][5] #amount
                        a=1
                    except:
                        pass
                browser.close()

        try:
            dfout.to_csv(dater+"Final_"+outfile+".csv",encoding='utf-8')
        except:
            dfout.to_csv(dater+"Final_"+outfile+".csv",sep='\t',encoding='utf-8')

    elif type=='progress':
        login(params)
        data=progress()
        f=open('progout.txt','w')
        f.write(str(data))
        f.close()

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

        dataframe.to_csv(dater+outfile)

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
