def solution(arr):
    answer = sorted(arr, reverse=True)
    lower = answer.pop()
    arr.remove(lower)
    if len(arr) == 0 :
        arr.append(-1)
    return arr