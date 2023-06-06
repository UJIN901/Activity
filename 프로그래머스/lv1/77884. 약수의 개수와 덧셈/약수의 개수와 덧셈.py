from math import*

def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        if sqrt(i) == trunc(sqrt(i)) :
            answer -= i
        else :
            answer += i
        
    return answer