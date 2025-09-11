import sys
sys.stdin = open('sample_input.txt', 'r')


def binary_coefficient(n, b):
    dp = [[0 for _ in range(b+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(b+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][b]


T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    coef = binary_coefficient(n, b)
    print(f'#{tc} {coef}')
