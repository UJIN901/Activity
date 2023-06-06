def solution(price, money, count):
    answer = -1
    sum_m = sum(price * i for i in range(1, count + 1))
    if  sum_m > money :
        answer = sum_m - money
    else :
        answer = 0

    return answer