def solution(numbers, target):
    if not numbers and target == 0 : # 값이 0일때
        return 1
    elif not numbers: # 값이 0이 안나왔을 때
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
