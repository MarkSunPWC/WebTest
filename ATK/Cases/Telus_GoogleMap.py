import time
import os
import sys
sys.path.append("..\Libs")
import webdriverFunctions

def InitialSteps():
    global webf
    global logger
    CaseName = sys.argv[0].split('\\')[-1].split('.py')[0]
    logDir = os.path.join(os.path.dirname(os.getcwd()),'Logs'+'\\'+CaseName)
    webf = webdriverFunctions.webdriverFunctions(logDir)
    logger = webf.getLogger()
    
def Test():
    global webf
    global logger
    webf.ExeWebdriverCmd('get','http://localhost:3000/')
    webf.ExeWebdriverCmd('assert','MWC App','title')
##    EmailElement = webf.ExeWebdriverCmd("find_element_by_xpath","//input[@type='text']")
##    EmailElement.send_keys("JSAutotest@pwc.com")
##    PasswdElement = webf.ExeWebdriverCmd("find_element_by_xpath","//input[@type='password']")
##    PasswdElement.send_keys("JSAuto/1")
##    webf.ExeWebdriverCmd("find_element_by_xpath","//input[@type='button' and @value='LOGIN']").click()

    time.sleep(10)
    #checking google map
    GoogleMapChecker()
    
    #checking chore elements
    ChoreElementChecker()
    
    #checking elements pined on map
    #FE pins
    FE1Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@src='/assets/MapFE1.png']")
    FE2Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@src='/assets/MapFE2.png']")
    FE4Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@src='/assets/MapFE4.png']")
    FE5Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@src='/assets/MapFE5.png']")
    FE7Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@src='/assets/MapFE7.png']")
    #Ticket pins
    Tic1Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket1/=1$ticket1.$ticket1.0']")
    Tic3Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket3/=1$ticket3.$ticket3.0']")
    Tic4Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket4/=1$ticket4.$ticket4.0']")
    Tic5Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket5/=1$ticket5.$ticket5.0']")
    Tic6Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket6/=1$ticket6.$ticket6.0']")
    Tic7Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket7/=1$ticket7.$ticket7.0']")
    Tic8Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket8/=1$ticket8.$ticket8.0']")
    Tic10Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket10/=1$ticket10.$ticket10.0']")
    Tic12Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket12/=1$ticket12.$ticket12.0']")
    Tic13Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket13/=1$ticket13.$ticket13.0']")
    Tic17Pin=webf.ExeWebdriverCmd("find_element_by_xpath","//div/span/img[@data-reactid='.1.$ticket17/=1$ticket17.$ticket17.0']")

    #checking ticket details
    #checking Josephine
    FE4Pin.click()
    time.sleep(1)
    webf.ExeWebdriverCmd("get_screenshot_as_file","MapFEDetails")
    FE4DetailChecker()
    Tic8Pin.click()
    time.sleep(1)
    webf.ExeWebdriverCmd("get_screenshot_as_file","MapTicDetailsTop")
    js="var q=document.getElementsByClassName('ticketDetail')[0].scrollTop=10000"
    webf.ExeWebdriverCmd("execute_script",js)
    time.sleep(1)
    webf.ExeWebdriverCmd("get_screenshot_as_file","MapTicDetailsBottom")
    Tic8DetailChecker()
    time.sleep(2)

def GoogleMapChecker():
    webf.ExeWebdriverCmd("get_screenshot_as_file","InitialMapPage")
    webf.ImageComp('Sample_InitialMapPage','InitialMapPage','InitialMapPageLBMap',(0,500,250,680))
    
def ChoreElementChecker():
    LTMenuBt=webf.ExeWebdriverCmd("find_element_by_xpath","//div/button[@type='button' and @tabindex='0']")
##    LBGoogleIc=webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='https://maps.gstatic.com/mapfiles/api-3/images/google4.png']")
    RBZoomInBt=webf.ExeWebdriverCmd("find_element_by_xpath","//div[@title='Zoom in']")
    RBZoomOutBt=webf.ExeWebdriverCmd("find_element_by_xpath","//div[@title='Zoom out']")
##    webf.ImageComp('Sample_InitialMapPage','InitialMapPage','InitialMapPageRTName',(880,25,940,45))
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'Peggy')]")
    webf.ImageComp('Sample_InitialMapPage','InitialMapPage','InitialMapPageRTBell',(1395,20,1420,50))
    RTHeadShotIm=webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='../../../assets/peggy.png']")

def FE4DetailChecker():
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4TRCancelBt',(245,80,270,100))
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/p[contains(text(),'Josephine Grant')]")
##    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4FinishedCount',(230,120,280,170))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4FERating',(30,165,145,185))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4Votes',(149,165,178,185))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4Skills',(27,198,113,216))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4CallIc',(30,270,130,310))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4TextIc',(155,275,260,310))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4Tic1',(30,345,210,435))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4Tic2',(25,445,215,565))
    webf.ImageComp('Sample_MapFEJosephineDetails','MapFEDetails','FE4Tic3',(25,575,210,685))

def Tic8DetailChecker():
    #check before scroll
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8TRCancelBt',(248,79,267,99))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8TicNum',(68,90,110,110))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8CusName',(66,113,190,140))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8Address',(20,190,205,250))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8CallCus',(20,265,160,295))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8TextCus',(20,310,175,330))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8JobInfo',(15,380,275,400))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8ETA',(15,445,200,480))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8AssignedFE',(15,490,275,530))
    webf.ImageComp('Sample_MapTicRuthTop','MapTicDetailsTop','Tic8JobHistory',(15,580,275,615))
    #check after scroll
    webf.ImageComp('Sample_MapTicRuthBottom','MapTicDetailsBottom','RessignEngList',(15,175,275,535))
    webf.ImageComp('Sample_MapTicRuthBottom','MapTicDetailsBottom','RatingMaker',(15,550,180,745))
    

if __name__ == "__main__":
    InitialSteps()
    try:
        Test()
        logger.logInfo('-----------------------Test Case Passed-----------------------')
    except:
        logger.logException("\nException captured, here is trace back:")
        logger.logInfo('-----------------------Test Case Failed-----------------------')
    finally:
        logger.logInfo('-----------------------Ending test case-----------------------')
        webf.ExeWebdriverCmd("close")
        webf.ExeWebdriverCmd("quit")
