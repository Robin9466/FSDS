import logging

logging.basicConfig(filename="test5.log", level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


try:
    logging.info("i am trying to read a file")
    with open("robi.txt", "r"):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.critical("this situation is for us")
    logging.error(e)
    logging.exception(e)