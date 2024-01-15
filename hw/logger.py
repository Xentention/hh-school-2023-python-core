import time
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()

def methods_logger(klass):
    def log(function):
        def wrap(*args, **kwargs):
            time1 = time.time()
            ret = function(*args, **kwargs)
            time2 = time.time()
            logger.info(f'{function.__name__} function took {(time2-time1)*1000.0} ms')
            return ret
        
        logger.info(f'{function.__name__} execution logged at {time.time()}')
        return wrap
    
    for name in dir(klass):
        if name.startswith('__'):
            continue
        method = getattr(klass, name)
        if callable(method):
            setattr(klass, name, log(method))
    return klass
