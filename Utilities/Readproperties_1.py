"""

This file is created for read the data from config.ini
we create methods to read it



"""

# read the ini file by using configparser module

import configparser

config = configparser.RawConfigParser()

# Then read the file  by config

config.read('.\\configurations\\config.ini')

# we are reading config file by python file

# Now create class for reading (creation of methods)

class ReadConfigClass_1:


    # Now we need to create method for returning value of hardcoded objects
    # which is written in ini file


    # first of all we read email

    @staticmethod  # Staticmethod : no need to create objects of class to call methods
    def get_email_1():

        return config.get('login_data' , 'email')
        # return email value (option) of ini file of login_data (section)


    @staticmethod
    def get_password_1():

        return config.get('login_data' , 'password')

    @staticmethod
    def get_login_url():

        return config.get('url' , 'login_url')

    @staticmethod
    def get_registration_url():

        return config.get('url' , 'registration_url')

    @staticmethod
    def get_registration_password():

        return config.get('registration data' , 'registration_password')



    # so these methods called by using class name (ReadConfigClass_1)
    # at email , password in login page
    # and at registration page (registration_password , registration_url) (testcases folder)





