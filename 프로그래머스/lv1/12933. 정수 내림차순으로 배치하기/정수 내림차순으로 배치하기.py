def solution(n):
    answer = 0
    n_list = list(map(int, str(n)))
    n_list.sort()
    n_list.reverse()
    answer = int(''.join(map(str, n_list)))
    return answer