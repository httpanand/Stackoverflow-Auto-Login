from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(executable_path=r'your chrome driver path') 

driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")


element = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/form/div[1]/div/input")
email = 'your email id'
element.send_keys(email)

time.sleep(2)

element2 = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/form/div[2]/div[1]/input")
password = 'your password'
element2.send_keys(password)

time.sleep(2)

element3 = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/form/div[3]/button")
element3.click()

