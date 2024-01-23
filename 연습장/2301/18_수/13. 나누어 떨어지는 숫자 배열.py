def solution(array, divisor):
    answer = []
    for i in array:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if int(len(answer)) == 0:
        return [-1]
    else:
        return answer
