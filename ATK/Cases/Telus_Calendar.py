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
    webf.ExeWebdriverCmd('get','http://localhost:3000/ticketAssignment')
    webf.ExeWebdriverCmd('assert','MWC App','title')

    time.sleep(10)
    webf.ExeWebdriverCmd("get_screenshot_as_file","InitialCalendarPage")
    
    #checking chore elements
    ChoreElementChecker()
    
    #checking FEs
    FEChecker()

    #checking time line
    TimeTableChecker()

    #checking wheather bar
    WheatherBarChecker()

    #checking content of notice bell
##    BellChecker()
    
    time.sleep(2)
    
def ChoreElementChecker():
    LTMenuBt=webf.ExeWebdriverCmd("find_element_by_xpath","//div/button[@type='button' and @tabindex='0']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/span[contains(text(),'MWC Work Calendar')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/span[contains(text(),'Peggy')]")
    webf.ImageComp('Sample_InitialCalendarPage','InitialCalendarPage','InitialCalendarPageRTBell',(1395,20,1420,50))
    webf.ImageComp('Sample_InitialCalendarPage','InitialCalendarPage','InitialCalendarPageRTMicrophone',(1270,20,1300,40))
    RTHeadShotIm=webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/peggy.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'What are you looking for?')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/input[@value='' and @type='text']")
    
def FEChecker():
    #checking names
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'Jeremy.K')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'Jackson.W')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'James.D')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'Josephine.G')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'Joe.M')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'John.F')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'Jenna.F')]")
    #checking headshots
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE1.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE2.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE3.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE4.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE5.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE6.png']")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/img[@src='/assets/FE7.png']")

def TimeTableChecker():
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'8:00AM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'9:00AM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'10:00AM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'11:00AM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'12:00PM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'1:00PM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'2:00PM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'3:00PM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'4:00PM')]")
    webf.ExeWebdriverCmd("find_element_by_xpath","//div[contains(text(),'5:00PM')]")

def WheatherBarChecker():
    TIMEFORMAT='%a %b %d %Y'
    webf.ExeWebdriverCmd("find_element_by_xpath","//div/span[contains(text(),'%s')]"%time.strftime( TIMEFORMAT,time.localtime(time.time())))

def BellChecker():
    import pyaudio
    import wave
    CHUNK=1024
    webf.ExeWebdriverCmd("find_elements_by_tag_name","path")[1].click()
    time.sleep(1)
    
    print '----------------------Going to play audio---------------------------'
    wf=wave.open(r"VoiceSearch\OkGoogleNext.wav", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),\
                channels=wf.getnchannels(),\
                rate=wf.getframerate(),\
                output=True)
    data = wf.readframes(CHUNK)
 
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
     
    stream.stop_stream()
    stream.close()
     
    p.terminate()

    webf.ExeWebdriverCmd("get_screenshot_as_file","CalendarPageNoticeDraw")
    
    time.sleep(50)

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
