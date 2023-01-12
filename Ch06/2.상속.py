"""
날짜 : 2023/01/11
이름 : 홍민준
내용 : 파이썬 상속 실습하기
"""

from sub2.StockAccount import StockAccount

kb = StockAccount('KB증권','101-1231-12312','홍길동',5000,'삼전',10,5000)
kb.deposit(1011111111)
kb.sell(5, 70000)
kb.show()