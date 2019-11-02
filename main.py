from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

page_number_max = int(input("Number of Pages on the Website: "))
page_number = 1

for x in range(0, page_number_max):
    myurl = "https://guide.swissbau.ch/de/aussteller?page=" + str(page_number)
    page_number += 1

    #connencting to site and grabbing content
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    #html parser
    page_soup = soup(page_html, "html.parser")

    #grabs each object with the no-image tag & image
    containers = page_soup.findAll("li", {"class":"ngn-content-box ngn-content-box-horizontal ngn-bookmark-button-visible"})

    #loop container
    for container in containers:
        #name of the company
        name = container.div.picture.img["alt"]
        #country of company
        country_container = container.findAll("div", {"class":"ngn-search-card-country ngn-block"})
        country = country_container[0].text.strip()
        #link to profile page
        link = "https://guide.swissbau.ch" + container.div.a["href"]
