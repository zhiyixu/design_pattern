"""
factory_method
this pattern will give a clear interfeace of how to create a factory and the specific of all action this class should have.
"""

from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self):... 

    @abstractmethod
    def pay(self, money: float):...


def Alipay(Payment):

    def pay(self, money: float):
        print(f"pay {money} via alipay.")


def Wxpay(Payment):

    def pay(self, money: float):
        print(f"pay {money} via wechatpay.")

class PaymentFactory(ABC):

    @abstractmethod
    def create_payment(self):
        # the interface of all factory class
        # param here shoule be the pubilc param of all factory.
        ...


class AlipayFactory(PaymentFactory):

    def create_payment(self):
        return Alipay()

class WxPay(PaymentFactory):

    def create_payment(self):
        return WxPay()







