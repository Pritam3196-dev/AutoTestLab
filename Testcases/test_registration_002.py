"""

This is the file for registration testcase where we write the testcase result


"""

import time
import pytest
import allure
from PageObjects.registrationpage import registration_page_class
from faker import Faker
from Utilities.Readproperties import ReadConfigClass
# import ReadConfigClass from Readproperties.py
from Utilities.logs import logs_generator_class

# import class from registrationpage


# use browser setup fixture method of conftest.py .
# Use at class level instead of method(testcase)
#becuase we defined there (conftest.py) @pytest.fixture(scope='class')
# because we use driver from that file because open and close browser code write there

@pytest.mark.usefixtures('browser_setup')  # use fixture code at class level instead of testcase level
class Test_register:

    driver = None
    faker = Faker()
    name_value = faker.user_name()
    email_value = faker.email()
    #password_value = 'Radheshyam@123'
    # create object of calling the method of logs file
    log = logs_generator_class.logs_generator_method()

    # allure decorators # that showcase in allure reports

    @allure.title('test_registration_002')
    @allure.severity(allure.severity_level.NORMAL)  # while executing testcase how important is that respective testcase
    @allure.epic('Credkart : User Registration')  # epic name in Jira
    @allure.story('validate user register of credkart')
    @allure.description('Validating registration functionality of credkart app')
    @allure.issue(ReadConfigClass.get_registration_url(), 'user registration')
    @allure.link(ReadConfigClass.get_registration_url())

    @pytest.mark.smoke # smoke markers
    @pytest.mark.flaky(reruns=2 , rerun_delay = 1)  # rerun failure
    #@pytest.mark.dependency(depends=['test_verify_credkart_url_001'])
    @pytest.mark.order(5)
    def test_register_002(self):

        self.log.info('Testcase test_register_002 is starting ....')

        self.log.info(f'Opening browser and getting {ReadConfigClass.get_registration_url()}')
        self.driver.get(ReadConfigClass.get_registration_url())
        # use self.driver because by self we can use variable in another method
        self.log.info(f'Checking the driver title ..... {self.driver.title}')
        if self.driver.title == 'CredKart':


            # now we need to create class object which is defined in registrationpage.py file

            r = registration_page_class(self.driver)

            # we create object of class where we gave self.driver(this is driver)
            # to driver argument of constructor

            # Now we can call the methods now

            self.log.info('Entering name....')

            r.name_element(self.name_value)

            # name_value is the value to name argument of name_element method

            self.log.info('Entering email')

            r.email_address_element(self.email_value)

            self.log.info('Entering password')

            r.password_element(ReadConfigClass.get_password())

            # By using class name call the get_password method from reProperties.py

            self.log.info('Entering confirm password')

            r.confirm_password_element(ReadConfigClass.get_password())

            # we use self because this variables are not defined in this methods
            # there area are too restricted so if we want to use this variables
            # in another methods so we need to use self

            self.log.info('CliKing register button ....')
            r.register_button() # we call the register button method



            # now after click register button
            # we call the demo button method to check is that register pass or fail

            if r.demo_button_visible() == 'pass':

                self.log.info('Taking screenshot when testcase test_register_002 is passing')

                self.driver.save_screenshot(f'.\\Screenshots\\registration_pass_{self.email_value}.png')
                allure.attach.file(f'.\\Screenshots\\registration_pass_{self.email_value}.png' , attachment_type = allure.attachment_type.PNG)
                self.log.info('Testcase test_register_002 is passed')
                assert True

            else:

                self.log.info('Taking screenshot when testcase test_register_002 is failing')
                self.driver.save_screenshot(f'.\\Screenshots\\registration_fail_{self.email_value}.png')
                allure.attach.file(f'.\\Screenshots\\registration_fail_{self.email_value}.png' , attachment_type = allure.attachment_type.PNG)
                self.log.info('Testcase test_register_002 is failing')
                assert False , "Registration Failed"

            self.log.info('Testcase test_register_002 is completed')











