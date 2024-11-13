import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
li = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
li.sort()

# 산술평균
print(round(sum(li) / len(li)))

# 중앙값
print(li[len(li) // 2])

# 최빈값
frequency = Counter(li).most_common()
frequency.sort(key=lambda x: (-x[1], x[0]))  # 빈도수 내림차순, 숫자 오름차순

if len(frequency) > 1 and frequency[0][1] == frequency[1][1]:  # 최빈값이 여러 개일 경우
    print(frequency[1][0])
else:
    print(frequency[0][0])

# 범위
print(max(li) - min(li))
