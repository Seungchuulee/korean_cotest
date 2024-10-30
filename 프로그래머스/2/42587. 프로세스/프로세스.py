from collections import deque

def solution(priorities, location):
    

    li = []

    for i in range(len(priorities)):
        li.append([priorities[i], i])

    queue = deque(li)
    count = 0

    while True:
        maxNum = max(queue, key=lambda x: x[0])[0]
    

        # 우선순위가 가장 높다면.
        if queue[0][0] == maxNum:
            # location과 일치하면 종료
            if queue[0][1] == location:
                count += 1
                break
            else:
                queue.popleft()
                count += 1
            
        else:
            # 우선순위가 낮으면 뒤로 보냄
            x = queue.popleft()
            queue.append(x)
        

    return count
