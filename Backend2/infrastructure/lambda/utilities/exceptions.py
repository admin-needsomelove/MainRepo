from utilities import http
import logging

logger = logging.getLogger()

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.info(str(e))
            return http.returnHttpException(e.args[0])
    return inner_function
