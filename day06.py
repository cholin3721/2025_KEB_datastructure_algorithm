def is_Even(n) -> bool:
    """
    :param n: Integer
    :return: Even -> True, Odd -> False
    """
    if n&1 == 0 :
        return True
    else :
        return False

a = 10
b = 11
# bit operation

print(a & b)

n = int(input("정수를 입력하시오 : "))
print(is_Even(n))