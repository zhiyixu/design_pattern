"""
为子系统中的一组接口提供一个一致的界面，
外观模式定义了一个高层接口，这个接口使得这一子系统过更加容易使用
"""

from abc import ABC, abstractmethod 

class HardWare(ABC):

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def stop(self): ...


class CPU(HardWare):

    def run(self):
        print("cpu run")

    def stop(self):
        print("cpu stop")


class Disk(HardWare):

    def run(self):
        print("disk run")

    def stop(self):
        print("disk stop")

class Memory(HardWare):

    def run(self):
        print("mem run")

    def stop(self):
        print("mem stop")

class Computer(HardWare):

    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()


    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    
    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()

if __name__ == "__main__":
    computer = Computer()
    computer.run()
    computer.stop()
