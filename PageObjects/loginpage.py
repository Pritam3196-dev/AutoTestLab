"""

This page objects is basically for to write code for selenium actions in browser.
means whatever actions happened on browser that write in pageobjects.
because in future any UI change of your application then locators are changed
so no need to change in testcase file . we need to change only in pageobjects folder

In pageobjects folder ,

we always created loginpage.py file . where we write selenium / browser actions
on browser

If your web application have login page then always create loginpage.py in pageobjects

In our application login page has elements

1.Email
2.Password
3.Login button
After login button if login pass then
4.Menu button
5.logout button

so we need to define there locators value first because in future if any change in UI then
locators value will change easily

"""

import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Utilities.logs import logs_generator_class





class login_page_class:

    # Here we define locators value of element which is present in login page
    email_address_xpath = "//input[@id='email']"
    password_id= 'password'
    login_button_xpath = "//button[@type='submit']"
    menu_button_xpath = "//a[@role='button']"
    logout_button_xpath = "//a[normalize-space()='Logout']"
    log = logs_generator_class.logs_generator_method()


    def __init__(self , driver): # This is the constructor . we defined it for when we
        # create the class object in login_testcase.so we can call methods of this class
        # in testcase
        self.driver = driver # driver is argument which gives value when object is creation of class
                             # and assign that driver value to self.driver
        # self is by default variable in constructor and instance method
        # self is always pointing to current object so by using self we can access
        # instance method and variables of class . so here if want to access
        # or use driver variable in another methods of same class then self.driver
        # because driver is restricted for only constructor area . apart of constructor
        # if want to use driver then self.driver



    # now as per our discussion we need to create browser actions of login page
    # here we create methods of browser actions so we called that methods in login testcase
    # by object created of class

    def email_address_element(self , email_address):  # email is an argument where we gave value at time of call that method


        wait = WebDriverWait(self.driver , 10)
        self.log.info('Email Address element found out')
        email_add = wait.until(expected_conditions.visibility_of_element_located((By.XPATH , self.email_address_xpath)))
        email_add.send_keys(email_address)


        #self.driver.find_element(By.XPATH , self.email_address_xpath).send_keys(email_address)


        # self is give access of another instance method or by using self
        # we can use variable in another method
        # self give access of instance variable and method
        # driver in constructor by using self we can use in email_address method
        # email_address_id is out of all methods but by self we can access it in email_address method

    def password_element(self,password):

        self.driver.find_element(By.NAME , self.password_id).send_keys(password)


    def login_button(self):

        self.driver.find_element(By.XPATH , self.login_button_xpath).click()




    def menu_button(self):

        self.driver.find_element(By.XPATH , self.menu_button_xpath).click()


    def logout_button(self):

        self.driver.find_element(By.XPATH , self.logout_button_xpath).click()


        # self is give access / by using self we can use the variables in another methods
        # in class where it has no access by just variable name


    # Here we verify is that login happened or not because in testcase folder only testcase
    # results where write other all browser activities in pageobjects.
    # we verify is that login happened or not . that is part of selenium actions


    def verify_menu_button_visibility(self):

        try:

            wait = WebDriverWait(self.driver,20)

            wait.until(expected_conditions.visibility_of_element_located((By.XPATH , self.menu_button_xpath)))
            #self.driver.find_element(By.XPATH , self.menu_button_xpath)
            self.log.info('menu button is visible')

            return "pass"

        except:


            #self.log.info('menu button is not visible....')
            return "fail"



        #Here we defined that code where selenium / browser actions happened in login page
        # so testcase result and screenshots in testcase folder









