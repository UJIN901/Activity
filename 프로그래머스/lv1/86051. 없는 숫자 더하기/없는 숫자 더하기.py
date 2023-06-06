def solution(numbers):
    answer = -1
    set_list = list(range(10))
    print(set_list)
    for i in range(len(numbers)) :
        set_list.remove(numbers[i])
    answer = sum(set_list)
    return answer