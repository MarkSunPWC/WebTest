import os
import selenium
import traceback
import logger
import imageHandler
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class webdriverFunctions:


    def __init__(self, logDir):
        TIMEFORMAT='_%Y_%m_%d-%H-%M-%S'
        self.logDir = logDir
        try:
            self.logDir = logDir+''+time.strftime(TIMEFORMAT,time.localtime(time.time()))
            self.imgDir = os.path.join(os.path.dirname(os.getcwd()),'Images')
            os.mkdir(self.logDir)
            chrome_driver = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()),'tools\chromedriver.exe'))
            os.environ["webdriver.chrome.driver"] = chrome_driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--test-type")
            chrome_options.add_argument("disable-extensions")
            chrome_options.add_argument("--user-data-dir="+os.path.abspath(os.path.join(os.path.dirname(os.getcwd()),'tools\User Data')))
            self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
            print '--------------%s--------------'%self.driver.set_window_size(1500,850)
            self.logger  = logger.logger(os.path.join(self.logDir,'test.log'))
            self.logger.logInfo('Starting case with\n  ---logDir:%s\n  ---imgDir:%s'%(self.logDir,self.imgDir))
            self.imageHandler = imageHandler.imageHandler()
        except:
            raise Exception(traceback.print_exc())

    def __del__(self):
        del self

    def ExeWebdriverCmd(self, cmd=None, param1=None, param2=None):
        self.logger.logInfo('Executing driver commmand:'+cmd+','+str(param1)+','+str(param2)+':')
        try:
            if param1==None:
                if cmd=='close':
                    return self.driver.close()
                elif cmd =='quit':
                    return self.driver.quit()
                else:
                    return self.NoSuchCmd(cmd)
            elif param2==None:
                if cmd=="get":
                    return self.driver.get(param1)
                elif cmd=="find_element_by_id":
                    return self.driver.find_element_by_id(param1)
                elif cmd=="find_element_by_name":
                    return self.driver.find_element_by_name(param1)
                elif cmd=="find_element_by_xpath":
                    return self.driver.find_element_by_xpath(param1)
                elif cmd=="find_elements_by_xpath":
                    return self.driver.find_elements_by_xpath(param1)
                elif cmd=="get_screenshot_as_file":
                    return self.driver.get_screenshot_as_file(os.path.join(self.logDir,param1+'.png'))
                elif cmd=="find_elements_by_class_name":
                    return self.driver.find_elements_by_class_name(param1)
                elif cmd=="find_elements_by_tag_name":
                    return self.driver.find_elements_by_tag_name(param1)
                elif cmd=="execute_script":
                    return self.driver.execute_script(param1)
                else:
                    return self.NoSuchCmd(cmd)
            else:
                if cmd=="assert":
                    if param2=='title':
                        assert("%s"%param1 in self.driver.title)
                    else:
                        return self.NoSuchCmd(cmd)
                elif cmd=="execute_script":
                    return self.driver.execute_script(param1,param2)
                else:
                    return self.NoSuchCmd(cmd)
        except:
            self.logger.logException("\nException captured, here is trace back:")
            raise Exception('Test Case Fail')

    def ImageComp(self, img1, img2, ResultFile, bound=(0, 0, 0, 0)):
        img1 = os.path.join(self.imgDir,img1+'.png')
        img2 = os.path.join(self.logDir,img2+'.png')
        self.logger.logInfo('Comparing images %s and %s with bound %s'%(img1,img2,str(bound)))
        if self.imageHandler.ImageComp(img1, img2, ResultFile, bound):
            self.logger.logInfo('Image comparision result is True')
            return True
        else:
            self.logger.logInfo('Image comparision result is False')
            raise Exception('Image comparision result between %s and %s is False'%(img1,img2))

    def getLogger(self):
        return self.logger

    def NoSuchCmd(self, cmd=None):
        self.logger.logException('command %s is not available now'%cmd)
        raise Exception('No Such Command')

