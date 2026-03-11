"""

This file is created for to make logs by python code
The code is creating the logs
Logs : Track down the process of your functionality (of testcases)
       from scratch during automation

       eg : from starting executing the testcase upto completion of testcases
       eg : Login testcase : 1.Start the testcase
                             2.Get the url
                             3.Open the browser
                             4.Enter the email
                             5.Enter the password
                             6.click on login button
                             7.Testcase pass
                             8.Complete the testcase



Why we create logs :

                   We get understand how the testcases execute , after which statement testcase is
                   failed . any one who don't have technical knowledge will get understand easily

"""



# This is the file of python which creates logs

# for creation of logs we need
# 1.file (where logs are storing)
# 2.format
# 3.logger object


# import logging module
import logging

class logs_generator_class:


    @staticmethod  # we can call this method without creation of class object . we can directly call
                   # this method by class name only (testcase file)
    def logs_generator_method():


        # we need file to store logs
        log_file = logging.FileHandler('.\\Logs\\CredKart.log')
        # creating log file in Logs directory where logs storing

        # now we need to set format of logs

        log_format = logging.Formatter('%(asctime)s : %(levelname)s : %(lineno)d : %(message)s')

        # log file is created , log format is created then log object

        logger = logging.getLogger()  # log object

        # Now three basic things completed which is required to create logs

        # now we need to set format of logs in log file

        log_file.setFormatter(log_format)     # This is set format which we declare earlier

        # now after that how many logs generate add those logs everytime in log file

        logger.addHandler(log_file)   # logger is creating logs so we add logs in file so
                                      # logger object is use

        # now we set the level of logs means which log level we want

        logger.setLevel(logging.INFO)     # set INFO level

        # we use logger object because logger is creating logs (logging.getLogger())

        return logger  # return logger level to method




    # Now we need to call this method by class name in testcases




"""

levels of logs 

debug
info
warning
error
critical 

if we set level as info then it record info and its above means warning , error , critical
ignored debug




"""
