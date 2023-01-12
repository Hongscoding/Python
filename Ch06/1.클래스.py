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
