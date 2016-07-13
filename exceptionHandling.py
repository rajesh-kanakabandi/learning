import logging
logging.basicConfig(filename='learning.log',level=logging.NOTSET)

logging.error("I am an error")
logging.debug("I am here for debugging purposes")
logging.info("I am logging some important info for you.")
logging.critical("there is a critically wrong situation")
list1 = []
j=0
try:
    print(list1)
    i = 10/j
except ZeroDivisionError as e:
    logging.exception("zero division error")

    j = 1
    i = 10
except IndexError as e:
    print("index out of bound" + str(e))
except:
    print("something went wrong")
