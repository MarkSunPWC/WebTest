import logging

class logger:

    def __init__(self, logName='test.log'):
        global logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        FH = logging.FileHandler(logName,'w')
        FH.setLevel(logging.DEBUG)
        SH = logging.StreamHandler()
        SH.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')
        FH.setFormatter(formatter)
        SH.setFormatter(formatter)
        logger.addHandler(FH)
        logger.addHandler(SH)
        
    def __del__(self):
        del self

    def logInfo(self, logStr=''):
        global logger
        try:
            logger.info(logStr)
        except:
            logger.exception("Exception captured")
        return True

    def logDebug(self, logStr=''):
        try:
            logger.debug(logStr)
        except:
            logger.exception("Exception captured")
        return True
    
    def logException(self, logStr=''):
        try:
            logger.exception(logStr)
        except:
            logger.exception("Exception captured")
        return True



