import itertools, math

def solution(numbers):

    li = []
    li2 = []
    n = list(numbers)

    for i in range(1, len(n)+1):
        for x in itertools.permutations(n, i):
            li.append(list(x)) 
            
    for i in range(len(li)):
        li[i] = int(''.join(li[i]))
        li2.append(li[i])

    li2 = list(set(li2))  # 중복 제거

    answer = []
    for i in range(len(li2)):
        if li2[i] == 0 or li2[i] == 1:
            continue
        elif li2[i] == 2:
            answer.append(li2[i])
        else:
            # 소수 판별
            for j in range(2, int(math.sqrt(li2[i])) + 1):
                if li2[i] % j == 0:
                    break
            else:
                answer.append(li2[i])

    return len(answer)
