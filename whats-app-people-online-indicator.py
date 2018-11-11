from selenium import webdriver
import time

import json
from urllib.request import urlopen,Request
from urllib.parse import urlencode
import time

from datetime import datetime

from selenium import webdriver


localtime = time.asctime(time.localtime(time.time()))
def target():

    driver=webdriver.Chrome("C:\\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")


    input("scan the qr code using mobile phone manually")

    time.sleep(3)

    search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label')
    search_name=input('enter the name')
    search.send_keys('search_name')
    input('wait until the name in a list')


    search_click=driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[2]/div').click()


    time.sleep(20)
    print(localtime)
    online(driver)

def online(driver):

    while '1' == '1':

            time.sleep(10)
            #driver.find_element_by_class_name('O90ur').is_displayed()
            check_fun=driver.find_element_by_class_name('O90ur')

            if check_fun != 'online':


                message_send_call(driver)


            else:
                None




def message_send_call(driver):
    TO = 'place a sender mobile number here'

    print(    "Local current time :", localtime)

    times=localtime
    message = '''online\n''' + str(times)
    
    mob = 'place a mobile number here'
    passw = 'place a login password here'
    try:


                        #https://smsapi.engineeringtgr.com/ visit a website to generate an api key 
                        apikey=('enter the api key here')
                        #example_apikey="thamav9lOdWuZRaSfDrXmM95N3e472"
                        api = apikey

                        headers = {"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://thewebsite.com",
"Connection": "keep-alive"}

                        values={
                            'Mobile':mob,
                            'Password':passw,
                            'Message': message,
                            'To': TO,
                            'Key':api
                        }
                        datas = urlencode(values)
                        data=datas.encode('ascii')
                        urls= "https://smsapi.engineeringtgr.com/send/"
                        url=urls+'?'+datas
                        req = Request(url,data,headers)
                        response = json.loads(urlopen(req).read())
                        print(response)


                        if response['status'] == "False":

                         print("check apikey")
                         message_send_call()

                        else:

                         print("SMS Send Successfully")
                         print(datetime.now())
                         time.sleep(10)
                         logout_waiting(driver)




    except Exception as e:
       print(e)


def logout_waiting(driver):

    while '1' == '1':
        check_fun=driver.find_element_by_class_name('O90ur')

        if check_fun != 'online':


            None


        else:

            online()



if __name__ == '__main__':

  target()
