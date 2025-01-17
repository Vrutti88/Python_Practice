# Q110) Write a script that uses the logging module to log debug, info, warning, and error messages to a file.
import logging
logging.basicConfig(filename='app.log',
                    level=logging.DEBUG,  
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical error message.")
