from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options

service = Service(executable_path = './chromedriver')
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(service=service,chrome_options=chrome_options)

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')

assert 'Show message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('.btn')
print(user_button2)
user_message.clear()
user_message.send_keys('I am extra cool')

button.click()
output_message = chrome_browser.find_element_by_id('display')

chrome_browser.quit()



