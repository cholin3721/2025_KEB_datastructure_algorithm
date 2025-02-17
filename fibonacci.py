store = [0, 1]
memo = dict()

def fibonacci_memo(n) -> int:
    if n in memo:  # 딕셔너리에 이미 계산된 결과가 있으면 그 값을 리턴
        return memo[n]
    elif n <= 1:  # 0이나 1이 오면 그 값을 바로 리턴
        return n
    else:
        memo[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1)  # 계산된 결과 값이 없을 경우 딕셔너리에 추가
        return memo[n]

# def develop_fibonaaci(n) :
#     if n < len(store)-1 :
#         for i in range
#     else :
#         return store[n]



def cj_fibonacci_recursion(n) -> int :
    """
    fibonacci number
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else :
        return cj_fibonacci_recursion(n-1) + cj_fibonacci_recursion(n-2)

def cj_Fibonacci3(n) :
    a, b = 0, 1
    for i in range(n) :
        a, b = b, b+a
    return a