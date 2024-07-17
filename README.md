# Selenium Automation Script Documentation

Overview

This script automates the process of filling out a Google Form, capturing screenshots at various steps, and submitting the form using Selenium WebDriver in Python.
* Setup Instructions *

Prerequisites
•	Latest Python installed on your system (Download Python)
•	Chrome WebDriver installed if you are running on your local machine (Download WebDriver)


Dependencies Installation
Install the required Python libraries using pip:

Copy code:
		pip install selenium pillow

WebDriver Configuration
Ensure Chrome WebDriver is installed and accessible from your PATH environment variable.

Usage
1.	Clone the Repository
Clone the repository containing the Selenium script.
							cd Downloads
							git clone https://github.com/Saptarshi2120/Selenium_Form

2.	Run the Script

		Execute the Python script :-
						python Selenium_script.py

4.	Script Execution
   
•	The script will open the Google Form URL specified (https://forms.gle/WT68aV5UnPajeoSc8).
•	It will fill out the form fields with predefined data (name, contact number, email, address, date, gender).
•	Screenshots will be captured at each step and saved in the Downloads folder (~/Downloads).
•	After capturing screenshots, it will fill in the CAPTCHA field automatically.
•	Finally, the script will find the submit button and click it to submit the form.

Customization
•	Form Fields: Modify the script (selenium_script.py) to change the data being filled in form fields.
•	XPath: Adjust XPath expressions (//*[@id="..."]) in the script to match the structure of your specific Google Form.
Troubleshooting
•	WebDriver Issues: Ensure Chrome WebDriver is up to date and compatible with your Chrome browser version.
•	Element Not Found: Check and adjust XPath expressions if elements are not located correctly.




