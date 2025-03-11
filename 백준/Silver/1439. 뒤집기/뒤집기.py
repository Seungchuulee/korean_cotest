# 문자열 뒤집기
import sys
li = list(sys.stdin.readline().rstrip())

li2 = []

k = li[0]
# 연속해서 나오면 취급하지 않고, 숫자가 바뀔때마다 이전 수를 저장
for i in range(1, len(li)):
    if li[i-1] == li[i]:
        
        if i == len(li)-1 :
            li2.append(li[i])
        else:
            continue
    else:
        li2.append(li[i-1])
        
        if i == len(li)-1:
            li2.append(li[i])




c1 = li2.count('0') # 0의 등장횟수 구하기
c2 = li2.count('1') # 1의 등장횟수 구하기
li3 = [c1,c2]

'''
반례 : 100100
정답 : 2
'''

answer = 0
# 0과 1이 담긴 리스트의 길이에 따라 변경횟수 구하기 (최소가 나오는게 우선)
for i in range(len(li2)):
    if len(li2) == 1:
        break
    elif len(li2) == 2:
        answer = 1
    else:
        answer = min(li3)

print(answer)