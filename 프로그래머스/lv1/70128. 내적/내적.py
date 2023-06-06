def solution(a, b):
    answer = 0
    answer = sum(x * y for x, y in zip(a, b))
    print(answer)
    return answer