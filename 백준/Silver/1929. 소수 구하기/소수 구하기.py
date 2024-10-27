import math, sys
m, n = map(int, sys.stdin.readline().split())
li = []
for i in range(m, n+1):
    li.append(i)
answer = []
for i in range(len(li)):
    if -1 < li[i] < 2:
        continue
    else:
        for j in range(1, int(math.sqrt(li[i]))+1):
            if j > 1 and li[i] % j == 0:
                break
        else:
            answer.append(li[i])

for i in answer:
    print(i)
