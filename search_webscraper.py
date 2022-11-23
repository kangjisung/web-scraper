import requests
from bs4 import BeautifulSoup

from basic_methods import get_title, get_rating, get_review_count, get_availability, get_price

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.8'})

# samsung
URL = "https://www.amazon.com/s?k=samsung&ref=nb_sb_noss"

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

links = soup.find_all("a", attrs={
    'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
links_list = []

for link in links:
    links_list.append(link.get('href'))

# for link in links_list:
#     print(links_list.pop())

for link in links_list:
    new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
    new_soup = BeautifulSoup(new_webpage.content, "lxml")

    print("================================")
    print("amazon 상품 조회")
    print("================================")
    print(f"상품명: {get_title(new_soup)}")
    print(f"가격: {get_price(new_soup)}")
    print(f"평점: {get_rating(new_soup)}")
    print(f"리뷰 개수: {get_review_count(new_soup)}")
    print(f"재고 여부: {get_availability(new_soup)}")
    print(f"상품 링크: https://www.amazon.com{link}")
    print("================================")
    print()









