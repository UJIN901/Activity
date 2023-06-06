def solution(n):
    answer = '수박'
    if n % 2 == 0 :
        answer *= n // 2
        return answer
    else :
        answer *= n // 2 + 1
        return answer[:len(answer) - 1]
        
