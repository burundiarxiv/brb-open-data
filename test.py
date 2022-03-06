from operator import ge
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
import pyexcel as converter

URL = "https://brb.bi"

def get_everything(path):
    page = requests.get(URL + path)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div",class_= "section")[2] # The second occurence of the section class is what contains our section
    others = results.find_all("p")
    links = [] 
    for i in others:
        links.append(URL + i.find_all("a")[0]["href"])
    return links
def download_x(element):
    links = get_everything("/fr/content/balance-des-paiements")
    for link in links:
        if element in unquote(link):
            data = requests.get(link)
            open(unquote(link[35:]),'wb').write(data.content)
            converter.save_book_as(file_name=unquote(link[35:]), dest_file_name=unquote(link[35:])+"x")
            print("Successfully Created ",unquote(link[35:]) )


download_x("Importations_par_rubrique en valeur")