"""
实代理
虚代理
保护代理
"""
from abs import ABC, abstractmethod 


class Subjct(ABC):

    @abstractmethod
    def get_content(self): ...


    @abstractmethod
    def set_content(self, content: str): ...


class RealSubject(Subjct):
    """
    read file content whenever its created
    """
    def __init__(self, fname: str): 
        self.fname = fname 
        with open(self.fname,"r") as f:
            self.content = f.read()

    def get_content(self):
        return self.content 

    def set_content(self, content: str):
        with open(fname, "w") as f:
            f.write(content)
    

class VirtuaProxy(Subjct):

    def __init__(self, fname: str):
        self.obj = None
        self.fname = fname

    def get_content(self):
        if self.obj is None:
            self.obj = RealSubject(fname=self.fname)
        return self.obj.get_content()

    def set_content(self, content: str): 
        self.obj.set_content(content=content)

class ProtuctedProxy(Subjct):

    def __init__(self, fname):
        self.obj = None 
        self.fname = fname 

    def get_content(self):
        if self.obj is None:
            self.obj = RealSubject(fname=self.fname)
        return self.obj.get_content()

    def set_content(self):
        raise ValueError("you do not have this permission.")