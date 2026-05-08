import logging

print("Basic logging with File handler")
print("-----\n")

basic_logger= logging.getLogger("file.basic") 
basic_logger.setLevel(logging.DEBUG)

basic_fh= logging.FileHandler("basicfile.log",delay=True)

basic_fh.setLevel(logging.INFO)

basic_logger.addHandler(basic_fh)

basic_logger.info("Info: will be written to file")
