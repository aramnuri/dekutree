from src.modules import StockLoaderModule

from quant import get_symbols
from quant.providers.naver import NaverFinanceProvider


class KospiIndexLoaderModule(StockLoaderModule):

    def run(self, start, end, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']):
        symbols = get_symbols(start=start, end=end)
        return super(KospiIndexLoaderModule, self).run(symbols, columns)


if __name__ == "__main__":
    kospi = KospiIndexLoaderModule().run(start='2000-01-01', end='2020-12-31')
    print(kospi)
