"""
将对象组合成树形结构以表示“部分-整体”的层次结构
组合模式使得用户对单个对象和组合对象的使用具有一致性
    抽象组件 component
    叶子组件 leaf 
    复合组件 composite 
    客户端 clinet
"""

from abc import ABC, abstractmethod 
import random

class Graphic(ABC):

    @abstractmethod
    def render(self): ...



class Point(Graphic): 
    
    def __init__(self, x: float, y: float):
        self.x = round(x, 2) 
        self.y = round(y, 2) 

    def __repr__(self):
        return f"<Point(x={self.x}, y={self.y})>"
    
    def render(self):
        print(self)


class Line(Graphic): 

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    
    def __repr__(self):
        return f"<Line(start={self.start.x, self.start.y}, end={self.end.x, self.end.y})>"

    def render(self):
        print(self)

class Picture(Graphic):

    def __init__(self):
        self.children = [] 

    def add(self, child: Graphic):
        self.children.append(child)

    def render(self):
        for c in self.children:
            print(c)


if __name__ == "__main__":
    
    p1 = Point(x=random.random(), y=random.random())
    p2 = Point(x=random.random(), y=random.random())

    p1.render()
    p2.render() 

    p3 = Point(x=random.random(), y=random.random())
    p4 = Point(x=random.random(), y=random.random())

    p3.render()
    p4.render() 

    l1 = Line(start=p1, end=p2)
    l1.render()

    l2 = Line(start=p3, end=p4)
    l2.render()

    print(f"\n\n========= Picture =======\n\n")

    pic = Picture()
    pic.add(l1)
    pic.add(l2)
    pic.render()

    




