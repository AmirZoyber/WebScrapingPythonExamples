import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

def getHtml(link):
    htmlCode=''
    while (htmlCode==''):
        try:
            htmlCode = requests.get(link)
            time.sleep(5)
            break
        except:
            print("[--] It's like I should spleep for a few seconds!"+Fore.WHITE+Style.BRIGHT+Back.RED)
            print("[--] Zzzz"+Fore.WHITE+Style.BRIGHT+Back.RED)
            time.sleep(5)
            continue
    sourceCode = BeautifulSoup(htmlCode.text,'html.parser')
    print("[++] sources downloaded successfully."+Fore.WHITE+Style.BRIGHT+Back.GREEN)
    return sourceCode
