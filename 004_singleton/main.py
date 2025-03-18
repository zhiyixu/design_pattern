from abc import ABC, abstractmethod 


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):  # if not exists, crate it.
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
class SingleClass(Singleton):
    def __init__(self, data):
        if not hasattr(self, 'initialized'):  # Check if already initialized
            self.data = data
            self.initialized = True  # Mark as initialized

a = SingleClass(data=10)
b = SingleClass(data=100)

print(a.data, b.data, id(a), id(b))

