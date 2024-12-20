def solution(progresses, speeds):
    answer = []
    x = 1
    beforeValue = 0
    for i in range(len(progresses)):
        if (100 - progresses[i])%speeds[i] == 0:
            returnValue = (100 - progresses[i])//speeds[i]
        else:
            returnValue = (100 - progresses[i])//speeds[i]+1
        if i==0:
            beforeValue = returnValue
            answer.append(x)
        else:
            if beforeValue>=returnValue:
                x+=1
                answer[-1]=x
            else:
                beforeValue=returnValue
                x=1
                answer.append(x)
    return answer