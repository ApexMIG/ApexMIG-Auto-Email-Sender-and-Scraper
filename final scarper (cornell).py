#While using this Program you will have to sit and enter some data manually also for better results since
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def file_appender(name ,email):
    file  = open ("Email list.csv","a")
    file.write(f"{name},{email},,FALSE")


driver = webdriver.Chrome()
driver.get('https://www.cs.cornell.edu/people/faculty?combine=&field_research_concentration_tid=143&field_based_in_tid=All&field_faculty_type_tid=All')

WebDriverWait(driver, 20)

professor_list = driver.find_elements(By.CLASS_NAME,"text-primary")

input_list = []
for element in professor_list:
    input_list.append(element.text)
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)

for j in range(1,39):
    del unique_list[0]

for i in unique_list:
    try:
        professor = driver.find_element(By.LINK_TEXT,i)
        ActionChains(driver).scroll_to_element(professor)
        ActionChains(driver).key_down(Keys.CONTROL).click(professor).key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 15)
        email = driver.find_element(By.PARTIAL_LINK_TEXT,"cornell.edu")

    except:
        try:
             email2 = driver.find_element(By.PARTIAL_LINK_TEXT,"cornell dot edu")
        except:
            file_appender(i ,"U")
            time.sleep(8)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            WebDriverWait(driver, 10)
        else:
            file_appender(i ,email2.text)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            WebDriverWait(driver, 10)
    else:
        file_appender(i ,email.text)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, 10)


    