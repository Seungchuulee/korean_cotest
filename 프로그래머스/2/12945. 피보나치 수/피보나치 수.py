import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    li = []
    for i in range(n+1):
        if i == 0:
            li.append(0)
        elif i == 1:
            li.append(1)
        else:
            li.append(li[i-1]+li[i-2])
    answer = li[-1] % 1234567
    return answer