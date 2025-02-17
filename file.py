# import csv
# numpy 처럼 설치 필요x 기본 모듈
# import random

students = []
try:
    # file = input("file name : ")
    with open('students.csv', 'r') as fp :
        readme_list = fp.readlines()
        rls = readme_list[0].split("_")
        # print(readme_list)

except FileNotFoundError as err :
    print(f"{err}")


# fp.close()