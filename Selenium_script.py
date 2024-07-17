#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from PIL import Image

# Function to take a screenshot
def take_screenshot(driver, filename):
    driver.save_screenshot(filename)

# Set up the WebDriver
web = webdriver.Chrome()

try:
    # Open the Google Form
    web.get('https://forms.gle/WT68aV5UnPajeoSc8')
    time.sleep(2)  

    # Fill in the form fields
    fullname = "Saptarshi Dey"
    full = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    full.send_keys(fullname)
    time.sleep(1)

    contact_num = "8116850597"
    num = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    num.send_keys(contact_num)
    time.sleep(1)

    email_id = "saptarshidey2120@gmail.com"
    id1 = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    id1.send_keys(email_id)
    time.sleep(1)

    full_address = "Sector 4, Salt Lake, Kolkata"
    add = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    add.send_keys(full_address)
    time.sleep(1)

    pin_code = "700098"
    pin = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin.send_keys(pin_code)
    time.sleep(1)

    # Fill in the date field
    calendar_icon = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    calendar_icon.send_keys('28-08-2003')
    time.sleep(1)

    gender = "Male"
    gen = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gen.send_keys(gender)
    time.sleep(1)

    # Find the CAPTCHA text
    captcha_text_element = web.find_element(By.XPATH, '//*[@id="i30"]/span[1]/b')
    captcha_text = captcha_text_element.text

    # Fill in the CAPTCHA field
    captcha_field = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    captcha_field.send_keys(captcha_text)
    time.sleep(1)

    # Create a downloads folder path
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    # Get the total height of the webpage
    total_height = web.execute_script("return document.body.scrollHeight")

    # Set initial values
    scroll_step = 600  
    current_scroll = 0
    screenshot_counter = 1

    # Scroll and capture screenshots
    while current_scroll < total_height:
        # Scroll down the page
        web.execute_script(f"window.scrollTo(0, {current_scroll});")
        time.sleep(1)  # Adjust as needed to allow content to load

        # Capture screenshot
        screenshot_path = os.path.join(downloads_path, f"screenshot_{screenshot_counter}.png")
        take_screenshot(web, screenshot_path)
        print(f'Screenshot {screenshot_counter} saved to {screenshot_path}')
        
        # Update variables for next iteration
        current_scroll += scroll_step
        screenshot_counter += 1

    # Find and click the submit button
    submit_button = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()
    print("Form submitted successfully.")

finally:
    # Close the WebDriver
    web.quit()

