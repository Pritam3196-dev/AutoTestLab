"""

This is the file for registration testcase where we write the testcase result


"""

import time
import pytest
import allure
from PageObjects.registrationpage_inheritance import registration_page_class_inheritance
from faker import Faker
from Utilities.Readproperties import ReadConfigClass
from Utilities.logs import logs_generator_class
from PageObjects.registrationpage_inheritance import registration_page_class_inheritance


# import class from registrationpage_inheritance


# use browser setup fixture method of conftest.py .
# Use at class level instead of method(testcase)
#becuase we defined there (conftest.py) @pytest.fixture(scope='class')
# because we use driver from that file because open and close browser code write there

@pytest.mark.usefixtures('browser_setup')  # use fixture code at class level instead of testcase level
class Test_register_inheritance:

    # Here we create object of child class(registration class) and by using that
    # we access parent class methods and properties
    # email , password , demo button , constructor

    driver = None
    faker = Faker()
    #
    # name_value = faker.user_name()
    # email_value = faker.email()
    # #password_value = 'Radheshyam@123'
    logs = logs_generator_class.logs_generator_method()
    # This is the object of method called by class name

    # allure decorators # use in allure reports
    @allure.title('test_register_003_by-inheritance')
    @allure.severity(allure.severity_level.NORMAL) # how important is that testcase
    @allure.epic('Credkart : User registration Inheritance')
    @allure.link(ReadConfigClass.get_registration_url())
    @allure.issue(ReadConfigClass.get_registration_url() , 'User registration')
    @allure.story('Validate registration of credkart application')
    @allure.description('Validate registration of credkart application')
    @pytest.mark.smoke # smoke markers
    @pytest.mark.flaky(reruns=2 , rerun_delay =1)
    #@pytest.mark.dependency(depends=['test_verify_credkart_url_001'])
    @pytest.mark.order(4)
    def test_register_003(self):

        self.logs.info('Testcase test_register_003 is starting ....')

        # info is basically use for print message . which we defined in log_format
        # INFO is for set log level

        # log is object of calling method
        # self is allow to use this variable / object in another method
        # by using self variable we can access the methods and variables of class


        self.logs.info(f'Opening the browser and getting {ReadConfigClass.get_registration_url()}')

        self.driver.get(ReadConfigClass.get_registration_url())

        # By using class name we call the registration_url method


        # use self.driver because by self we can use variable in another method


        self.logs.info(f'Checking the title of driver is ...... {self.driver.title}')

        if self.driver.title == 'CredKart':


            # now we need to create class object which is defined in registrationpage_inheritance.py file

            # This is the create object of registration class where parent class login
            # inherited . so by using that object we can access the entire parent class
            r = registration_page_class_inheritance(self.driver)

            # we create object of class where we gave self.driver(this is driver)
            # to driver argument of constructor


            self.logs.info('Generating fake username .....')
            name_value = self.faker.user_name()
            self.logs.info('Generating fake email.....')
            email_value = self.faker.email()


            # Now we can call the methods now

            self.logs.info('Entering the name ....')

            r.name_element(name_value)  # This is child class own method

            # name_value is the value to name argument of name_element method

            self.logs.info('Entering the email ....')

            r.email_address_element(email_value)  # This is the method of parent class

            self.logs.info('Entering the password ....')
            r.password_element(ReadConfigClass.get_registration_password())
            # This is the method of parent class
            # This is the value of password which get from by calling method of
            # Readproperties.py (which is defined in config.ini (password_value))

            self.logs.info('Entering the confirm password ....')
            r.confirm_password_element(ReadConfigClass.get_registration_password()) # This is child class own method

            # we use self because this variables are not defined in this methods
            # there area are too restricted so if we want to use this variables
            # in another methods so we need to use self

            self.logs.info('CliKing the register button')

            r.register_button() # we call the register button method

            self.logs.info('Registration Successful ....')

            # so we just called it by using child class object. we not create explicitly

            self.logs.info('ClicKing menu button ....')

            # This is also method of parent class

            if r.verify_menu_button_visibility() == 'pass':

                self.logs.info('Registration Successful')

                self.logs.info('Taking screenshot when testcase test_register_003 passing')
                self.driver.save_screenshot(f'.\\Screenshots\\register_inheritance_test_case_{ReadConfigClass.get_email()}_pass.png')

                allure.attach.file(f'.\\Screenshots\\register_inheritance_test_case_{ReadConfigClass.get_email()}_pass.png' , attachment_type = allure.attachment_type.PNG)

                # self.driver.find_element(By.XPATH , p.menu_button_xpath).click()
                self.logs.info('CliKing on menu button ...')
                r.menu_button()  # menu button click
                self.logs.info('CliKing on logout button....')
                r.logout_button()  # logout button click
                self.logs.info('Logout Successful....')

                self.logs.info('Testcase test_register_003 is passed')
                assert True



            else:
                self.logs.info('registration failed')
                self.logs.info('Taking testcase test_register_003 failing')
                self.driver.save_screenshot(f'.\\Screenshots\\registration_test_case_{ReadConfigClass.get_email()}_fail.png')
                allure.attach.file(f'.\\Screenshots\\registration_test_case_{ReadConfigClass.get_email()}_fail.png' , attachment_type = allure.attachment_type.PNG)
                self.logs.info('Testcase test_register_003 is failed')

                assert False, 'register Failed'

            self.logs.info('Testcase test_register_003 completed ....')




"""
        We will use a menu button of parent class

            # now after click register button
            # we call the demo button method to check is that register pass or fail

            if r.demo_button_visible() == 'pass':

                self.driver.save_screenshot(f'.\\Screenshots\\registration_pass_{self.email_value}.png')
                assert True

            else:

                self.driver.save_screenshot(f'.\\Screenshots\\registration_fail_{self.email_value}.png')
                assert False , "Registration Failed"

"""










