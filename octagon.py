def octagon(n) :
    if n <= 7 :
        return str(n)
    a = n // 8
    b = str(n % 8)
    return octagon(a) + b
# 내 버전

def dec_oct(n) -> int :
    if n == 0 :
        return ""
    else :
        return dec_oct(n//8) + str(n%8)
# 교수님 버전


while True :
    print(octagon(int(input("8진수로 변환할 수를 입력하시오 : "))))
    print(dec_oct(int(input("8진수로 변환할 수를 입력하시오 : "))))
    #printe(n, oct(n))



