import requests
from bs4 import BeautifulSoup
import csv

# to run cell # %%

CITY = "london"
URL = "https://www.artrabbit.com/all-listings/united-kingdom/{city}?page={page_number}"

page = requests.get(URL)


def getEventDetails(article):
    category = article.find(class_="b_categorical-heading").text

    title = article.find_all(class_="b_small-heading")[0].text
    date = article.find_all(class_="b_small-heading")[1].text

    venue = article.find_all(class_="b_instructional-text")[0].text
    location = article.find_all(class_="b_instructional-text")[1].text

    return category, title, date, venue, location


def getEventLink(article):
    link = article.find("a").get("href")
    return link


def getEventImage(article):
    picture = article.find("picture")
    if picture:
        image = picture.find("img")
        image_src = image.get("src")
        image_alt = image.get("alt")
        return image_src, image_alt


events = []

for page in range(1, 20):
    r = requests.get(URL.format(page_number=str(page), city=CITY))
    soup = BeautifulSoup(r.content, "html.parser")

    content = soup.find("div", class_="m_listing-items_section")
    articles = content.find_all("article")

    if not articles:
        break
    else:
        print(f"page number: {page}")
        for article in articles:
            d = {}
            details = getEventDetails(article)
            link = getEventLink(article)
            image = getEventImage(article)
            d["Category"] = details[0]
            d["Title"] = details[1]
            d["Date"] = details[2]
            d["Venue"] = details[3]
            d["Locations"] = details[4]
            d["Link"] = link
            if image:
                d["Image Src"] = image[0]
                d["Image Alt"] = image[1]
            events.append(d)

filename = "documents/events.csv"
with open(filename, "w", newline="") as f:
    w = csv.DictWriter(
        f,
        [
            "Category",
            "Title",
            "Date",
            "Venue",
            "Locations",
            "Link",
            "Image Src",
            "Image Alt",
        ],
    )
    w.writeheader(),
    w.writerows(events),
