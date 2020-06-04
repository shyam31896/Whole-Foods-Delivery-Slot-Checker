from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import smtplib
import argparse
import warnings
warnings.filterwarnings("ignore")

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--browser", nargs='?', help="Specify the browser to open with")
args = parser.parse_args()

def send_email(sender, password, recipient):
    try:
        subject = "Amazon Whole Foods Market Delivery Slots Available!"
        body = "Delivery Slots available for your order at the Whole Foods Market. Order soon!\n\nLink: https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        message = "Subject: {}\n\n{}".format(subject, body)
        server.sendmail(sender, recipient, message)
        server.close()
        print("\n <-- Email sent! --> \n")
    except:
        print("\n <-- E-mail not sent. Something went wrong...! --> \n")

print("\n <-- Collecting details for E-mail notification -->")
sender = str(input("\nEnter the Sender's email: "))
password = str(input("Enter Password: "))
recipient = str(input("Enter the Recipient's email (Can be the same as Sender's email): "))
if args.browser == "Chrome":
    from selenium.webdriver.chrome.options import Options
    options = Options()
    # options.headless = True
    os.system("google-chrome --remote-debugging-port=9000 &")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9000")
    driver = webdriver.Chrome(chrome_options=options)
elif args.browser == "Firefox":
    from selenium.webdriver.firefox.options import Options
    options = Options()
    # options.headless = True
    print("\n <-- Firefox Profile Path required. -->\n <-- Copy and paste the Root Directory path of the default profile. -->\n")
    time.sleep(3)
    os.system("firefox -new-window about:profiles &")
    profile_path = str(input("Enter the path for the firefox profile: "))
    profile = webdriver.FirefoxProfile(profile_path)
    driver = webdriver.Firefox(firefox_profile=profile, firefox_options=options)

driver.get("https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1")
no_open_slots = True
time.sleep(5)

while no_open_slots:
    driver.refresh()
    soup = BeautifulSoup(driver.page_source, "html.parser")

    try:
        days = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
        count = 0
        for day in days:
            if day.text.strip() != "Not available":
                print("\n <-- Delivery available -->")
    except AttributeError:
        pass

    try:
        if "No delivery windows available. New windows are released throughout the day." == soup.find('h4', class_ ='a-alert-heading').text:
            print("\n <-- Delivery time slots not available -->")
    except AttributeError: 
        print("\n <-- Delivery time slots available -->")

    slot_patterns = ['Next available', '1-hour delivery windows', '2-hour delivery windows']
    try:
        next_slot_text = str([x.text for x in soup.findAll('h4', class_ ='ufss-slotgroup-heading-text a-text-normal')])
        if any(next_slot_text in slot_pattern for slot_pattern in slot_patterns):
            print('\n <-- Delivery slots available! -->')
            send_email(sender, password, recipient)
            no_open_slots = False

    except AttributeError:
        pass
    time.sleep(30)