from bs4 import BeautifulSoup
import requests
content = requests.get("https://books.toscrape.com/").text
soup = BeautifulSoup(content, 'html.parser')
#print(soup.p)
# all_prices = soup.find_all("p", attrs={"class":'price_color'})
# for price in all_prices:
#     print(price.string[2:])
all_titles = soup.find_all("h3")
for title in all_titles:
    link = title.find("a")
    print(link.string)
    # all_links = title.find_all("a")
    # for link in all_links:
    #     print(link.string)