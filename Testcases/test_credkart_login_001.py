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




@pytest.mark.usefixtures('browser_setup')  # This line says use fixture function browser_setup
                          # at class level not at testcase level so use for whole class
class Test_user_profile:

    driver=None
    log = logs_generator_class.logs_generator_method()
    # This is the object of calling the method by classname

    @allure.title('test_verify_credkart_url_001')  # mention title of testcase in allure report
    @allure.epic("Epic : verify User Profile")  # epic of jira
    @allure.description("This testcase is design for to verify url of credkart application....")
    @allure.issue('https://automation.credence.in/shop', 'verify url of credkart')
    @allure.link('https://automation.credence.in/shop')
    @allure.severity(allure.severity_level.CRITICAL)  # To check severity level of testcase means how testcase is to you like normal , critical
    @allure.story('Validate url of credkart app')
    @pytest.mark.smoke   # markers
    @pytest.mark.flaky(reruns=2 , rerun_delay=1)  # failure rerun
    @pytest.mark.dependency(name = 'test_verify_credkart_url_001')
    @pytest.mark.order(1) # order marker for put order of execution (but not in parallel run)
    def test_verify_credkart_url_001(self):   # testcase where verify url of credkart app


        #driver = webdriver.Edge() # invoke chrome browser object
        #driver.maximize_window()    # maximize the browser window

        # self.log.info('This is info log level')
        # self.log.debug('This is debug log level')
        # self.log.warning('This is warning log level')
        # self.log.error('This is the error log level')
        # self.log.critical('This is the critical log level')

        self.log.info('Testcase test_verify_credkart_url_001 is starting....')


        self.log.info(f'Opening the browser and getting {"https://automation.credence.in/shop"}')
        self.driver.get('https://automation.credence.in/shop')  # read the url

        self.log.info(f'Checking Title of driver.... {self.driver.title}')
        if self.driver.title == 'CredKart':   # verify that title of page where driver is present

            self.log.info('Taking screenshot when testcase test_verify_credkart_url_001 passing')

            self.driver.save_screenshot('.\\Screenshots\\test_verify_credkart_url_pass_001.png')
            allure.attach.file('.\\Screenshots\\test_verify_credkart_url_pass_001.png' , attachment_type = allure.attachment_type.PNG)

            self.log.info('Testcase test_verify_credkart_url_001 is passed')

            #screenshot of pass url
        else:

            self.log.info('Taking screenshot when testcase test_verify_credkart_url_001 failing')

            self.driver.save_screenshot('\\.Screenshots\\test_verify_credkart_url_fail_001.png')

            self.log.info('Testcase test_verify_credkart_url_001 is failed')
            assert False


        self.log.info('Testcase test_verify_credkart_url_001 is completed....')



        # To check testcase is pass or fail
        # pytest -v -s --html=Html_reports/my_report.html

    @allure.title('test_verify_login_002')  # mention title of testcase in allure report
    @allure.epic("Epic : verify User Profile")  # epic of jira
    @allure.description("This testcase is design for to verify login of credkart application....")
    @allure.issue(ReadConfigClass.get_login_url(), "user login")
    @allure.link(ReadConfigClass.get_login_url())
    @allure.severity(allure.severity_level.CRITICAL)  # To check severity level of testcase means how testcase is to you like normal , critical
    @allure.story('Credkart : User login')

    @pytest.mark.smoke  # markers
    @pytest.mark.flaky(reruns=2 , rerun_delay=1)  # rerun failures . after testcase fail run for 2 times
    #@pytest.mark.dependency(depends = ['test_verify_credkart_url_001']) # This is the creation of dependency when dependency
    # testcase fail another testcase will not run
    @pytest.mark.order(2)   # order marker for put order of execution (but not in parallel run)
    def test_verify_login_002(self):



        #driver = webdriver.Chrome()
        #driver.maximize_window()
        #driver = browser_setup # this is the method where we write driver code
        # it all return driver things / properties to function so indirectly here

        self.log.info('Testcase test_verify_login_002 is starting....')

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

            # Here we create object of login_page_class and we pass self.driver to driver
            # argument to constructor
            # we give self.driver because driver defined in conftest.py we take it at class level
            # By @pytest.mark.usefixtures(--browser_setup)
            # so driver there we use here that driver by self.driver so we gave self.driver
            # as value so driver contains all properties of driver of conftest.py


            # now successfully created object of class now we call it that methods
            # because in this method we need to determine testcase pass or fail
            # it is about testcases so we call it and then make it login if
            # expected result and actual result match then pass

            self.log.info('Entering the email address.... ')
            p.email_address_element(ReadConfigClass.get_email())
            # By using class name call get_email() method which return email_value

            # here we call email_address_element method and email_value to email argument
            # by class object p

            self.log.info('Entering the password....')
            p.password_element(ReadConfigClass.get_password())

            #call the get_password() method

            # we call password_element method and password_value to argument password

            self.log.info('Clicking login button')
            p.login_button()

            # we call login_button method
            self.log.info('Checking login status ')

            if p.verify_menu_button_visibility() == 'pass':

                self.log.info('Login Successful')

                self.log.info('Taking screenshot when testcase test_verify_login_002 passing')
                self.driver.save_screenshot(f'.\\Screenshots\\login_test_case_{ReadConfigClass.get_email()}_pass.png')
                allure.attach.file(f'.\\Screenshots\\login_test_case_{ReadConfigClass.get_email()}_pass.png' , attachment_type = allure.attachment_type.PNG)
                #self.driver.find_element(By.XPATH , p.menu_button_xpath).click()
                self.log.info('CliKing on menu button ...')
                p.menu_button() # menu button click
                self.log.info('CliKing on logout button....')
                p.logout_button() # logout button click
                self.log.info('Logout Successful....')

                self.log.info('Testcase test_verify_login_002 is passed')
                assert True



            else:
                self.log.info('Login failed')
                self.log.info('Taking testcase test_verify_login_002 failing')
                self.driver.save_screenshot(f'.\\Screenshots\\login_test_case_{ReadConfigClass.get_email()}_fail.png')
                self.log.info('Testcase test_verify_login_002 is failed')

                assert False , 'Login Failed'

            self.log.info('Testcase test_verify_login_002 is completed....')



            #
            # #
            # # #wait = WebDriverWait(self.driver, 10)
            # # #email = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//input[@id = "email"]')))
            # #
            # # #email = driver.find_element(By.XPATH , '//input[@id = "email"]')
            # # email.send_keys(email_value)
            #
            # # tag_name : input
            # # attribute : id
            # # value : email
            #
            # password = self.driver.find_element(By.XPATH , '//input[@id = "password"]')
            # password.send_keys(password_value)
            #
            # # checkbox
            # remember_me = self.driver.find_element(By.XPATH , '//input[@type = "checkbox"]')
            # remember_me.click()
            #
            # assert remember_me.is_selected() , 'Not selected'
            #
            # # Login button
            #
            # login_btn = self.driver.find_element(By.XPATH , '//button[@type = "submit"]')
            # login_btn.click()
            #
            # # How to verify the testcase is pass or fail ?
            # # for that reason we take text after login
            #
            # try:
            #     login_text = self.driver.find_element(By.XPATH , '/html[1]/body[1]/div[1]/div[1]/p[1]')
            #     print(f'Login text case : {login_text.text}')
            #
            #     self.driver.save_screenshot('.\\Screenshots\\test_verify_login_pass_002.png')
            #
            #     # when login successful then logout
            #
            #     logout_toggle = self.driver.find_element(By.XPATH , '//a[@class ="dropdown-toggle"]')
            #     logout_toggle.click()
            #
            #     # now click on logout
            #
            #     logout = self.driver.find_element(By.XPATH , '//a[@href="https://automation.credence.in/logout"]')
            #     logout.click()
            #
            #     print('Logout Successful')
            #
            #     self.driver.save_screenshot('.\\Screenshots\\test_verify_logout_pass_002.png')
            #
            #
            # except:
            #
            #     print('Login Failed')
            #     self.driver.save_screenshot('.\\Screenshots\\test_verify_login_fail_002.png')
            #     assert False
