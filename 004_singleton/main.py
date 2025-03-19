from abc import ABC, abstractmethod 


class Meta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Meta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingleClass(metaclass=Meta):
    
    def __init__(self, data):
        self.data = data


a = SingleClass(data=10)
b = SingleClass(data=100)

print(a.data, b.data, id(a), id(b))

