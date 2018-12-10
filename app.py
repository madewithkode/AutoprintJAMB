# AutoprintJAMB....made with love by Onyenanu Princewill

import selenium.webdriver
import pdfkit
import time

#initialize the browser
driver = selenium.webdriver.Firefox()

#pass in the list of regnumbers here as strings(comma seperated)
regNumbers = []

#get the root url
driver.get('https://www.jamb.org.ng/examslipprinting1/PrintExaminationSlip')
print('Loading https://www.jamb.org.ng/examslipprinting1/PrintExaminationSlip...... ')
time.sleep(3)

#The input field
inputBtn = driver.find_element_by_id('txtRegNumber')


def saveSlip():
    for regnumber in regNumbers: #loop through the regnumber list
        inputBtn.send_keys(regnumber) #send virtual clicks to type regnumber
        print("typing regnumber .....")
        '''make a reference to the current window as we're going to be switching to the new window where the slip will be loaded'''
        window_before = driver.window_handles[0]

        driver.find_element_by_id('lnkSearch').click()
        print("submitting.....") #click the submit button
        
        time.sleep(15) #the ammount of time you pass here shuld be determined by your network speed 
        print('Waiting for slip to fully load......')
        
        window_after = driver.window_handles[1] #the newly loaded exam slip window
        driver.switch_to_window(window_after)
        
        #examSlipUrl = driver.current_url

        print("writing HTML........")
        f = open(regnumber+'.html','w')
        f.write(driver.page_source)
        f.close()
        print(regnumber + "DONE!")
        
        #pdfkit.from_url(examSlipUrl, regnumber+'.pdf')# if you need the result as pdf
        #driver.save_screenshot('output.png') #if you need the page as png
##print(driver.page_source)

saveSlip()

#driver.save_screenshot('output.png')
##print(driver.page_source)

#pdfkit.