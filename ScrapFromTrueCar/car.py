#!/bin/usr/python3
'''
author : @ AmirZoyber
'''
import requests
import re
import mysql.connector
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_html(link):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    h = session.get(link)
    s = BeautifulSoup(h.text,'html.parser')
    return s

cnx = mysql.connector.connect(user='USERNAME',password='PASSWORD',host='127.0.0.1',database='DatabaseName') # table car (name,price,miles)
myCursor = cnx.cursor()

carName = input("enter car name : ") # CarName to search datas about in the site.
link = "https://www.truecar.com/used-cars-for-sale/listings/CARNAME/?sort[]=best_match"
namedLink = re.sub('CARNAME',carName,link) # Change the CARNAME with the carName that you typed in input.

htmlPages = get_html(namedLink) # Download the HTML source of namedLink.

allCars = htmlPages.find_all('li',attrs={'class':'margin-top-3 d-flex flex-grow col-md-6 col-xl-4'}) # Find all cars with specific name.

if (len(allCars)!=0):
    for car in (allCars):
        #x = allCars[i]
        carFullName = car.find('span','vehicle-header-make-model text-truncate')  # Car FullName

        carPrice = car.find('div','heading-3 margin-y-1 font-weight-bold')        # Car Price
        carPrice = re.sub(',',"",carPrice.text)                                 

        carPerformance = car.find('div',attrs={'data-test':'vehicleMileage'})     # Miles
        carPerformance = re.sub(',',"",carPerformance.text)                    

        myCursor.execute("INSERT INTO mashin VALUES (\'%s\',\'%s\',\'%s\')"%(carFullName.text,carPrice,carPerformance))  # Save data in database.
        cnx.commit()
        print(myCursor.rowcount, "was inserted.")
else:
    print (f"Nothing founded with {carName} name.")