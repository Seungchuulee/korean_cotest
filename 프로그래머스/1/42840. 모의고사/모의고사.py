def solution(answers):
    num1 = [1,2,3,4,5]

    # 2번 수포자
    num2 = [2,1,2,3,2,4,2,5]

    # 3번 수포자
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    count1 = 0
    count2 = 0
    count3 = 0

    li = []

    start1 = 0
    start2 = 0
    start3 = 0
    
    # 1번 수포자
    for i in range(len(answers)):
        if answers[i] == num1[start1]:
            count1 += 1
        if start1+1 == len(num1):
            start1 = 0
        else:
            start1 += 1

    # 2번 수포자
    for i in range(len(answers)):
        if answers[i] == num2[start2]:
            count2 += 1
        if start2+1 == len(num2):
            start2 = 0
        else:
            start2 += 1

    # 3번 수포자
    for i in range(len(answers)):
        if answers[i] == num3[start3]:
            count3 += 1
        if start3+1 == len(num3):
            start3 = 0
        else:
            start3 += 1
        
    li = [count1, count2, count3]

    x = max(li)
    ans = []
    for i in range(len(li)):
        if li[i] == x:
            ans.append(i+1)

    return ans
