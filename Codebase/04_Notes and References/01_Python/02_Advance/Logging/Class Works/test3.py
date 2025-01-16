import logging
logging.basicConfig(filename='test4.log', level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def divide(a,b):
    logging.info("the number entered by the user is %s and %s",a,b)

    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info(f"result of code is {div} ")
        return a / b
    except Exception as e:
        logging.exception(e)
        print(e)


divide(3,0)