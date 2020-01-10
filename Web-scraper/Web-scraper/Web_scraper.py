import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.co.uk/Bose-QuietComfort-Wireless-Headphones-Cancelling-Black/dp/B0756CYWWD/ref=sr_1_3?crid' \
      '=12D1KD67DSJY4&keywords=bose+quietcomfort+35+ii&qid=1578424602&sprefix=bose%2Caps%2C169&sr=8-3 '

headers = {"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/79.0.3945.88 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:4])

    print(title)
    print(converted_price)

    if converted_price < 200.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email', 'password')

    subject = "Bose Headphones. Price fell!"
    body = 'Check the link! https://www.amazon.co.uk/Bose-QuietComfort-Wireless-Headphones-Cancelling-Black/dp' \
           '/B0756CYWWD/ref=sr_1_3?crid' \
           '=12D1KD67DSJY4&keywords=bose+quietcomfort+35+ii&qid=1578424602&sprefix=bose%2Caps%2C169&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email sender',
        'email recipient',
        msg
    )
    print("Email sent!")

    server.quit()


check_price()

