"""
This is the file is created for to execute / write the code before testcase execute
and after testcase execute means invoke the browser and quit the browser

"""
import pytest
from selenium import webdriver

# right now we work on automated command line to pytest for opening the testcase
# in given command line argument(browser) so for that reason we need to introduce
# --browser (command line argument to pytest) for that reason this method is write

# we use hookup function (pytest_addoption) .
# This function is used to pass command line argument to pytest
# It is customize or user defined argument


def pytest_addoption(parser):  # parser : to add command line argument(--browser)

    parser.addoption('--browser')  # This line says adding the command line argument to
                                   # pytest


# we introduce command line argument ('--browser') to pytest but it just argument till
# value is not assigned to argument (--browser=chrome)
# till browser value is not assigned like chrome , firefox , edge, headless
# so need to assign the value so thats why this function is written



@pytest.fixture(scope='class')  # This line code says we defined that fixture function there
                                # scope is at class level means we will use that browser_setup
                                # at class level (in testcases class)
def browser_setup(request):            # request is argument

    browser = request.config.getoption('--browser')   # This line of code says
                         # it returns the value which value given by end user while in command
                         # like chrome , firefox , edge , headless , safari
                         # This line says it is ask to pytest what is value/ browser name given by end user while
                         # in command line (chrome , firefox , edge , headless , safari)
                         # browser is reference variable
                         # request.config.getoption('--browser') returns the which browser value given
                         # by end user


    if browser == 'chrome':

        driver = webdriver.Chrome()

    elif browser == 'firefox':

        driver = webdriver.Firefox()

    elif browser == 'edge':

        driver = webdriver.Edge()

    elif browser == 'headless':

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver=webdriver.Chrome(options=chrome_options)

    else:

        driver=webdriver.Chrome()


    driver.maximize_window()

    request.cls.driver=driver  # attaching driver to main class

    yield driver # return driver(all properties of driver) to fun/method

    driver.quit()






# when html report generation

# 1.Environment report(Metadata)
# 2.Based on testcases


# we want to edit the Environment report / metadata report

def pytest_metadata(metadata): # metadata is argument

    # Add metadata in html report
    metadata["project_name"] = "CredKart Test Automation"
    metadata["Environment"] = "QA Environment"
    metadata['tester'] = "Credence"

    # delete metadata in html report
    del metadata['Platform']





# basically we're changing the metadata of project report where we add the project name ,
# Environment , tester and we delete the platform of the project









