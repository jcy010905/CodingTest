def solution(num):
    answer = 0 # 횟수를 0으로 설정
    while(num != 1): # 값이 1일 때 까지
        if answer == 500: # 횟수가 500이 되면 
            return -1 # -1 리턴
        if (num % 2) == 0: # 값이 짝수이면
            num /= 2 # 값을 2로 나눔
        else: # 아니면(홀수 이면)
            num = num*3+1 #값을 3으로 곱하고 1을 더함
        answer += 1 # 횟수 증가
    return answer # 횟수 리턴