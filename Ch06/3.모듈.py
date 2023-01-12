"""
날짜 : 2023/01/11
이름 : 홍민준
내용 : 파이썬 모듈 실습하기
"""

import sub2.calc 
import sub2.calc as a
from sub2.calc import *

r1 = sub2.calc.plus(1,2)
print(r1)

r2 = a.minus(2,3)
print(r2)

r3 = multi(3,4)
print(r3)

r4 = div(4,2)
print(r4)