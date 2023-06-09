# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:14:41 2023

@author: Pavankumar
"""

#some of the important libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv

def mail_me():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('kpkumbar99@gmail.com','xxxxxxxxxxxxxx')
     
    subject = "The Shirt you want is below $20! Now is your chance to buy!"
    body = "This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
    
    msg = f"Subject: {subject}\n\n{body}"
     
    server.sendmail('kpkumbar99@gmail.com', msg )
    

def call_me_pavan():
    # connect to a web site we requires
    
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    
    page = requests.get(URL, headers=headers)
    # after this we start to get
    
    soup1 = BeautifulSoup(page.content, "html.parser")
    #print(soup1)
    #this is where f12 worls on webpage
    
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    # print(soup2)
    # simplifies the data
    
    title = soup2.find(id='productTitle').get_text()
    # find the id by f12 and copy the id of the title
    
    price = soup2.find(id='priceblock_ourprice').get_text()
    
    print(title)
    
    price = price.strip()[1:]
    title = title.strip()
    
    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    # storing in the form of list 
    
    #create a csv with write accepter
    with open ('PavankumarAmazonScraper', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
        
    if (price < 20):
        mail_me()
        
def main():
    while(True):
        call_me_pavan()
        time.sleep(86400)
        #it will print for every day on exact time
        
        
if __name__  == "__main__":
    main()