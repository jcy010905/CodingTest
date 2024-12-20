def solution(prices):
    answer = [0] * len(prices)  # 각 시점별로 유지되는 기간을 저장할 리스트
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:  # 가격이 떨어진 경우
                break  # 루프를 종료하고 다음 시점으로 이동
    
    return answer

print(solution([1, 2, 3, 2, 3]))