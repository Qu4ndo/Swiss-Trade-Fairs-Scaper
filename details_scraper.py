from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

filename = "index_exhibitors.csv"
f = open(filename, "r+")
data = csv.reader(f, delimiter=';')

#ignore header row
headers = next(data)

for row in data:
    print(row[1])
    myurl = row[0]
    company = row[1]

    #connencting to site and grabbing content
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()

    #html parser
    page_soup = soup(page_html, "html.parser")

    #grabs each object
    container_details = page_soup.findAll("div", {"class":"ngn-box__content"})
    container_contact = page_soup.findAll("div", {"class":"media-object-section"})

    #adress
    adress_container = container_details[1].find("span", {"itemprop":"streetAddress"})
    adress = adress_container.get_text().strip()

    #postalcode
    postal_container = container_details[1].find("span", {"itemprop":"postalCode"})
    postal = postal_container.get_text().strip()

    #city
    city_container = container_details[1].find("span", {"itemprop":"addressLocality"})
    city = city_container.get_text().strip()

    #country
    country_container = container_details[1].find("span", {"itemprop":"addressCountry"})
    country = country_container.get_text().strip()

    phone_container = container_details[2].a["href"]
    phone = phone_container.replace("tel:", "")


    website_container = container_details[3].a["content"]

    contact_name_container = container_contact[2].img["alt"]
    contact_name = contact_name_container

    contact_position_container = container_contact[3].div.find("div", {"itemprop":"jobTitle"})
    contact_position = contact_position_container.get_text().strip()

    contact_link_container = container_contact[2].div.a["href"]
    contact_link = "https://guide.swissbau.ch" + contact_link_container

    f.write(myurl + ";" + company + ";" + adress + ";" + postal + ";" + city + ";" + country + ";" + phone + ";" + contact_name + ";" + contact_position + ";" + contact_link)

f.close()
