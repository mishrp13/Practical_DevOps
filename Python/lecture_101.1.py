import logging
from logging.handlers import RotatingFileHandler

def configure_rotating_logger(logger_name, log_filepath, max_size_bytes,backup_count):

    if not isinstance(logger_name,str):
        raise TypeError("logger_name must be a string")
    if not logger_name:
        raise ValueError("logger_name cannot be an empty string")
    if not isinstance(log_filepath,str):
        raise TypeError("logger_name must be a string")
    if not log_filepath:
        raise ValueError("log_filepath cannot be empty string")
    
    if  not isinstance(max_size_bytes, int):
        raise TypeError("max_size_byte must be a intiger")
    if not max_size_bytes <=0:
        raise ValueError("max_size_byte must be a greater than 0")
    
    if not isinstance(backup_count,int):
        raise TypeError("backup count must be a intiger")
    if backup_count<0:
        raise ValueError("backout count must be greater than 0")
    

    logger= logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    handler= RotatingFileHandler(
        log_filepath,
        maxBytes=max_size_bytes,
        backupCount=backup_count
    )

    if not logger.handlers:
        logger.addHandler(handler)

    return logger


    