import urllib.request
from bs4 import BeautifulSoup
from utils.exceptions import exception_handler

URL = "https://finance.naver.com/item/main.nhn?code="
"""
- naver metrics
종목별
현재가
전일비
등락률
거래량
거래대금(백만)
시가총액(억)
"""


class NaverFinanceProvider:

    def get_kospi200(self):
        url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="  # page 1~20
        kospi200 = []
        for i in range(20):
            response = get_response(url, i)

            if response:
                soup = BeautifulSoup(response, "html.parser")
                corporations = soup.find_all("td", {"class": "ctg"})
                for corporation in corporations:
                    anchor = corporation.find("a")
                    kospi200.append({
                        "name": anchor.text,
                        "code": anchor["href"].split('=')[-1]
                    })

        return kospi200

    def get_current_price(self, stock_code='005930'):
        result = get_response(URL + stock_code)
        # result = urllib.request.urlopen(URL + stock_code).read()
        soup = BeautifulSoup(result, "html.parser")
        no_today = soup.find("p", {"class": "no_today"})
        now_price = no_today.find("span", {"class": "blind"})
        return int(now_price.text.replace(',', ''))


@exception_handler
def get_response(url, i):
    download_url = url + str(i + 1)
    response = urllib.request.urlopen(download_url).read()
    return response


if __name__ == "__main__":
    print("Execute directly")
    print(__name__)
else:
    print("Imported")
    print(__name__)
