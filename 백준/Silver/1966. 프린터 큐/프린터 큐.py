import sys
from collections import deque

t = int(sys.stdin.readline())
answer = []

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    
    # 각 문서의 인덱스와 중요도를 [index, 중요도] 형태로 저장
    li2 = [[i, li[i]] for i in range(n)]
    
    queue = deque(li2)
    count = 0

    while queue:
        # 중요도가 가장 높은 문서를 찾음 (queue 내에서 중요도 [1] 기준으로 max 찾기)
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            count += 1
            # 맨 앞에 있는 문서를 꺼냄
            temp = queue.popleft()
            
            # 우리가 찾고자 하는 문서가 출력된 경우
            if temp[0] == m:
                answer.append(count)
                break
        else:
            # 중요도가 가장 높지 않다면, 맨 앞 문서를 뒤로 보냄
            queue.append(queue.popleft())

# 결과 출력
for a in answer:
    print(a)
