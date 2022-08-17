import json

#Count the scrapped questions.
scrappedCounter = 1 

def writeJsonToFile(file,out):
    with open(file, "a",encoding='utf8') as write_file:
            json.dump(out, write_file,ensure_ascii=False, indent=4)
            print("%i inserted"%(counter));counter+=1
            write_file.write(",\n")