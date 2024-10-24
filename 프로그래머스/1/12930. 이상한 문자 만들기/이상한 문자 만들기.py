def solution(s):
    s = list(s.split(' '))

    answer = []

    for i in range(len(s)):
        ss = list(s[i])
        for j in range(len(ss)):
            if j % 2 == 0:
                ss[j] = ss[j].upper()
            else:
                ss[j] = ss[j].lower()
        x = ''.join(ss)
        answer.append(x)
    total = ''
    for i in range(len(answer)):
        total+=answer[i]
        if i != len(answer)-1:
            total+=' '
    return total