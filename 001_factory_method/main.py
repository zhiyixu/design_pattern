"""
factory_method
this pattern will give a clear interfeace of how to create a factory and the specific of all action this class should have.
define a  factory interface for create class interface, let subclass determine which class should instence. 
/* 定义了一个用于创建对象的接口（工厂接口），让子类来决定实例化哪一个产品类 */
make sure each class has single responsibility.
if we want add a new payment method, then add a new class, rather than alter our code.
"""

from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self):... 

    @abstractmethod
    def pay(self, money: float):...


class Alipay(Payment):

    def pay(self, money: float):
        print(f"pay {money} via alipay.")


class WxPay(Payment):

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


class WxPayFactory(PaymentFactory):

    def create_payment(self):
        return WxPay()


if __name__ == "__main__":
    alipay_factory = AlipayFactory()
    alipay = alipay_factory.create_payment()
    alipay.pay(money=100)

    wxpay_factory = WxPayFactory()
    wxpay = wxpay_factory.create_payment()
    wxpay.pay(money=200)





