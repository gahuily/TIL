import sys
sys.stdin = open('sample_input.txt', 'r')


def max_price(N, size, price):
    dp = [0 for _ in range(N+1)]
    for idx in range(len(size)):
        for weight in range(N, size[idx]-1, -1):
            dp[weight] = max(dp[weight], price[idx]+dp[weight-size[idx]])
            '''
                dp[weight]: 이전 idx(item)으로 계산해둔 최적해
                price[idx]: 현재 idx를 선택했을 경우의 가치
                dp[weight-size[idx]]: 순회 중인 weight에서 현재 idx를 선택하고
                                      남은 size로 선택할 수 있는 최적해
                즉, 현재 dp[weight] 값을 기존 값과 새 idx를 선택했을 때의 값 중
                큰 값으로 선택하는 것
            '''
    return dp[N]


T = int(input())
for tc in range(1, T+1):
    # N: 박스 크기, M: 상품 개수
    N, M = map(int, input().split())
    size = []
    price = []
    for _ in range(M):
        # S: 각 상품의 크기, P: 각 상품의 가격
        S, P = map(int, input().split())
        size.append(S)
        price.append(P)
    result = max_price(N, size, price)
    print(f'#{tc } {result}')
