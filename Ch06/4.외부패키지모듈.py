"""
날짜 : 2023/01/11
이름 : 홍민준
내용 : 파이썬 외부 패키기 모듈 실습하기

패키지 설치
pip install openpyxl
"""

from openpyxl import Workbook

# 새로운 엑셀 파일 생성
wb = Workbook()

# 현재 sheet 활성화
sheet = wb.active

#데이터 입력
sheet['A1'] = '파이썬 Excel 실습'
sheet.append(['아이디','이름','휴대폰','나이','주소'])
sheet.append(['a101','김유신','010-1234-1001',21,'서울'])
sheet.append(['a102','김춘추','010-1234-1002',21,'대구'])
sheet.append(['a103','강감찬','010-1234-1003',21,'부산'])

# 저장 후 종료
wb.save('C:/Users/java1/Desktop/Member.xlsx')
wb.close()

print('프로그램 종료')
