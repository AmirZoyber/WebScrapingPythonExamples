import requests
from bs4 import BeautifulSoup
a = requests.get("https://divar.ir/s/karaj")
s = BeautifulSoup(a.text,'html.parser')
div1 = s.find_all('div',attrs={'class':'post-card-item kt-col-6 kt-col-xxl-4'})
for i in range(0,len(div1)):
    x = div1[i]
    z = x.find('div',attrs={'class':'kt-post-card__description'})
    try:
        f = z.text
        if (f=='توافقی'):
            print (x.text)
        else:
            pass
    except:
        pass
    