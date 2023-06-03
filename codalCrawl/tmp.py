import re
from time import sleep
import openpyxl
#"متاسفانه سیستم با خطا مواجه شده است." in maliHTML.text


excell = openpyxl.load_workbook('coda.xlsx')
#sheet = excell.active

nameOfCompanies = []

def get_html(link):
    sleep(5)
    from selenium import webdriver
    from bs4 import BeautifulSoup
    url = link
    driver = webdriver.Chrome()
    driver.get(url)
    html_content = driver.page_source
    html_content = BeautifulSoup(html_content,'html.parser')
    driver.quit()
    sleep(5)
    return html_content

linkNotif = "https://codal.ir/Reports/Decision.aspx?LetterSerial=FPC31vmscwW7yOLzClRBlQ%3d%3d&rt=0&let=6&ct=0&ft=-1"

def jn():
            # صورت جریان های نقدی 
            jarianNaqd = []
            linkJarianNaqd = linkNotif+"&sheetid=9"
            jarianNaqdHTML = get_html(linkJarianNaqd)
            jarianNaqdRows = jarianNaqdHTML.find('tbody').find_all('tr')
            for j in range(1,len(jarianNaqdRows)):
                 row = jarianNaqdRows[j].text.split()
                 if ((j==1) or (j==43)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]
                         val = row[4]

                 elif((j==2) or (j==9) or (j==11) or (j==15) or (j==19) or (j==24) or (j==25) or (j==27) or (j==32) or (j==33) or (j==38) or (j==41) or (j==42) or (j==44)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]
                         val = row[6]

                 elif ((j==3) or (j==17) or (j==18) or (j==21)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+ " "+row[6]+" "+row[7]+" "+row[8]
                         val = row[9]
                 
                 elif ((j==5) or (j==12) or (j==34)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]
                         val = row[8]
                
                 elif((j==6) or (j==8) or (j==10) or (j==13) or (j==14) or (j==16) or (j==20) or (j==26) or (j==31) or (j==35) or (j==36) or (j==37)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]
                         val = row[7]

                 elif ((j==7) or (j==22) or (j==40)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "+row[8]+" "+row[9]
                         val = row[10]
                
                 elif ((j==28) or (j==29) or (j==30) or (j==39)):
                      if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]
                         val = row[5]
                      
                 elif ((j==45)):
                     if ('۰' not in row):
                         var = row[0].strip()+" "+row[1]
                         val = row[2]

                 jarianNaqd.append((var,val))