"""
seprate tow part of a object, let the parts can change indvidially
"""

from abc import ABC, abstractmethod 
import math


class Shape(ABC):

    def __init__(self, color: object):
        self.color = color 

    @abstractmethod
    def render(self):...


class Color(ABC):

    @abstractmethod
    def render(self, shape: Shape, area: float=.0):...



class Rectangle(Shape):

    def __init__(self, color: Color, w: float=.0, h: float=.0):
        super().__init__(color=color)
        self.w = w
        self.h = h
        self.name = 'Rectangle'

    def render(self):
        self.color.render(shape=self, area=self.w * self.h)


class Circle(Shape):

    def __init__(self, color: Color,r: float=.0):
        super().__init__(color=color)
        self.r = r
        self.name = "Circle"

    def render(self):
        self.color.render(shape=self, area=math.pi * self.r ** 2)


class Red(Color):

    def __init__(self):
        self.color_name = "red"

    def render(self, shape: Shape, area: float=.0):
        print(f"render shape {shape.name} to color {self.color_name} with size {area:.2f} area.")


if __name__ == "__main__":
    
    red = Red() 
    circle = Circle(r=2.1, color=red)
    circle.render()

    rectangle = Rectangle(w=2.3, h=4.1, color=red)
    rectangle.render()