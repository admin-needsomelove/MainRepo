from utilities import http
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.log(e)
            return http.returnHttpException(e.args[0])
    return inner_function
