import re
import PostsToJson
import GetHtmlSourceCode

#All the categories and questions.
topicLink = "https://islamqa.info/language/categories/topics/number/" 

#Languages of questions. (16)
languages = ["fa","en","ar","id","tr","fr","ur","ru","es","ge","hi","zh","ug","tg","bn","pt"]

#The path for scraping each language in seperate files.
path = "/home/amirzoyber/ISQA_out_4/ISQA_V4_language.json" 

#Count the scrapped questions.
scrappedCounter = 1 

def languageLinks():
    for lang in languages:
        link = re.sub("/language","/"+lang,topicLink)
        file = re.sub("language",lang,path)
        for i in range(1,270):
            Link = re.sub("number",str(i),link)
            soup = GetHtmlSourceCode.getHtml(Link)
            posts = soup.find_all('a',attrs={"class":"card post-card"})
            lastPage = soup.find_all("li",attrs={'class':'pagination-link pagination-last'})

            if (posts!=[]):
                if (lastPage==[]):
                    PostsToJson.postToJson(posts,lang)
                else:
                    lastINT = lastPage[0];lastINT = lastINT.find('a');lastINT = lastINT['href']
                    lastINT = re.sub(".*\?page=","",lastINT)

                    lastLink = Link+"?page=adad"
                    for j in range(1,int(lastINT)+1):
                        lastedLink = re.sub("adad",str(j),lastLink)
                        soup2 = GetHtmlSourceCode.getHtml(lastedLink)
                        posts = soup.find_all('a',attrs={"class":"card post-card"})
                        PostsToJson.postToJson(posts,lang,scrappedCounter,file)
