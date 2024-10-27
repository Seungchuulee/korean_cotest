def solution(s):
    answer = True
    li = list(s)
    temp = []
    
    if li.count('(') != li.count(')'):
        answer = False
        return answer
    elif li[0] == ')' or li[len(li)-1] == '(':
        answer = False
        return answer
    
    for i in range(len(li)):
        if len(temp) == 0 and li[i] ==  ')':
            answer = False
            break
        
        if li[i] == '(':
            temp.append(li[i])
        elif li[i] == ')':
            temp.pop()
    
        if i == len(li)-1 and len(temp) == 0:
            break
        if i == len(li)-1 and len(temp) > 0:
            answer = False
    
    

    return answer