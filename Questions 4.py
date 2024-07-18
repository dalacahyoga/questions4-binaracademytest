from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the game page
driver.get('https://zzzscore.com/1to50/en/')
driver.maximize_window()

# Loop to find and click numbers from 1 to 50
for i in range(1, 51):

    # Find the element by its text
    number_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f"//div[text()='{i}']")))
    
    # Click the element
    number_element.click()

# Close the browser
driver.quit()