from sub1.Account import Account

class StockAccount(Account):
    def __init__(self, bank, id, name, balance, stock, amount, price):
        super().__init__(bank, id, name, balance)

        self.stock = stock
        self.amount = amount
        self.price = price

    def sell(self, amount, price):
        self.balance += amount * price
        self.amount -= amount


    def buy(self, amount, price):
        self.balance -= amount * price
        self.amount += amount


    def show(self):
        super().show()
        print('주식 종목 :', self.stock)
        print('주식 종목 :', self.amount)
        print('주식 종목 :', self.price)

        