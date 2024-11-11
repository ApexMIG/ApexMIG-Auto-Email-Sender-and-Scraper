#While using this Program you will have to sit and enter some data manually also for better results since
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

#You will have to manually change some info like the link to website
def file_appender(name ,email):
    file  = open ("Email list.csv","a")
    file.write(f"{name},{email},,FALSE\n")


driver = webdriver.Chrome()
#Manually add the link of the first second and third page
driver.get('https://faculty-directory.dartmouth.edu/department?field_people_department_tid=4041&page=2')

WebDriverWait(driver, 20)

professor_list = driver.find_elements(By.TAG_NAME,"a")

input_list = []
for element in professor_list:
    input_list.append(element.text)

# Add the name of the very first professor and the email of very last professor on page to clean up the list
start_index = input_list.index('Nikhil U Singh') if 'Nikhil U Singh' in input_list else None
end_index = input_list.index('Bo.Zhu@dartmouth.edu') if 'Bo.Zhu@dartmouth.edu' in input_list else None

# Modify the list in place to include only the values between these indices
if start_index is not None and end_index is not None and start_index <= end_index:
    del input_list[:start_index]  # Remove all elements before 'Nikhil U Singh'
    del input_list[end_index - start_index + 1:]  # Remove all elements after 'Bo.Zhu@dartmouth.edu'

profesor_name = [input_list[i] for i in range(len(input_list)) if i % 2 == 0]
odd_index_list = [input_list[i] for i in range(len(input_list)) if i % 2 != 0]

for name, email in zip(profesor_name, odd_index_list):
    file_appender(name, email)