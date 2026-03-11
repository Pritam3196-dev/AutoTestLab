"""

As we talked about ,loginpage.py where we create browser actions of loginpage
same in registrationpage.py where we create selenium / browser actions of registration
page . because in pageobjects . it is python package so it contains python code
In testcases only trstcases results will there .

# In registration page we have ,

# Name
# Address
# Password
# Confirm Password

so first of all we define the locators value of this , because in future if UI changes
then locators value will also change so if need to change it so no need to change code
of testcases file . it can easily change here


"""
import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Here intentionally create this file because we want to perform inheritance
# because login page and registration page has some same features like
# email , password , demo button(after login) and we use constructor login page also
# so that's why we inherit the parent class (login class) into child class (registration class)
# we create object of child class and inherit the properties of parent class


# we need to import login page class here test_registration_002

from PageObjects.loginpage import login_page_class

class registration_page_class_inheritance(login_page_class):
      # child class                      # parent class

    # we take some features from loginpage.py . which is same on registration page
    # when we use inheritance . now we can access all the properties of parent class
    # so no need to inherit constructor explicitly
    # because if we re not created constructor of child class then it can access it
    # by default




    Name_id = 'name'
    #email_address_id = 'email'  # we access this two things of parent class
    #password_id = 'password'
    confirm_password_id = 'password-confirm'
    register_button_xpath = '//button[@type= "submit"]'
    demo_button_xpath = "//a[@role='button']"


    def name_element(self , name):

        self.driver.find_element(By.ID , self.Name_id).send_keys(name)
        # name is parameter /argument where we call that method when after object creation
        # of class that time pass argument to the method




    def confirm_password_element(self , confirm_password):

        self.driver.find_element(By.ID , self.confirm_password_id).send_keys(confirm_password)

    def register_button(self):

        self.driver.find_element(By.XPATH, self.register_button_xpath).click()



    # we create function where demo button is visible or not ?
    # we call that method in testcase folder and compare there result










    # Now all elements locators are mentioned correctly
    # now need to call define the methods of this element for finding the
    # locations on web page (registration) we call this methods after creating class
    # object in testcase folder


"""
    This we hide constructor because we use of parent class constructor  
    #
    # def __init__(self , driver): # This is the constructor . we defined it for when we
    #     # create the class object in login_testcase.so we can call methods of this class
    #     # in testcase
    #     self.driver = driver


        # self is the variable which access instance variable and instance method
        # by using self , we can use the method and variable in another method
        # we use self.driver instead of driver
        # we use all locators variable by self in another method
        # apart of constructor if want to use driver then always use with self

"""






"""
     This data we comment it because we import that email and password and constructor from
     login page class


    # 
    # def  email_address_element(self , email):
    # 
    #     self.driver.find_element(By.ID , self.email_address_id).send_keys(email)

    # 
    # def password_element(self , password):
    # 
    #     self.driver.find_element(By.ID , self.password_id).send_keys(password)
  

"""






    # now we need to think about after registration what will happen

    # There are two possibilities
       # 1.registration success (Then redirected to next page where demo button is there)
       # 2.registration failed (stuck on same page)

    # If success then demo button so here we check is that demo button is displayed or not
    # it is browser action so do it in same file only
    # but if not then selenium not got the element (demo button) then raised error
    # so we need to write that code in try and except block for avoiding error
    # and raise exception of register fail

"""
    we use This menu button of parent class 

    # we create function where demo button is visible or not ?
    # we call that method in testcase folder and compare there result

    def demo_button_visible(self):

        try:

            wait = WebDriverWait(self.driver , 30)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH , self.demo_button_xpath)))
            return "pass"

        except:

            return "fail"

"""













