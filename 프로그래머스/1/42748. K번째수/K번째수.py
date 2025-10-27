def solution(array, commands):
    answer = []
    
    for k in range(len(commands)):
        li1 = array[commands[k][0]-1:commands[k][1]]
        li1.sort()
        answer.append(li1[commands[k][2]-1])
    return answer