"""

Testcases :

1.Login
2.Registration
3.Checkout
4.Amount verification
5.Login_with_paramas (take test data for login from conftest.py)
6.Login_with_excel  (take test data for login from excel)
7.Registration_with_params
8.Registration_with_excel

Mostly smoke and sanity testcases are make automate
because on daily basis it came

sanity : After fixed bug , check is that really fixed or not ?
smoke : when new build received , check is that stable before detail level testing
        means check is that major functionalities / features are really worked before
        detail level testing
"""
import time
import selenium
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from PageObjects.loginpage import login_page_class
from Utilities.Readproperties import ReadConfigClass
from Utilities.logs import logs_generator_class
from Utilities.utilities_Excel import excel_method




@pytest.mark.usefixtures('browser_setup')  # This line says use fixture function browser_setup
                          # at class level not at testcase level so use for whole class
class Test_user_profile:

    driver=None
    log = logs_generator_class.logs_generator_method()
    # This is the object of calling the method by classname



    #excel_path = '.\\Desktop\\login_credentials.xlsx'
    excel_path = 'C:\\Users\\Lenovo\\OneDrive\\Desktop\\login_credentials.xlsx'
    sheet_name = 'login_data'

    @allure.title('test_verify_login_excel_005_(verify_login_by_excel)')
    @allure.severity(allure.severity_level.CRITICAL)  # while executing testcase how important is that respective testcase
    @allure.epic('Credkart : User login') # epic name in Jira
    @allure.story('validate login of credkart')
    @allure.description('Validating login functionality of credkart app')
    @allure.issue(ReadConfigClass.get_login_url() , 'user loin')
    @allure.link(ReadConfigClass.get_login_url())
    @pytest.mark.smoke   # smoke markers
    @pytest.mark.flaky(reruns=2 , rerun_delay=2)  #rerun failure
    #@pytest.mark.dependency(depends = ['test_verify_credkart_url_001'])
    @pytest.mark.order(3)
    def test_verify_login_excel_005(self):



        #driver = webdriver.Chrome()
        #driver.maximize_window()
        #driver = browser_setup # this is the method where we write driver code
        # it all return driver things / properties to function so indirectly here

        self.log.info('Testcase test_verify_login_excel_005 is starting....')

        self.log.info(f'Opening the browser and getting {ReadConfigClass.get_login_url()}')
        self.driver.get(ReadConfigClass.get_login_url())
        # By using class name we access the login_url method
        # we replace hardcoded url



        # test login feature

        # 1.E-Mail address
        # 2.Password

        #email_value = 'credUser_1447@gmail.com'
        #password_value = 'credUser_1447'

        self.log.info(f'Checking the driver title {self.driver.title}')

        if self.driver.title == 'CredKart':


            p = login_page_class(self.driver)
            # This is object of loginpage.py file class . which perform selenium action there

            # now we create for loop to perform that no of iterations exactly
            # equal to no of columns in excel file
            # if 4 rows then 4 iterations
            # because we read the data from every line so we need to create that no of
            # iterations

            rows = excel_method.get_rows(self.excel_path , self.sheet_name)
            # when call this method . so that method return max rows of excel file

            testcase_result = []

            self.log.info('Sub testcases are starts ....')
            for i in range(2 , rows+1): # excel file contains very 1st row have headers


                self.driver.get(ReadConfigClass.get_login_url())
                # we write this again because when very first test enter credentials
                # after that if it is fail then ok .then come back for next testcase
                # in loop then still driver on same page so it enter credentials
                # but when credentials are wrong login pass then it goes on
                # landing page so then come to next iteration that time
                # driver on same page so that driver/selenium not get
                # email and password field . because that page is not login page
                # so we mention this line again
                # when new iteration/testcase then again login page will load
                # irrespective previous result

                #first read the data . so call the read method so that method return
                #data

                email = excel_method.read_excel(self.excel_path , self.sheet_name , i , 2)
                password = excel_method.read_excel(self.excel_path , self.sheet_name , i , 3)
                expected_result = excel_method.read_excel(self.excel_path , self.sheet_name , i , 4)
                #actual_result = excel_method.read_excel(self.excel_path , self.sheet_name , i , 5)


                self.log.info(f'Entering the email address.... {email} ')
                p.email_address_element(email)

                # here we call email_address_element method and email is argument
                # by class object p

                self.log.info(f'Entering the password.... {password}')
                p.password_element(password)

                #call the get_password() method

                # we call password_element method and argument is password

                self.log.info('Clicking login button')
                p.login_button()


                # we call login_button method
                self.log.info('Checking login status ')

                #print(f'login pass or fail :  {p.verify_menu_button_visibility()}')
                self.log.info(p.verify_menu_button_visibility())

                if p.verify_menu_button_visibility() == 'pass':

                    actual_result = "pass"

                    self.log.info('Write actual in excel file ....')

                    excel_method.write_excel(self.excel_path , self.sheet_name , i , 5  , actual_result)


                    self.log.info('Login Successful')


                    self.driver.save_screenshot(f'.\\Screenshots\\login_pass_{email}.png')
                    allure.attach.file(f'.\\Screenshots\\login_pass_{email}.png' , attachment_type = allure.attachment_type.PNG)

                    self.log.info('CliKing on menu button ...')
                    p.menu_button() # menu button click
                    self.log.info('CliKing on logout button....')
                    p.logout_button() # logout button click
                    self.log.info('Logout Successful....')
                    self.log.info('*' * 20)
                    assert True



                else:


                    actual_result = "fail"
                    self.log.info('Login failed')
                    self.log.info('Write actual result in excel file.....')
                    excel_method.write_excel(self.excel_path , self.sheet_name , i , 5 , actual_result)
                    self.driver.save_screenshot(f'.\\Screenshots\\login_fail_{email}.png')
                    allure.attach.file(f'.\\Screenshots\\login_fail_{email}.png' , attachment_type = allure.attachment_type.PNG)
                    self.log.info('*' * 20)


                    #assert False , 'Login Failed'


                if expected_result == actual_result:  # pass == pass / fail==fail

                    result = "pass"  # when actual == expected then .if actual = 'pass' , expected = 'pass' both are same
                                     # when actual = 'fail' and expected = 'fail' . then actual == expected then 'pass'

                    testcase_result.append(result)
                    self.log.info('Write testcase result in excel file ....')
                    excel_method.write_excel(self.excel_path , self.sheet_name , i , 6 ,result)

                else:
                    result = 'fail'  # when actual = fail and expected = 'pass' then both are different so 'fail'

                    testcase_result.append(result)
                    self.log.info('Write testcase result in excel file ....')
                    excel_method.write_excel(self.excel_path , self.sheet_name , i , 6 , result)


            print(f'Testcase result is : {testcase_result}')
            if 'fail' in testcase_result:

                self.log.info('Entire testcase test_verify_login_excel_005 is failed')
                assert False

            else:

                self.log.info('Entire testcase test_verify_login_excel_005 is passed')




            self.log.info('Testcase test_verify_login_002 is completed....')



