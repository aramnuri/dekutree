import pandas as pd


class StockLoaderModule:

    def run(self, symbols: pd.DataFrame, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']):
        return symbols if self._validate_dataframe_column(symbols, columns) \
            else None

    def _validate_dataframe_column(self, dataframe, columns):
        df_columns = tuple(dataframe)
        return all(map(lambda c: c in df_columns, columns))


if __name__ == "__main__":
    pass
