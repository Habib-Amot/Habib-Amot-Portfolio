# in the basic logging module, we relied on the root logger to log something inside the log file
# in this lesson, I am going to use a custom logger

# Custom loggers use an hierrachy of loggers, and the base logger is the parent logger for all loggers 
# this means that if some configurations or logs are not handled by our custom logger, it will be propagated to loggers in higher levels
# in th hierrachy to the base logger which is the root logger

# to build a custom logger, I first need to configure the Handlers, Filter and formatters that the logger is going to make use of

import os
import random
import smtplib
import logging
from pathlib import Path
from logging import Formatter
from dotenv import load_dotenv
from logging import FileHandler
from logging.handlers import SMTPHandler

load_dotenv()

# a handler is what handles the output of the log message i.e where the message should go to
# while a formatter is responsible for handling how the log message should look

handler = FileHandler(filename=Path(__file__).parent / 'custom-log.log', mode='w')
formatter = Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%d %b %Y %I:%M:%S %p %z UTC')

handler.setFormatter(formatter)  # add the formatter object to the handler

logger = logging.getLogger(__name__)  # give the handler a name and also create it
logger.addHandler(handler)  # set the logger handler to the handler object
logger.setLevel(logging.DEBUG)  # set the logger log level

# and now, the handler can be make use of
for number in random.choices(list(range(5)), k=19):
    try:
        print(10 / number)
    except ZeroDivisionError:
        logger.error('number 0 was generated during random selection')

# one more flexibility with the logging module is that, we can aslo log to an email address
smtp_handler = SMTPHandler(
    mailhost='smtp.google.com', fromaddr='habibgemini1@gmail.com', toaddrs='habibyakubu005@gmail.com', subject='Critical error has occurred', credentials=(os.getenv('GOOGLE_USERNAME'), os.getenv('GOOGLE_PASSWORD'))
)
smtp_handler.setLevel(logging.FATAL)
logger.addHandler(smtp_handler)
try:
    logger.fatal('this is a fatal error that needs immediate attention!')
except smtplib.SMTPDataError:
    logger.error('failed to send email notification about fatal error')
except smtplib.SMTPAuthenticationError:
    logger.error('failed to authenticate with the email server, check the credentials')
except smtplib.SMTPException as e:
    logger.error(f'smtp exception occurred: {e}')
