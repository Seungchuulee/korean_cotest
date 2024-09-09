n, k = map(int, input().split())

li = [i + 1 for i in range(n)]
li2 = []

i = 0  # 시작 인덱스
while len(li) > 0:
    # 리스트가 순환하므로 k-1만큼 이동 후 현재 인덱스를 구함
    i = (i + k - 1) % len(li)
    li2.append(li.pop(i))  # 해당 인덱스의 값을 추가하고 리스트에서 제거


print('<', end='')
for i in range(len(li2)):
    if i == len(li2)-1:
        print(li2[i],end='')
    else:
        print(li2[i], end=', ')
print('>')