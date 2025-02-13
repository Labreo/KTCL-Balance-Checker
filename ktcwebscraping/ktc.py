import requests
from bs4 import BeautifulSoup
import base64
import pywhatkit as kit
import pyautogui
import time
#Future updates:implement storing data{skipped},auto reloading at intervals or after change{done},whatsapp automation{done}
#User enters ktc data manually and redirects according
BASE_URL = 'https://cashless.ktcl.goa.gov.in'
card_details = "-"
phone_number = "-"
#card_details=input("Enter your card number:")
#print(card_details)
s = requests.Session()

# Step 1: Construct the Encoded URL/website use base64 to encode
encoded_card = base64.b64encode(f"{card_details}|test_value".encode()).decode()
generated_url = f"{BASE_URL}/Smartcard/card_details/{encoded_card}"
#print(f"Constructed URL: {generated_url}")

# Step 2: Fetch Data from the Constructed URL/avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": f"{BASE_URL}/Smartcard/card_details/",
    "Origin": BASE_URL
}
r = s.get(generated_url, headers=headers)

# Step 3: Parse the Response
soup = BeautifulSoup(r.text, 'html.parser')
wallet_element = soup.find("input", {"id": "Wallet_balance"})

if wallet_element:
    balance =int(wallet_element.get("value"))
    if balance<53:
        message = f"Your KTCL card has only ₹{balance} balance remaining!Recharge it soon!"

        # Send the message instantly
        kit.sendwhatmsg_instantly(phone_number, message)
        time.sleep(2)

        # Simulate pressing "Enter" to send the message
        pyautogui.press("enter")

        print("Message sent successfully!")
    #print(f"Current balance: {balance}")
else:
    print("Could not find balance information. Check if login is required.")

