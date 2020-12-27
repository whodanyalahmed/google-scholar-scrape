from selenium import webdriver
import requests
from lxml import html
from bs4 import BeautifulSoup
import selenium
from selenium.common.exceptions import TimeoutException
import time,sys,os,re
import pandas as pd
from sys import platform

# cur_path = sys.path[0]
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.dirname(__file__)
#     return os.path.join(base_path, relative_path)

# if platform == "linux" or platform == "linux2":
#     # linux
#     path = resource_path('driver/chromedriver')
# else:
#     path = resource_path('driver/chromedriver.exe')
#     # Windows...

first = "earthquake"
newLinks = []
newHeading = []
        
print("\n\nProcessing.....")
# options = webdriver.ChromeOptions()
# options.add_argument('--disable-extensions')

# options.add_argument('--profile-directory=Default')

# options.add_argument("--disable-plugins-discovery")

# options.add_argument("--start-maximized")
# # options.add_argument('headless')
# driver =webdriver.Chrome(path,options=options)
proxies = {
 "http": "10.10.1.10:3128",
 "https": "10.10.1.11:1080",
}

url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="
def getHeadings(url,first):
    try:
        page = requests.get(url+first)
        tree  = html.fromstring(page.content)
        print("success : Loaded...")
    except Exception as e:
        print("info : website taking too long to load...stopped" + str(e))
    headings = tree.xpath('//div[@class="gs_ri"]/h3')

    return headings

headings = getHeadings(url,first)
for s in headings:
    print(s)
# def FilterHeadings(url,first):

#     filtered = ['[CITATION]','[PDF]','[BOOK]']
#     headings = getHeadings(url,first)
#     for heading in headings:
#         text = heading.text
#         # print(text)
#         if any(x in text for x in filtered):
#             continue
#         else:
#             newHeading.append(text)
#     return newHeading

# def checkLen(newHeading):
#     pag = 10
            
#     while(len(newHeading) <= 3):
#         url = "https://scholar.google.com/scholar?start=+"+pag+"&q=biology&hl=en&as_sdt=0,5"
#         FilterHeadings(url,first)
#         if(len(newHeading) <= 3):
#             break
#         pag += 10
#     return len(newHeading)



# def getLinks(first):
#     links = FilterHeadings(url,first)
#     for link in links:
#         anchors = driver.find_elements_by_partial_link_text(link)
#         for anchor in anchors:
#             l = anchor.get_attribute('href')
#             # print( anchor.text + "  ===  " + l)
#             newLinks.append(l)

    # for link in links:
    #     print(link.text)

# FilterHeadings(url,first)
# getLinks(first)

# if os.path.isfile('google scholar/text.txt'):
#     print ("File exist")
#     os.remove('google scholar/text.txt')
# else:
#     print ("File not exist")

def getSoup(u):
    
    req = requests.get(u)
    soup = BeautifulSoup(req.content,'lxml')
    headin = soup.find_all(re.compile('^h[1-6]$'),text="Abstract")
    # print(headin)

    with open('google scholar/text.txt',"a+") as f:

        f.write(str(headin))
        print("wrote")



# for d in newLinks:
#     getSoup(d)
# getSoup(newLinks)
# print(newLinks)
# for t in fil:
#     print(t) 




print("Completed")