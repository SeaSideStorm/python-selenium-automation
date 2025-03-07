from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\Admin\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# input search text
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

# Click on search btn
driver.find_element(By.ID, 'nav-search-submit-button').click()

# wait for 4 sec
sleep(4)

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
print('Test case passed')

driver.quit()
