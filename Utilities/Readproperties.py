"""

This is the file basically created for to read the config file [Hardcoded] data


"""

import configparser  # This is the import configparser module


# we need to read the file for that reason we need to import the configparser module


config = configparser.RawConfigParser()  # from configparser we access RwaConfigParser
# method

config.read('.\\Configurations\\config.ini')


# This line of code says config read the file from that location


class ReadConfigClass:

    @staticmethod # staticmethod : There is no need of object creation of this class
    def get_email(): # by using class name can access the class methods

        return config.get("login data" , "email_value")
        # This return the value of email_value to method

    @staticmethod
    def get_password():

        return config.get('login data' , 'password_value')

    @staticmethod
    def get_login_url():

        return config.get('urls' , 'login_url')

    @staticmethod
    def get_registration_url():

        return config.get('urls' , 'registration_url')
                          #section    # respective variable/option

    @staticmethod
    def get_registration_password():

        return config.get('registration_data' , 'registration_password_value')






# now we are able to read the data of config.ini file
# now we call this methods in respective testcases



