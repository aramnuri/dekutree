import sys
import urllib.request
import pandas as pd
from datetime import datetime
from io import StringIO
from utils.exceptions import exception_handler
from modules.stock_load import providers
from modules.utils import utils


def get_symbols(code='^KS11', start='2000-01-01', end=None, save_as=None):
    """
    YAHOO FINANCE provides ONLY KOSPI data.
    start: yyyy-MM-dd
    end: yyyy-MM-dd
    ---
    period1: gap between 1970-01-01 and start in SECONDS
    period2: gap between 1970-01-01 and end in SECONDS
    """
    if end is None:
        end = datetime.now().strftime('%Y-%m-%d')

    base_url = 'https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history'
    # url = 'https://finance.yahoo.com/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter=history&frequency=1d'
    period1 = int(utils.get_local_timestamp(start))
    period2 = int(utils.get_local_timestamp(end))

    assert period1 <= period2

    download_url = base_url.format(code, period1, period2)

    response = get_response(download_url)
    sys.stdout.write('quant.get_symbols: Succeed to read url ({0})\n'.format(download_url))

    if save_as is not None and type(save_as) is str:
        fhandle = open(save_as, 'w')
        fhandle.write(response)
        fhandle.close()

    # data = list(map(lambda x: x.split(','), result.content.decode("utf-8").split('\n')))
    data = pd.read_csv(StringIO(response)).dropna(axis=0, how='any')

    return data

    """
    result = requests.get(url)
    if result.status_code != HttpStatus.OK:
        print('Failed to get {}: {}'.format(result.status_code, url))
        return None
    soup = BeautifulSoup(result.content, "html.parser")
    # print(result.content)
    table_records = soup.find_all("tr", {"class": "BdT"})
    # table_records = list(filter(lambda x: x is not None, map(lambda x: x.find("span"), table_records)))
    print(table_records, len(table_records))
    """


@exception_handler
def get_response(download_url):
    response = urllib.request.urlopen(download_url).read().decode("utf-8")
    return response


def calculate_return(item, market_code='^KS11', method=['discrete', 'log', 'difference']):
    """
    Calculate returns from a prices stream
    ---
    prices: pandas.dataframe containing ordered price observations.
    Ri: rate of return of the item
    Rm: rate of return of the market
    """
    if type(method) is list:
        method = method[0]

    dates = item["Date"].tolist()
    market = get_symbols(code=market_code, start=dates[0], end=dates[-1])

    item = item.loc[item["Date"].isin(market["Date"])]
    market = market.loc[market["Date"].isin(item["Date"])]
    dates = item["Date"].tolist()

    return_i = [
        (prices[1] - prices[0]) / prices[0] * 100
        for prices in zip(item["Close"][:-1], item["Close"][1:])
    ]

    return_m = [
        (prices[1] - prices[0]) / prices[0] * 100
        for prices in zip(market["Close"][:-1], market["Close"][1:])
    ]

    return_i = pd.DataFrame({"Date": dates[1:], "Rate": return_i})
    return_m = pd.DataFrame({"Date": dates[1:], "Rate": return_m})

    return (return_i, return_m)
