from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

page_number_max = int(input("Maximum Number of Pages on the Website: "))
page_number = 1

filename = "buffer.csv"
b = open(filename, "w")
headers = "link; company_name"
b.write(headers)

for x in range(0, page_number_max):
    myurl = "https://guide.swissbau.ch/de/aussteller?page=" + str(page_number)
    page_number += 1

    #connencting to site and grabbing content
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    #html parser
    page_soup = soup(page_html, "html.parser")

    #grabs each object
    containers = page_soup.findAll("li", {"class":"ngn-content-box ngn-content-box-horizontal ngn-bookmark-button-visible"})

    #loop container to get infos and safe to csv
    for container in containers:
        #name of the company
        company_name = container.div.picture.img["alt"]
        #link to profile page
        link = "https://guide.swissbau.ch" + container.div.a["href"]
        b.write("\n" + link + ";" + company_name)
        print(company_name + ", " + link)

b.close()
