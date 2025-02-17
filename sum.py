
def hap(n) -> int :
    return sum(range(n+1))

#f(n) = n + 3
# n이 굉장히 켜지면 3이 무시됨
#O(n)

def hap2(n) -> int :
    sum = 0
    for n in range(n+1) :
        sum += n
    return sum

#f(n) = n + 3
print(hap(100))
print(hap2(100))