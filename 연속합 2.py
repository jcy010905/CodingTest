n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

dp[0][0] = arr[0]
dp[0][1] = arr[0]
result = arr[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])
    result = max(result, dp[i][0], dp[i][1])

print(result)