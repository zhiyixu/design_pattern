from __future__ import annotations 
from abc import ABC, abstractmethod 


class Strategy(ABC):

    @abstractmethod
    def execute(self, data): ... 


class FastStrategy(Strategy):

    def execute(self, data:str = "fast"):
        print(f"{data} strategy")

class SlowStrategy(Strategy):

    def execute(self, data:str = "slow"):
        print(f"{data} strategy")


class Contex(object):

    def __init__(self, data, strategy: Strategy):
        self.data = data 
        self.strategy = strategy

    def set_strategy(self, stragegy):
        self.strategy = stragegy
    
    def exec_strategy(self):
        self.strategy.execute(data=self.data)


if __name__ == "__main__":
    s1 = FastStrategy()
    data = "s1"
    c = Contex(data=data, strategy=s1)
    c.exec_strategy()

    s2 = SlowStrategy()
    c.set_strategy(stragegy=s2)
    c.exec_strategy()

