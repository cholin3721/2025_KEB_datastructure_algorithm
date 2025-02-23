def josephus_list(n, m):
    people = list(range(1, n + 1))  # 1 ~ n 리스트 생성
    result = []
    index = 0  # 시작 인덱스

    while people:
        index = (index + m - 1) % len(people)  # m번째 사람 선택
        result.append(people.pop(index))  # 제거 후 결과 리스트에 추가

    return result

n, m = map(int, input().split())  # 입력값을 정수로 변환
print("<" + ", ".join(map(str, josephus_list(n, m))) + ">")  