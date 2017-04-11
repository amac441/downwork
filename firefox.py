#ScriptName : Login.py
#---------------------
from selenium import webdriver
import time
#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://www.mywebsite.com/login.php"
username = "admin"
password = "admin"

xpaths = { 'usernameTxtBox' : "//input[@name='username']",
           'passwordTxtBox' : "//input[@name='password']",
           'submitButton' :   "//input[@name='login']"
         }

browser = webdriver.Firefox()
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
username='ajkrell@yahoo.com'
password='gogogo123'
ui.WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.ID, "login_username")))
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