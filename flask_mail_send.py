import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

my_email = "saptarshidey2120@gmail.com"
password = "deel tsxs omxc zdpg"

# Create the email
msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = my_email
msg['Cc'] = "mondalbulti1985@gmail.com"
msg['Subject'] = "Python (Selenium) Assignment - Saptarshi Dey"

# Email body
body = """
    Dear Sir,

    I am pleased to inform you that I have completed the Python (Selenium) Assignment as requested. Please find the submission details below:

    1. Screenshot of the Form Filled via Code: Attached as multiple screenshots namely:- screenshot_1.png, screenshot_2.png, screenshot_3.png.

    2. Source Code: https://github.com/Saptarshi2120/Selenium_Form.

    3. Brief Documentation of Approach: Included in the README.md file in the GitHub repository. Along with the a pdf named "Selenium Automation Script Documentation".

    4. Resume: Attached as Resume.pdf.

    5. Links to Past Projects/Work Samples:
        - Project 1: Web Scraping on books: https://github.com/Saptarshi2120/Web-scrapping.
        - Project 2: Flipkart Web Scraping: https://github.com/Saptarshi2120/Flipkart_scrapping.
        - Project 3: Electric Vehicle Market Segmentation: https://github.com/Saptarshi2120/Electric-Vehicle-Market-Segmentation.
        - Project 4: Drivers Drowsiness Detection: https://github.com/Saptarshi2120/Drivers-Drowsiness-Detection

    6. Availability: I confirm my availability to work full-time (10 am to 7 pm) for the next 3-6 months.

    Thank you for this opportunity. I look forward to discussing my submission and any next steps.

    Best regards,
    Saptarshi Dey
    saptarshidey2120@gmail.com
    +91-8116850597
    """
msg.attach(MIMEText(body, 'plain'))

# Attachments
attachments = ["screenshot_1.png","screenshot_2.png","screenshot_3.png", "Resume.pdf", "Selenium Automation Script Documentation.pdf"]
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

for attachment in attachments:
    file_path = os.path.join(downloads_folder, attachment)
    with open(file_path, "rb") as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={attachment}')
        msg.attach(part)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=msg.as_string())
