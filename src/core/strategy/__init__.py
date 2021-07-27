from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        raise NotImplementedError()


class BrownStrategy(Strategy):

    def __init__(self):
        super(BrownStrategy, self).__init__()

    def execute(self):
        print('BrownStrategy')


if __name__ == "__main__":
    pass
