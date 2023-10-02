#importing neccasary modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Amazon product URL
url = 'https://www.amazon.com/Apple-MacBook-13-inch-Storage-English/dp/B0CB745VMN/ref=sr_1_3?crid=KOSKD8OIB9HJ&keywords=macbook+pro&qid=1696241550&sprefix=macbook+pr%2Caps%2C558&sr=8-3'


# Set your target price
target_price = 700.0  # Replace with the desired target price

# Gmail configuration (you will need to use your own Gmail account)
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
receiver_email = 'receiver_email@gmail.com'  # Replace with the recipient's email address

def get_amazon_product_price(url):
    headers = {
        "User-Agent": "Your User Agent Here"  # Replace with your user agent
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate the price element on the Amazon product page
    price_element = soup.find('span', {'id': 'priceblock_ourprice'})

    if price_element:
        price = float(price_element.get_text().replace('$', '').replace(',', ''))
        return price
    else:
        return None
    
    def send_email(subject, message):
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Compose the email
        email_message = f'Subject: {subject}\n\n{message}'

        # Send the email
        server.sendmail(sender_email, receiver_email, email_message)

        # Close the server connection
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f'Error sending email: {str(e)}')
