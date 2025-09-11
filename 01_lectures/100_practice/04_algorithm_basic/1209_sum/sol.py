# sys
import sys
# open을 사용해서 input 파일을 연다
sys.stdin = open('input.txt')

# # 이 문제는 10개의 TC를 가진다.
# for _ in range(10):
#     tc = int(input())    # 테스트케이스 번호 입력
#     # 입력 받은 문자열을 공백 기준으로 쪼개서 정수로 바꾼 다음 리스트에 담는 걸 100번 반복
#     data = [list(map(input().split())) for _ in range(100)]
#     print(data)
#     # 각 행마다 가진 값들을 더한다.
#     # 각 열마다 가진 값들을 더한다.
#     # 대각선의 값들을 더한다.
#     # 그 모든 값들 중 제일 큰 값을 구한다. -> max 금지

# # 100 x 100을 2차원 리스트로 받아야 한다.
# # 즉, 한 번 입력 받은 한 줄에 100개의 숫자가 공백을 기준으로 문자열로 오게 됨
#     # 이걸 100번 반복해야 함.
# tc = int(input())
# data = []   # 2차원 배열을 만들기 위한 리스트
# for _ in range(100):
#     tmp_list = input().split()  # 공백 기준으로 쪼개서 리스트로 만듦
#     # 공백 기준으로 쪼개진 문자열 (ex '13', '24')를 정수로 바꿔야 함
#     map_data = map(int, tmp_list)
#     # 리스트로 만들어야 함
#     map_to_list_data = list(map_data)
#     # data.append(tmp_list)       # 그 리스트를 data에 추가
#     data.append(map_to_list_data)
# # print(data)
# # print(len(data))

# 각 행의 합의 최대를 구하는 함수
def row_sum_max(data):
    sum_max = 0
    row_sum = 0
    for idx in range(len(data)):
        row_sum = sum(data[idx])
        # sum_max = max(sum_max, row_sum)
        if row_sum > sum_max:
            sum_max = row_sum
    return sum_max

# 각 열의 합의 최대를 구하는 함수
def col_sum_max(data):
    col_sum = [0] * 100
    for i in range(len(data)):
        for j in range(len(data)):
            col_sum[j] += data[i][j]
    # return max(col_sum)
    sum_max = 0
    for val in col_sum:
        if val > sum_max:
            sum_max = val
    return sum_max


def diag_sum_max(data):
    diag_max = 0
    right_down = 0
    right_up = 0
    for i in range(100):
        right_down += data[i][i]
        right_up += data[i][99-i]
    # diag_max = max(right_down, right_up, diag_max)
    if right_down > diag_max:
        diag_max = right_down
    if right_up > diag_max:
        diag_max = right_up
    return diag_max

while True:
    try:
        T = int(input())
        max_val = 0
        data = []
        for _ in range(100):
            arr = list(map(int, input().split()))
            data.append(arr)
        row_max = row_sum_max(data)
        col_max = col_sum_max(data)
        diag_max = diag_sum_max(data)
        # max_val = max(row_max, col_max, diag_max)
        max_val = row_max
        if col_max > max_val:
            max_val = col_max
        if diag_max > max_val:
            max_val = diag_max
        print(f'#{T} {max_val}')
    except EOFError:
        break