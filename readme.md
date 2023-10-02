# Amazon Price Tracker

Amazon Price Tracker is a Python script that monitors the price of a specific product on Amazon and sends email notifications when the price drops below a set target price. This project uses web scraping techniques to fetch the current price of the product and Gmail's SMTP server for email notifications.

## Getting Started

To use this project, follow the steps below:

1. **Prerequisites**

   You'll need to have the following installed:

   - Python
   - Required Python packages: `requests`, `BeautifulSoup`, `smtplib`
   - A Gmail account with two-factor authentication enabled

2. **Installation**

   - Clone this repository to your local machine:

     ```bash
     git clone https://github.com/your_username/amazon-price-tracker.git
     cd amazon-price-tracker
     ```

   - Install the required Python packages:

     ```bash
     pip install requests beautifulsoup4
     ```

3. **Configuration**

   - Open the `web_scraping_price_alert.py` file in a text editor.

   - Update the following variables with your own information:

     - `sender_email`: Your Gmail email address.
     - `sender_password`: Your Gmail password or App Password (if using two-factor authentication).
     - `receiver_email`: The recipient's email address where you want to receive price alerts.
     - `target_price`: The target price for the product. You will receive an email notification when the product's price drops below this value.

   - Save the file.

## Usage

Run the script using the following command:

```bash
python web_scraping_price_alert.py
