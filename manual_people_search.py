# initialize
import time
from selenium import webdriver
import datetime
import pandas as pd

browser=''

def checkcaptcha(browser):
    time.sleep(2)
    try:
        recap=browser.find_element_by_class_name("g-recaptcha")
        raw_input("Press Enter when Captcha bypassed")
    except:
        pass

    try:
        if "Log in" in browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div/h1[1]').text:
            #login(params,browser)
            raw_input("Manually Login and Press Enter ")
    except:
        pass

def login(params,browser):
    url=r"https://www.upwork.com/ab/account-security/login"
    #url=r"https://www.upwork.com/ab/jobs-home/1189733"
    browser.get(url)
    time.sleep(4)

    username=params[0]
    password=params[1]
    try:
        #ui.WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.ID, "login_username")))
        id=browser.find_element_by_id('login_username')
        id.send_keys(str(username))
        pw=browser.find_element_by_id('login_password')
        pw.send_keys(str(password))
        time.sleep(3)
    except:
    #click
        pass
        #raw_input("Press enter when you have entered your login credentials")

    try:
        time.sleep(5)
        #raw_input("Press enter when you have entered your login credentials")
        #browser.find_element_by_tag_name('button').click()
    except:
        time.sleep(5)

    checkcaptcha(browser)

        #ActionChains(browser).move_to_element(hover).click(click).perform()

    time.sleep(2)
    # browser.get('https://www.upwork.com/ab/jobs-home/1189733')
    #ui.WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "twist-table")))
    #a=1

inputfile="input.csv"
#=======================================
# Open Input File
#=======================================
input = pd.read_csv(inputfile)
userow=input[input.id==int(1)].values.tolist()[0]
baseline=input[input.id==int(0)].values.tolist()[0]
params=[baseline[1],baseline[2]]
amount=str(userow[3])
batchsize=int(userow[4])

now = datetime.datetime.now()
dater=str(now.year)+"_"+str(now.month)+"_"+str(now.day)
# wr=open('output.csv','w')

path_to_chromedriver = r"chromedriver.exe"

chrome=raw_input("Chrome or Firefox? ")

if chrome.lower()=="chrome":
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
else:
    fp = webdriver.FirefoxProfile()
    path_modify_header = 'modify_headers-0.7.1.1-fx.xpi'
    fp.add_extension(path_modify_header)
    fp.set_preference("modifyheaders.headers.count", 1)
    fp.set_preference("modifyheaders.headers.action0", "Add")
    fp.set_preference("modifyheaders.headers.name0", "nm") # Set here the name of the header
    fp.set_preference("modifyheaders.headers.value0", "vl") # Set here the value of the header
    fp.set_preference("modifyheaders.headers.enabled0", True)
    fp.set_preference("modifyheaders.config.active", True)
    fp.set_preference("modifyheaders.config.alwaysOn", True)
    try:
        browser = webdriver.Firefox(firefox_profile=fp)
    except:
        browser = webdriver.Firefox()

#browser.get('https://www.upwork.com')
# search
# freelancer list

login(params,browser)

# list.find_element_by_class_name()
raw_input("Set your search criteria and press enter ")
filename="manual_search"
writefile='%s_%s.csv' % (dater, filename)
f = open(writefile, 'w')
# renamecolumns={'imageurl': 'portrait_50','profileurl': 'id','wage': 'rate','status': 'feedback','location': 'country'}
# df2.head()
f.write('imageurl,profileurl,name,title,description,wage,earned,status,location\n')

count = 0
nextbutton = True
while nextbutton == True:
    time.sleep(1)
    # //*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[2]
    # list=browser.find_element_by_xpath('//*[@id="layout"]/div[2]/div[2]/div/div/div/div/div/div[1]/div/freelancers-search/div/div[2]')
    try:
        list = browser.find_element_by_class_name('ats-applicants')
        people = list.find_elements_by_tag_name('article')
    except:
        list = browser.find_element_by_class_name('air-card-sm')
        people = list.find_elements_by_tag_name('section')


    for p in people:

        try:
            image = p.find_element_by_class_name('col-md-10')
            div = image.find_element_by_tag_name('div')
            # driver.find_element_by_xpath('//input[@node-type="searchInput"]')
            # driver.find_elements_by_xpath('.//span[contains(text(), "Author")]/a')
            # print('------')
            imageurl = div.get_attribute('data-photo-url')
            # print(imageurl)

            content = p.find_element_by_class_name('col-md-9')
            namediv = content.find_element_by_tag_name('a')

            try:
                name = namediv.text.decode('utf-8', 'ignore').replace(",",".").replace('"','').replace("'",'')

            except:
                name=''

            profileurl = namediv.get_attribute('href')

            try:
                title = content.find_element_by_tag_name('strong').text.decode('utf-8', 'ignore').replace(",",".").replace('"','').replace("'",'')
            except:
                title=''
            # print(name,profileurl,title)
            try:
                print name
            except:
                print "Can't Display Name"

            try:
                # description = content.find_element_by_xpath('//p[@data-qa="tile_description"]').text.decode('utf-8', 'ignore')
                # p-0-left
                description=''
                description = content.find_element_by_class_name('p-0-left').text.decode('utf-8', 'ignore').replace(",",".").replace('"','').replace("'",'')
            except:
                description = ''
            # print(description)

            details = content.find_element_by_class_name('m-0-bottom')
            detailslist = ['wage', 'earned', 'success(opt)', 'location']
            detailsvals = []
            for d in details.find_elements_by_class_name('col-md-3'):
                t = d.text.strip().decode('utf-8', 'ignore').replace(",",".").replace('"','').replace("'",'')
                # print(t)
                detailsvals.append(t)

            try:
                f.write('%s,%s,%s,%s,%s,%s\n' % (imageurl, profileurl, name.encode(encoding='UTF-8', errors='strict'),
                                                 title.encode(encoding='UTF-8', errors='strict'),
                                                 description.encode(encoding='UTF-8', errors='strict'), ",".join(detailsvals)))
            except:
                f.write('%s,%s,"name_error"\n' % (imageurl, profileurl))

        except:
            pass

    #==============================
    # click next
    #==============================

    try:
        child = browser.find_element_by_xpath('//a[contains(text(), "Next")]')
        parent = child.find_element_by_xpath('..')
        # child.is_disabled
        classes = parent.get_attribute("class")

        if 'disabled' in classes:
            f.close()
            nextbutton = False
            print 'disabled'
        else:

            child.click()
            time.sleep(3)
            print "--New Page--"

    except:
        f.close()
        nextbutton = False

    count += 1
    print count


print "Results are at " + '%s_%s.csv' % (dater, filename)
