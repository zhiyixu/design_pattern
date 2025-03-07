from abc import ABC, abstractmethod 


class Payment(ABC):  # the target

    @abstractmethod
    def pay(self, money: int) -> None:...


class Alipay(Payment):

    def pay(self, money: int):
        print(f"Alipay: {money}.")

class Wxpay(Payment):

    def pay(self, money):
        print(f"Wxpay: {money}")


class Bankpay(object):  # the adaptee
    """
    notic this class not inheritance from the Payment class 
    """
    def cost(self, money: int):
        print(f"Bankpay: {money}")


# --- # 

class NewBankPay(Payment, Bankpay):  # the adapter
    # with multi-inheritance
    # class adapter
    def pay(self, money: int):
        self.cost(money=money)


class PaymentAdapter(Payment):  # the adapter
    # with combine
    # object adapter
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money: int):
        self.payment.cost(money)




if __name__ == "__main__":

    wxp = Wxpay()
    wxp.pay(100)

    nbp = NewBankPay()
    nbp.pay(10000)

    pad = PaymentAdapter(payment=Bankpay())
    pad.pay(200)