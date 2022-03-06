from operator import ge
from bs4 import BeautifulSoup
import requests

URL = "https://brb.bi"

def get_everything():
    page = requests.get(URL + "/fr/content/balance-des-paiements")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div",class_= "section")[2] # The second occurence of the section class is what contains our section
    others = results.find_all("p")
    links = [] 
    for i in others:
        links.append(URL + i.find_all("a")[0]["href"])
    return links
def download_all_links():
    links = get_everything()
    for link in links:
        data = requests.get(link)
        open(link[35:].replace("%20"," "),'wb').write(data.content)
        print("Successfully Created ",link[35:].replace("%20"," ") )
download_all_links()