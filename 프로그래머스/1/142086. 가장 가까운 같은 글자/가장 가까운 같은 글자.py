def solution(s):
    answer = []
    example = list(s)
    
    result = [-1 for _ in range(len(example))]

    for i in range(len(s)):
    
        if s[i] not in answer:
            answer.append(s[i])
        else:
            
            for j in range(len(answer)-1,-1,-1):
                if answer[j] == s[i]:
                    result[i] = abs(i-j)
                    answer.append(s[i])
                    break
    
    
    return result