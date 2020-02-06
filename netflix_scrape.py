#Scrapes all netflix originals titles and writes them to netflix_titles.csv
#Author : Anirudh Kachroo
import requests
from bs4 import BeautifulSoup
from csv import writer
base_url ="https://www.netflix.com/in/browse/genre/839338"
title_url = "https://www.netflix.com/in/title/80211648"
nf = requests.get(base_url)
#print(nf.text)
soup = BeautifulSoup(nf.text,"html.parser")
horizontal_row_items=soup.find_all("img",class_="nm-collections-title-img")
with open("netflix_titles.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name","ID"])
    for row_item in horizontal_row_items:
        csv_writer.writerow([row_item["alt"],row_item["data-title-id"]])
        


