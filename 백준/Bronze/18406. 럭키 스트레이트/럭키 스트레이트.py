n = list(map(int, input()))

li = []
li2 = []

for i in range(len(n)//2):
    li.append(n[i])

for i in range(len(n)//2, len(n)):
    li2.append(n[i])

x = sum(li)
x2 = sum(li2)

if x == x2:
    print('LUCKY')
else:
    print('READY')

