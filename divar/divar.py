# @ AmirZoyber
import requests
from bs4 import BeautifulSoup

html = requests.get("https://divar.ir/s/karaj")
source = BeautifulSoup(html.text,'html.parser')
posts = source.find_all('div',attrs={'class':'post-card-item kt-col-6 kt-col-xxl-4'}) # Find all posts on home page of divar site.

for post in range(posts):
    tag = post.find('div',attrs={'class':'kt-post-card__description'}) # Find tag in a post.
    try:
        tagText = tag.text.strip()
        if (tagText=='توافقی'):
            print (tag.text)
        else:
            pass
    except:
        pass 
