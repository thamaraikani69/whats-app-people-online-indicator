###-------------------------------------------------sivaya nama-----------------------------###
from selenium import webdriver
import time

import json
from urllib.request import urlopen,Request
from urllib.parse import urlencode
import time

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def target():

    driver=webdriver.Chrome("C:\\chromedriver.exe")
    driver.get("https://web.whatsapp.com/")


    input("scan the qr code using mobile phone manually")

    time.sleep(3)

    search_name = input('enter the name here')
    search.send_keys(search_name)
    input('enter1')


    search_click=driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[2]/div').click()
    time.sleep(3)
    print(datetime.now())
    online(driver)

def online(driver):

    current_status=driver.find_element_by_class_name('O90ur').text
    print('current status:',current_status)

    while '1' == '1':
        check_fun=driver.find_element_by_class_name('O90ur').text


        if check_fun == 'online':


            print('online\n')
            print(check_fun + '\n')
            print(datetime.now()+'\n')
            message_send_call(driver)


        else:
            None





def message_send_call(driver):
    TO = message_sent
    times=datetime.now()
    message = '''online\n''' + str(times)

    mob = mobile_num
    passw = passw_pass
    try:


                        apikey=apikey
                        #examole apikey="osamav92OdWuZRaSfDrXmM95N3e472"
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
        check_fun=driver.find_element_by_class_name('O90ur').text

        if check_fun == 'online':


            None


        else:

            print ('offline\n')
            print(check_fun+'\n')
            print(datetime.now())
            online(driver)




if __name__ == '__main__':
    
  message_sent=input('enter the sender mobile number' )
  print("create a message api key in here https://smsapi.engineeringtgr.com/ and check a mail")
  apikey=input("enter the apikey")
  mobile_num=input("enter the login mobile number")
  passw_pass=input("enter the login password")
  target()
    
