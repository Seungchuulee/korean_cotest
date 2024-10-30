def solution(s):
    li = list(s)
    
    temp = []
    answer = True

    if li.count(')') != li.count(')'):
        answer = False
    elif li[0] == ')' or li[-1] == '(':
        answer = False
    else:
        for i in li:
            if i == '(':
                temp.append('(')
            else:
                if len(temp) == 0:
                    answer = False
                    break
                else:
                    temp.pop()
    if len(temp) != 0:
        answer = False

    return answer