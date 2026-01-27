import logging
from pathlib import Path


# calling the basic config module level function, will allow us to be able to configure the root logger and if this data are
# not passed to any child logger that will be used later, this default root logger config will be used
path = Path(__file__).parent / 'scripts.log'
logging.basicConfig(
    filename=path, level=logging.DEBUG, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%a %d %B %Y (%I:%M:%S %p %z UTC)'
)
logging.debug('this is a debug message')
logging.critical('there is an attempt to bypass domain registration processs...')

# an error log can also be logged inside the log
logging.error('failed to authenticate a user')

# or create an informational detail to the admin or even issue a warning
logging.warning('please check the module file for some pressumed future failure')

logging.info('found the user that tries to breach our database')

# to change the name of the logger, we can make use the getLogger function that only has a name but still relies on the root logger
admin_logger = logging.getLogger(name='ADMIN')

# now, I can make use of the admin logger
admin_logger.info('this is the admin logging to the log for the first time')

# normally, log messages get propagates to parent loggers, setting the propagate to false prevents this from happening
admin_logger.propagate = False

# this log message will not show since the admin disabled propagation and also did not have its own file to write to
admin_logger.info('please allow to log this important information')

admin_logger.propagate = True
admin_logger.warning('never disable the Admin from logging messages again')
