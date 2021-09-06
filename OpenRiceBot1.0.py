'''
Welcome to Open Rice Bot. We are glad you joined our mission to bankrupt the United Nations und den Welthunger enden!

Join our group using code 5DLN5PAE
https://freerice.com/groups 

To run: 
    -download FireFox
    -download GeckoDriver and add to PATH
    -pip install selenium
    -enter username, password, and last 4 digits of your social when prompted :)

This bot currently runs the multiplication table category.
Storing answers in lists and dictionaries would enable it to run different categories (English Grammar would be simple).
Could add the ability for users to input desired category at beginning of session.

Goal is to build a standalone executable file that is downloaded in package containing all necessary files (and will automatically add itself to PATH if necessary)
'''


from logging import raiseExceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




print("Welcome to Open Rice Bot\n\n")   #maybe some ascii art of rice and robots :)
username = input("Please enter your freerice.com username: ")
password = input("Please enter your password: ")
gov_id = input("Please enter last four digits of your social security number: (y/n)")
headless = True


#username = "Frau_Gygax"
#password ="mehrdeutsch"



class RiceBot:
    def __init__(self):
        self.compare_lst = []
        self.openBrowser()

    def openBrowser(self):
        self.options = webdriver.FirefoxOptions()

        if headless == True:
            self.options.add_argument("--headless")
        
        self.driver = webdriver.Firefox(options=self.options)  

        self.driver.implicitly_wait(2)     

        self.driver.get("https://freerice.com/profile")

        time.sleep(0.5)

        self.driver.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div[2]/button").click()


        login_username = self.driver.find_element_by_id("login-username")
        login_username.clear()
        login_username.send_keys(username) #Your username


        login_password = self.driver.find_element_by_id("login-password")
        login_password.clear()
        login_password.send_keys(password) #Your Password 

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

    def joinGroup(self):
        time.sleep(0.5)
        self.driver.find_element_by_class_name('toolbar__menu-toggle-icon').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div/nav/div/nav/ul/li[5]/div/a').click()

        group_code = self.driver.find_element_by_id("group-code")
        group_code.clear()
        group_code.send_keys("5DLN5PAE")
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div/div[2]/div/div[3]/div[3]/div/button').click()
        time.sleep(5)
        



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
                
                time.sleep(2)
                break
                

            except ValueError:
                pass

    

grains = 0
start = time.time()
rb = RiceBot()


#rb.joinGroup()





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


