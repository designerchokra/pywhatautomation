from selenium import webdriver
import autoit
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
driver = None
Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=C:/Users/harsh/AppData/Local/Google/Chrome/User Data/Profile 1')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message(number,name,testmsg,msg,file_name):
    #this script is written to access the unkown numbers
    # Reference : https://faq.whatsapp.com/en/android/26000030/
    print("In send_message_to_unsavaed_contact method")
    params = {'phone': str(number)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    print(final_url)
    driver.get(final_url)
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@title = "Menu"]')))
    print("Page loaded successfully.")
    sleep(5)

    #this script searches from the main homepage where the contact is.
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry,name))
            if retry==2:return
    you='/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    msg_box = driver.find_element_by_xpath(you)
    msg_box.send_keys(testmsg)
    sleep(1)
    msg_box.send_keys(msg)
    paths='/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'
    k= driver.find_element_by_xpath(paths)
    k.click()

    print("Message send successfully.")
 
    #this script is written to send the whatsapp attachment.
    sleep(6)
    user_group_xpath = '//span[@title = "{}"]'.format(name)
    print("sending attachment")
    for retry in range(3):
        try:
            sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, user_group_xpath))).click()
            break
        except Exception:
            print("retry:{} {} not found in your contact list".format(retry,name))
            if retry==2:return
    attachment_box = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')
    attachment_box.click()
    openexplorerbox = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[4]/button')
    openexplorerbox.click()
    sleep(3)

    #to send the attachment here we are setting the file name into the ToolWindows32 class 3
    docPath = "C:\\Users\\harsh\\" + file_name 
    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", (docPath))
    autoit.control_click("Open", "Button1")
    sleep(5)
    send = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
    send.click()
    sleep(10)
    print("File send successfully.")

if __name__ == "__main__":

    print("Web Page Open")
    
    whatsapp_login()
    sleep(4)
    #send_message(number,name,testmsg,msg,file_name)

    #for file name: 
    # 1. select your drive (Download, desktop, drives )
    # 2. followed by \
    # 3. enter your file name with extension.
    send_message("+917898798788","Mom","\n","...",(r"Desktop\1.PNG")) 
    sleep(10)

    driver.close() # Close the tab after the job is finished
    driver.quit()
