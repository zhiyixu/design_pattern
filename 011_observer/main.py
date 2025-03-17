"""
"""

from abc import ABC, abstractmethod



class Observer(ABC):

    @abstractmethod
    def update(self, notice: object): ...


class Notice():

    def __init__(self):
        self.observers = [] 

    def attach(self, obs):
        if obs not in self.observers:
            self.observers.append(obs)

    def dettach(self, obs):
        if obs in self.observers:
            self.observers.remove(obs)
    
    def notify(self):
        for obs in self.observers:
            obs.update(self)

    
class StaffNotice(Notice):

    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info 
        self.notify()


class Staff(Observer):

    def __init__(self):
        self.company_info = None 

    def update(self, notice):
        self.company_info = notice.company_info


if __name__ == "__main__":
    notice = StaffNotice("init")
    s1, s2 = Staff(), Staff()
    notice.attach(s1)
    notice.attach(s2)

    notice.company_info = "alter"
    print(s1.company_info)
    print(s2.company_info)