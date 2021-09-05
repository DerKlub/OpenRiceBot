'''
Welcome to Open Rice Bot. We are glad you joined our mission to bankrupt the United Nations und den Welthunger enden!

To run: 
    -download FireFox
    -pip install selenium
    -enter username on line 43 
    -enter password on line 48
    -enter last four digits of social on line 121

'''


from logging import raiseExceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


class RiceBot:
    def __init__(self):
        self.compare_lst = []
        self.openBrowser()

    def openBrowser(self):
        self.options = webdriver.FirefoxOptions()

        
        self.driver = webdriver.Firefox(options=self.options)  

        self.driver.implicitly_wait(2)     

        self.driver.get("https://freerice.com/profile")

        time.sleep(0.5)

        self.driver.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div[2]/button").click()


        username = self.driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys("") #Your username


        password = self.driver.find_element_by_id("login-password")
        password.clear()
        password.send_keys("") #Your Password 

        self.driver.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div/div[2]/button").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/button").click()


        time.sleep(0.5)
        self.driver.find_element_by_class_name('toolbar__menu-toggle-icon').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div/nav/div/nav/ul/li[2]/div/a').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div[2]/div/div/div[10]/div[1]/div/div[1]').click()
        time.sleep(2)

    def quitBrowser(self):
        self.driver.close()  

    def answerFrage(self, grains, elapsed):
        while True:
            full = self.driver.find_element_by_class_name('card-title').text
            split = full.split() 

            self.compare_lst.append(split)

    
            if len(split) == 0:
                continue
            else:
                a = int(split[0])
                b = int(split[-1])
                answer = a * b

            

            try:
                if answer == int((self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div')).text):                                                
                    try:
                        self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[2]/div').click()   
                    except:
                        
                        continue                         
                elif answer == int((self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[3]/div')).text):
                    try:
                        self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[3]/div').click()
                        
                    except:
                      
                        continue
                elif answer == int((self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[4]/div')).text):
                    try:
                        self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[4]/div').click()
                      
                    except:
                      
                        continue
                else:
                    try:
                        self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[5]/div').click()
                       
                    except:
                        
                        continue              
                
                time.sleep(1.3)
                break
                

            except ValueError:
                pass

    

gov_id = ""  #last four digits of social
grains = 0
start = time.time()
rb = RiceBot()

while True:
    try:
        grains+=10
        end = time.time()
        elapsed = round((end - start)/60, 2)

        rb.answerFrage(grains, elapsed)

        
    except Exception as e:
        try:
            rb.quitBrowser()
            rb.openBrowser()
            start = time.time()
        except Exception as p:
            rb.openBrowser()
            start = time.time()

        grains = 0
    
    if elapsed >= 240:
        rb.quitBrowser()
        rb.openBrowser()
        grains = 0
        start = time.time()

        
