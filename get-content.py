import requests
from bs4 import BeautifulSoup

# to run cell # %%

# make get request
page = requests.get(
    "https://www.artrabbit.com/all-listings/united-kingdom/birmingham?page=1"
)

# check status code for response
print(page)

# parse the html
soup = BeautifulSoup(page.content, "html.parser")
content = soup.find("div", class_="m_listing-items_section")
articles = content.find_all("article")
lines = articles[0].find_all("p")

# find all text in article
for line in lines:
    print(line.text)

# find all the anchor tags with "href" in article
for link in articles[0].find_all("a"):
    print(link.get("href"))

# find image src in article
picture = articles[0].find("picture")
image = picture.find("img")
src = image.get("src")
alt = image.get("alt")

print(src, alt)
