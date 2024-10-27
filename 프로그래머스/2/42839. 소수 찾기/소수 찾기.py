import itertools, math

def solution(numbers):


    li = []
    li2 = []
    n = list(numbers)
    
    for i in range(1, len(n)+1):
        for x in itertools.permutations(n, i):
            x2 = list(x)
            if x2[0] == '0':
                continue
            else:
                li.append(list(x))
            
    for i in range(len(li)):
        li[i] = int(''.join(li[i]))
    
        li2.append(li[i])


    li2 = list(set(li2))
    
    print('li2:',li2)

    answer = []
    for i in li2:
        if i== 0 or i == 1:
            pass
        elif i == 2:
            answer.append(i)
        else:
            for j in range(2, int(math.sqrt(i)+1)):
                if i % j == 0:
                    break
                #if j == int(math.sqrt(i)):
                #    answer.append(i)
            else:
                answer.append(i)
    return len(answer)
