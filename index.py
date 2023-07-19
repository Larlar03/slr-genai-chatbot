import requests
from bs4 import BeautifulSoup

# to run cell # %%

URL = "https://www.artrabbit.com/all-listings/united-kingdom/birmingham?page={page_number}"

page = requests.get(URL)

for num in range(1, 2):
    page = requests.get(URL.format(page_number=str(num)))
    soup = BeautifulSoup(page.content, "html.parser")

    content = soup.find("div", class_="m_listing-items_section")
    articles = content.find_all("article")
    # print(len(articles))
    for i in range(1, len(articles)):
        # Get article text
        for article in articles:
            category = article.find(class_="b_categorical-heading")
            # print(category.text)

            title = article.find_all(class_="b_small-heading")[0]
            date = article.find_all(class_="b_small-heading")[1]
            print(title.text, date.text)

            venue = article.find_all(class_="b_instructional-text")[0]
            location = article.find_all(class_="b_instructional-text")[1]
            # print(venue.text, location.text)

            links = article.find("a")
            # print(links.get("href"))

            image = article.find("picture").find("img")
            image_src = image.get("src")
            image_alt = image.get("alt")
            # print(image_src, image_alt)
