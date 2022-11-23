import requests
from bs4 import BeautifulSoup

from basic_methods import get_title, get_rating, get_review_count, get_availability, get_price


HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.8'})


# 2022 Apple MacBook Air
# URL = "https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C2R8MP/ref=sr_1_1?crid=3RGOFJ3K2VQ1Q&keywords=macbook+air&qid=1669130840&sprefix=macbook+a%2Caps%2C260&sr=8-1"
# 2021 Apple iMac
URL = "https://www.amazon.com/Apple-24-inch-8%E2%80%91core-7%E2%80%91core-256GB/dp/B0932HVSYM/ref=sr_1_3?crid=35X40896ENWJR&keywords=imac&qid=1669134326&sprefix=imac%2Caps%2C253&sr=8-3"


webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")


print("================================")
print("amazon 상품 조회")
print("================================")
print(f"상품명: {get_title(soup)}")
print(f"가격: {get_price(soup)}")
print(f"평점: {get_rating(soup)}")
print(f"리뷰 개수: {get_review_count(soup)}")
print(f"재고 여부: {get_availability(soup)}")
print("================================")
