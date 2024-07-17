# Google Form Automation with Selenium
This repository contains a Python script to automate the process of filling out a Google Form, capturing screenshots at various steps, and submitting the form using Selenium WebDriver.

Overview
The script automates the following steps:

Opens the specified Google Form URL.
Fills out the form fields with predefined data.
Captures screenshots at various steps and saves them to the Downloads folder.
Automatically fills in the CAPTCHA field.
Submits the form.
Prerequisites
Python 3.x (Download Python)
Chrome WebDriver (Download WebDriver)
Installation
Clone the Repository

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Install Dependencies

bash
Copy code
pip install selenium pillow
Configure WebDriver

Ensure Chrome WebDriver is installed and accessible from your PATH environment variable.

Usage
Run the Script

Execute the Python script:

bash
Copy code
python selenium_script.py
Script Execution

The script will open the Google Form URL specified (https://forms.gle/WT68aV5UnPajeoSc8).
It will fill out the form fields with predefined data (name, contact number, email, address, date, gender).
Screenshots will be captured at each step and saved in the Downloads folder (~/Downloads).
After capturing screenshots, it will fill in the CAPTCHA field automatically.
Finally, the script will find the submit button and click it to submit the form.
Customization
Form Fields: Modify the script (selenium_script.py) to change the data being filled in form fields.
XPath: Adjust XPath expressions (//*[@id="..."]) in the script to match the structure of your specific Google Form.
Troubleshooting
WebDriver Issues: Ensure Chrome WebDriver is up to date and compatible with your Chrome browser version.
Element Not Found: Check and adjust XPath expressions if elements are not located correctly.
