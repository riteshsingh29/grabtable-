import webbrowser,time
from PIL import ImageGrab
import pyautogui
import cv2 
import unittest
from selenium import webdriver




#webbrowser.open('https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10000&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17',new=1, autoraise=True)


browser=webdriver.Chrome()
for i in range (0,360):
    
browser.get("https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10000&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17")
browser.set_window_size(1400,1000)
browser.execute_script("window.scrollTo(0,600)")
time.sleep(5)
image = ImageGrab.grab(bbox=(232,190,1436,850))
image.save('sc.png')
browser.close()

