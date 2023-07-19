import requests
from bs4 import BeautifulSoup

# to run cell # %%

URL = "https://www.artrabbit.com/all-listings/united-kingdom/birmingham?page={page_number}"

page = requests.get(URL)


def getEventDetails(article):
    category = article.find(class_="b_categorical-heading").text
    # print(category.text)

    title = article.find_all(class_="b_small-heading")[0].text
    date = article.find_all(class_="b_small-heading")[1].text
    # print(title.text, date.text)

    venue = article.find_all(class_="b_instructional-text")[0].text
    location = article.find_all(class_="b_instructional-text")[1].text

    return category, title, date, venue, location
    # print(venue.text, location.text)


def getEventLink(article):
    link = article.find("a").get("href")
    return link


def getEventImage(article):
    image = article.find("picture").find("img")
    image_src = image.get("src")
    image_alt = image.get("alt")
    return image_alt, image_src


for page in range(1, 3):
    r = requests.get(URL.format(page_number=str(page)))
    soup = BeautifulSoup(r.content, "html.parser")

    content = soup.find("div", class_="m_listing-items_section")
    articles = content.find_all("article")

    if not articles:
        break
    else:
        print(f"page number: {page}")
        for article in articles:
            print(getEventDetails(article))
            print(getEventLink(article))
            print(getEventImage(article))
