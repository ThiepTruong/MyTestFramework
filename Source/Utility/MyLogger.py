#!/usr/bin/python
import logging
import datetime
import sys
import logging.config

def setup_logger(location = '../ExecutionResult/Log/Log_'):
    #For running main here
    #file_name = '../../ExecutionResult/Log/Log_' + datetime.datetime.now().strftime('%d_%m_%Y_%H%M%S') + '.log'
    
    file_name = location + datetime.datetime.now().strftime('%d_%m_%Y_%H%M%S') + '.log'
    formatter = logging.Formatter('%(asctime)s - %(name)-12s - %(levelname)-8s - %(message)s')
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)-12s - %(levelname)-8s - %(message)s',
                        filename=file_name,
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

if __name__ == "__main__":
    setup_logger()
    logging.info('Jackdaws love my big sphinx of quartz.')

    logger1 = logging.getLogger('myapp.area1')
    logger2 = logging.getLogger('myapp.area2')

    logger1.debug('Quick zephyrs blow, vexing daft Jim.')
    logger1.info('How quickly daft jumping zebras vex.')
    logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    logger2.error('The five boxing wizards jump quickly.')