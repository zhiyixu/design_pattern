from __future__ import annotations 
from abc import ABC, abstractmethod 


class Strategy(ABC):

    @abstractmethod
    def execute(self, data): ... 


class FastStrategy(Strategy):

    def execute(self, data: str):
        print(f"{data} strategy")


class SlowStrategy(Strategy):

    def execute(self, data: str):
        print(f"{data} strategy")


class Context(object):

    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.data = {}

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def set_data(self, data: str):
        self.data[self.strategy.__class__.__name__] = data

    def exec_strategy(self):
        strategy_name = self.strategy.__class__.__name__  # nice trick
        data = self.data.get(strategy_name, "default")
        self.strategy.execute(data=data)


if __name__ == "__main__":
    c = Context(strategy=FastStrategy())
    c.set_data("fast data")
    c.exec_strategy()

    c.set_strategy(SlowStrategy())
    c.set_data("slow data")
    c.exec_strategy()
