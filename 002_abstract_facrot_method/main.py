"""
define a factory class interface, let sub factory class create a series of related instenct.
compared to factory method, every factory in abstract factory method should procude a type of product.
/* 定义一个工厂类接口，让工厂子类来创建一系列相关或者相互依赖的对象 */

disavantages:
    it's hard to support when add new abstract class
"""

from abc import ABC, abstractmethod 


# --- abstract factory --- # 
class Shell(ABC):

    @abstractmethod
    def show(self): ...


class CPU(ABC):

    @abstractmethod
    def show(self): ...


class OS(ABC):

    @abstractmethod
    def show(self): ...


class PhoneFactory(ABC):

    @abstractmethod
    def make_shell(self): ...

    @abstractmethod
    def make_cpu(self): ...

    @abstractmethod
    def make_os(self): ...

# --- sub factory ---# 

class SmallShell(Shell):

    def show(self):
        print("small shell")


class LargeShell(Shell):

    def show(self):
        print("large shell")
       

class SnapDragonCPU(CPU):

    def show(self):
        print("snap sragon cpu")


class MediaTekCPU(CPU):

    def show(self):
        print("Media cpu")


class AppleCPU(CPU):

    def show(self):
        print("apple cpu")

class Android(OS):

    def show(self):
        print("android os")

class IOS(OS):

    def show(self):
        print("ios")

# --- product series ---- #

class IPhoneFactory(PhoneFactory):

    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()


class XiaoMiFactory(PhoneFactory):

    def make_shell(self):
        return SmallShell() 

    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android() 

class Phone(object):

    def __init__(self, cpu, os, shell):
        self.cpu = cpu 
        self.os = os 
        self.shell = shell 


    def show_info(self):
        self.cpu.show()
        self.os.show()
        self.shell.show() 


def make_phone(factory: PhoneFactory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu=cpu, shell=shell, os=os)

xiaomi = make_phone(factory=XiaoMiFactory())
xiaomi.show_info()

