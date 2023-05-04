"""
날짜 : 2023/01/11
이름 : 홍민준
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car
from sub1.Account import Account

bmw = Car('BNMW','검정색',5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

sonanta = Car('소나타', '흰색', 3000)
sonanta.speedUp()
sonanta.speedDown()
sonanta.show()

kb = Account('국민은행','101-21-1100','김유신',10000)
kb.deposit(40000)
kb.withraw(5000)
kb.show()

wr = Account('우리은행','101-21-1001','김춘추',2000)
wr.deposit(30000)
wr.withraw(12122)
wr.show()
