from tutorials.modules.stock_loader import KospiIndexLoaderModule


class TestStockClass:

    def test_load_dataframe(self):
        module = KospiIndexLoaderModule()
        symbols = module.run(start='2000-01-01', end='2020-12-31')
        assert len(symbols.Open) == len(symbols.Close)


if __name__ == "__main__":
    pass
