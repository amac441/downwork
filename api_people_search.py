import upwork
from selenium import webdriver
import time
#from multiprocess import Process, Queue
import multiprocessing

def writeResources(i,response):
    print "Writing "+str(i)

    keys=['portrait_50',
     'categories2',
     'profile_type',
     'title',
     'skills',
     'country',
     'description',
     'name',
     'last_activity',
     'rate',
     'member_since',
     'portfolio_items_count',
     'id',
     'test_passed_count',
     'feedback']

    csvname='api/upworkResourceCSV_10k_'+str(i)
    f = open(csvname+'.csv','w')
    f.write(";".join(keys))

    for r in response:
        data=[]
        f.write("\n")
        for key in keys:
            try:
                value=r[key]
                if isinstance(value, (list, tuple)):
                    value="--".join(value)
                if key == "id":
                    #https://www.upwork.com/freelancers/_~01ff203de58fed31fb/
                    value=r"https://www.upwork.com/freelancers/_"+value
                value=value.encode('ascii', 'ignore')
                value=''.join(value.splitlines())
                data.append(value.replace(";",'..'))
            except:
                data.append("-")

        f.write(";".join(data))

    f.close()

def login():
    username='ajkrell@yahoo.com'
    password='gogogo123!'
    try:
        time.sleep(2)
        #ui.WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "login_username")))
        id=browser.find_element_by_id('login_username')
        id.send_keys(username)
        pw=browser.find_element_by_id('login_password')
        pw.send_keys(password)
        #click
        browser.find_element_by_tag_name('button').click()
    except:
        print "No Login"

def worker(j,client):
    #for j in range(pr*100,pr*100+100):
    print "Started "+ str(pr)
    response3=[str(j)]
    for i in range(j*100,(j*100)+100):
        data = {'profile_type':'Independent',
                'subcategory2':'Article & Blog Writing'}
        try:
            r=client.provider_v2.search_providers(data=data, page_offset=i*100, page_size=100)
        except:
            try:
                print 'retry'
                time.sleep(1)
                r=client.provider_v2.search_providers(data=data, page_offset=i*100, page_size=100)
            except:
                try:
                    time.sleep(1)
                    print "retry2"
                    r=client.provider_v2.search_providers(data=data, page_offset=i*100, page_size=100)
                except:
                    try:
                        time.sleep(2)
                        print "retry3"
                        r=client.provider_v2.search_providers(data=data, page_offset=i*100, page_size=100)
                    except:
                        r=[]
                        print 'fail'

        response3 = response3+r
    #print i
    writeResources(j,response3)
    #time.sleep(10)
    print j

    return pr

if __name__ == '__main__':
    public_key='8b4e214913168000580280e93e9a2b66'
    secret_key='5a38eba13351a43d'
    client = upwork.Client(public_key, secret_key)
    ver= client.auth.get_authorize_url()

    path_to_chromedriver = r"chromedriver.exe"
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    browser.get(ver)
    print ver
    login()
    code=raw_input("Key ")
    browser.close()

    oauth_access_token, oauth_access_token_secret = client.auth.get_access_token(code)
    client = upwork.Client(public_key, secret_key,
                          oauth_access_token=oauth_access_token,
                          oauth_access_token_secret=oauth_access_token_secret)
    jobs = []
    for pr in range (17,18):
        worker(pr,client)
        # p = multiprocessing.Process(target=worker, args=(pr,client,))
        # jobs.append(p)
        # p.start()
        # q = Queue()
        # p = Process(target=worker, args=[j,client])
        # p.start()
        # print (q.get())
        # p.join()

