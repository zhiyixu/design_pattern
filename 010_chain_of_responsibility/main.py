"""
使多个对象都有机会处理请求， 从而避免请求的发送者和接收者之间的耦合关系
将这些对象连成一条链， 并沿着这条链传递该请求， 直到有一个对象处理它为止
"""

from abc import ABC, abstractmethod 


class Handler(ABC):

    @abstractmethod 
    def handel_leave(self, day): ...


class GeneralManager(Handler):


    def __init__(self):
        self.next_hander = None

    def handel_leave(self, day):

        if day <= 10:
            print(f"{day} days Approved by {self.__class__.__name__}")
        else:
            if self.next_hander is None:
                print("not approve.")
            else:
                print(f"not approve.")

class DepartmentManager(Handler):

    def __init__(self):
        self.next_hander = GeneralManager()

    def handel_leave(self, day):
        if day <= 3:
            print(f"{day} days Approved by {self.__class__.__name__}")
        else:
            if self.next_hander is None:
                print("not approve.")
            else:
                self.next_hander.handel_leave(day=day)


class ProjectDirector(Handler):

    def __init__(self):
        self.next_hander = DepartmentManager()

    def handel_leave(self, day):
        if day <=1 :
            print(f"{day} days Approved by {self.__class__.__name__}")
        else:
            if self.next_hander is None:
                print("not approve.")
            else:
                self.next_hander.handel_leave(day=day)

if __name__ == "__main__":
    handeler = ProjectDirector()
    day = 1
    handeler.handel_leave(day=day)
    day = 5
    handeler.handel_leave(day=day)
    day = 100
    handeler.handel_leave(day=day)