import sys

t = int(sys.stdin.readline())
ans = 'YES'
answer = []
for i in range(t):
    temp = []
   # k = sys.stdin.readline().strip()
    k = input()
    li = list(k)
    
    if li.count('(') != li.count(')'):
        answer.append('NO')
        continue
    elif li[0] == ')' or li[len(li)-1] == '(':
        answer.append('NO')
        continue
    
    for j in range(len(li)):
        
        if li[j] == '(':
            temp.append('(')
        elif li[j] == ')':
            if len(temp) == 0:
                answer.append('NO')
                break
            else:
                temp.pop()
        if j == len(li)-1 and len(temp) == 0:
            answer.append('YES')

for i in answer:
    print(i)