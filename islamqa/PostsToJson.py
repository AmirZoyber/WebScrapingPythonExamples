import re
import GetHtmlSourceCode
import json


def postToJson(postsArray,lang,scrappedCounter,file):
    for pst in postsArray:  
                    question = pst.find_all('p',attrs={'class':'has-font-content card-title'});question=question[0].text.strip()
                    
                    post_link = pst['href']
                    post = GetHtmlSourceCode.getHtml(post_link)
                    
                    tgs = post.find_all('a',attrs={'itemprop':'item'});tags=[]
                    if (len(tgs)!=0):
                        for t in tgs:
                            tags.append(t.text.strip())
                    else:
                        tags=None

                    lc=[tags[1] if ((tags!=None) or (len(tags)>=2)) else None]

                    if ((len(tags)!=0) or (tags==None)):
                        tags.pop(0)
                    

                    full_question = post.find_all('section',attrs={'class':'single_fatwa__question text-justified'})
                    full_question=full_question[0].text.strip()

                    answer = post.find_all('section',attrs={'class':'single_fatwa__answer__body text-justified _pa--0'})
                    answer=answer[0].text.strip() 

                    translates = post.find_all('div',attrs={'class':'dropdown-content'});translates=translates[1];translates=translates.find_all(href=True)
                    
                    source = post.find_all('span',attrs={'class':'has-text-muted'});source=source[0];source=source.find_next();source=source.text.strip();resource=[];resource.append(source) 

                    languages2 = []
                    for o in translates:
                        l = []
                        url = o['href'] 
                        l.append(url)
                        r = re.sub("/answers.*","",o['href'])
                        r = re.sub(".*/","",r)
                        l.append(r)               
                        languages2.append(l)
                    lans = [] 
                    for m in languages2:
                            l = {
                                "url" : m[0] ,
                            "language" : m[1]
                            }
                            lans.append(l)

                    view = None
                    v = post.find_all("p",attrs={"class":"subtitle has-text-muted has-title-case"})
                    for baz in v:
                        if ("بازدید" in baz.text):
                                view = re.sub("بازدیدها :\n\n","",baz.text.strip())
                                view = view.strip()
                        else :
                                view = 0  

                    if (resource==[""] or resource==[" "]):
                        resource=None

                    que = full_question if (len(full_question)>5) else question

                    if (True):                  
                            out = {            
                                "language" : lang, 

                                "index" : None ,

                                "category" : lc ,

                                "phrase" : None ,

                                "category_phrase" : None , 

                                "tags" : tags, 

                                "subject" : None,

                                "question" : que,

                                "answer" : [answer],

                                "full_answer": None,

                                "resource" : resource,

                                "translate" : lans if len(lans)!=0 else None ,

                                "link" : post_link,

                                "marja" : None,

                                "source" : {"persian_name": "اسلام سوال و جواب","english_name" :"Islam Question &amp","url": "www.islamqa.com"},

                                "date" : "1401/04/16",
                                "view" :  int(view),
                                "vote" : 0                     
                            }
                            with open(file, "a",encoding='utf8') as write_file:
                                    json.dump(out, write_file,ensure_ascii=False, indent=4)
                                    print("%i inserted"%(scrappedCounter));scrappedCounter+=1
                                    write_file.write(",\n")

                            