"""
定义一个操作中的算法骨架， 而将一些步骤延迟到子类中。
模板方法使得子类可以不改变一个算法的结构即可重新定义该算法的某些特定步骤。

角色：
    抽象类： 定义抽象的原子操作
            实现一个模板方法作为骨架
    具体类： 实现原子操作
"""

from abc import ABC, abstractmethod 
import time 


class Window(ABC):

    @abstractmethod
    def start(self): ...

    @abstractmethod
    def render(self): ...

    @abstractmethod
    def stop(self): ...

    def run(self): 
        self.start() 
        while 1:
            try:
                self.render()
                time.sleep(1)
            except KeyboardInterrupt:
                break 
        self.stop()


class MacWindow(Window):

    def __init__(self, msg: str):
        self.msg = msg

    def start(self):
        print(f"start mac windos")

    def stop(self):
        print(f"stop mac window")

    def render(self):
        print(f"render: {self.msg}")


if __name__ == "__main__":
    w = MacWindow(msg="mac")
    w.run()