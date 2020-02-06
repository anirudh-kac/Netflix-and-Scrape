#Scrapes all netflix originals titles along with other details and writes them to netflix.csv
#Author : Anirudh Kachroo
import requests
from bs4 import BeautifulSoup
from csv import writer

base_url ="https://www.netflix.com/in/browse/genre/839338"
title_url = "https://www.netflix.com/in/title/80211648"

nf = requests.get(base_url)
#print(nf.text)
soup = BeautifulSoup(nf.text,"html.parser")
#Find all horizontal title cards
horizontal_row_items=soup.find_all("img",class_="nm-collections-title-img")

with open("netflix.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Title","Id","Year","Seasons","Maturity Rating","Genre","Synopsis"])

    for row_item in horizontal_row_items:

            title=row_item["alt"]
            data_id=row_item["data-title-id"]
            #Making request to each title page to get all data
            title_res = requests.get(f"https://www.netflix.com/in/title/{data_id}")
            title_soup = BeautifulSoup(title_res.text,"html.parser")

            info = title_soup.body.find(class_="info-container")
            year = info.find(class_="item-year").get_text()
            maturity_rating = info.find(class_="maturity-number").get_text()
            seasons = info.find(class_="duration").get_text()[0]
            genre = info.find(class_="item-genre").get_text()
            synopsis = info.find(class_="title-info-synopsis").get_text()
            # starring = info.find(class_="title-data-info-item-list").get_text()
            csv_writer.writerow([title,data_id,year,seasons,maturity_rating,genre,synopsis])
            print(year,maturity_rating,genre,synopsis,seasons)

        


