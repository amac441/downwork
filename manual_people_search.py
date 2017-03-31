
#initialize
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
#search
#freelancer list

# list.find_element_by_class_name()

f=open('manual_people/people_3.csv','w')
# renamecolumns={'imageurl': 'portrait_50','profileurl': 'id','wage': 'rate','status': 'feedback','location': 'country'}
# df2.head()
f.write('imageurl;profileurl;name;title;description;wage;earned;status;location\n')

count=0
nextbutton=True
while nextbutton==True:
    time.sleep(1)
                                        #//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[2]
    #list=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[2]')
    list=browser.find_element_by_class_name('ats-applicants')
    people=list.find_elements_by_tag_name('article')

    for p in people:

        image=p.find_element_by_class_name('col-md-10')
        div=image.find_element_by_tag_name('div')
        # driver.find_element_by_xpath('//input[@node-type="searchInput"]')
        # driver.find_elements_by_xpath('.//span[contains(text(), "Author")]/a')
        #print('------')
        imageurl=div.get_attribute('data-photo-url')
        #print(imageurl)

        content=p.find_element_by_class_name('col-md-9')
        namediv=content.find_element_by_tag_name('a')
        name=namediv.text
        profileurl=namediv.get_attribute('href')

        title=content.find_element_by_tag_name('strong').text
        #print(name,profileurl,title)
        print(name)
        description = content.find_element_by_xpath('//p[@data-qa="tile_description"]').text
        #print(description)

        details=content.find_element_by_class_name('m-0-bottom')
        detailslist=['wage','earned','success(opt)','location']
        detailsvals=[]
        for d in details.find_elements_by_class_name('col-md-3'):
            t = d.text.strip()
            #print(t)
            detailsvals.append(t)

        f.write('%s;%s;%s;%s;%s;%s\n' % (imageurl,profileurl,name.encode(encoding='UTF-8',errors='strict'),title.encode(encoding='UTF-8',errors='strict'),description.encode(encoding='UTF-8',errors='strict'),";".join(detailsvals)))
        #next button
        #https://www.upwork.com/ab/profiles/search/?revenue=1&rate=10-30&last=15&c=writing&sc=article-blog-writing
    try:

        child=browser.find_element_by_xpath('//a[contains(text(), "Next ›")]')
        parent=child.find_element_by_xpath('..')
        # child.is_disabled
        classes = parent.get_attribute("class");

        if 'disabled' in classes:
            f.close()
            nextbutton=False
            print('disabled')
        else:

            child.click()
            time.sleep(3)
            print("--New Page--")

    except:
        f.close()
        nextbutton=False

    count+=1
    print(count)
