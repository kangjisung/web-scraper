def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_value = title.string
        title_string = title_value.strip()
    except AttributeError:
        try:
            title = soup.find("span", attrs={"id": 'prologueProductTitle'})
            title_value = title.string
            title_string = title_value.strip()
        except:
            title_string = "예기치 못한 에러 발생으로 상품명 조회가 불가합니다."

    return title_string


def get_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip()

    except AttributeError:
        price = "예기치 못한 에러 발생으로 가격 조회가 불가합니다."

    return price


def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()

        except AttributeError:
            rating = "예기치 못한 에러 발생으로 평점 조회가 불가합니다."

    return rating


def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        try:
            review_count = soup.find("span", attrs={'class': 'a-size-base s-underline-text'}).string.strip()
        except:
            review_count = "예기치 못한 에러 발생으로 리뷰 개수 조회가 불가합니다."

    return review_count


def get_availability(soup):
    try:
        price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip()

        if price is not None:
            available = "재고가 있습니다"
            return available
        else:
            pass

        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = ""

    return available
