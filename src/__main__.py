from core.db_connector import db_backend
from modules.stock_load.provider.naver import NaverFinanceProvider
from modules.stock_load.provider.krx import KRXProvider


# with dbBackend.Connector() as conn:
#     print("###")


def main():
    # kospi200 = get_kospi200()
    # print(kospi200)
    print(NaverFinanceProvider().get_kospi200())
    # print(NaverFinanceProvider().get_current_price())
    corps = KRXProvider.get_corporations()
    print(corps)
