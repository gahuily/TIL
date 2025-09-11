# 0~9 사이의 숫자 카드에서 임의의 카드 6 장을 뽑았을 때 ,
# 3 장의 카드가 연속적인 번호를 갖는 경우를 run 이라 하고 ,
# 3 장의 카드가 동일한 번호를 갖는 경우를 triplet 이라고 한다
#
# 그리고 , 6 장의 카드가 run 과 triplet 로만 구성된 경우를
# baby gin 으로 부른다
#
# 6 자리의 숫자를 입력 받아 baby gin 여부를 판단하는 프로그램을 작성하라
#
# [입력]
#
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=10
#
# 두번째줄에는 6장의카드의 숫자들이 주어진다.(예: 123456)
# 숫자는 1<=N<=.9 이다


from itertools import permutations
import sys
sys.stdin = open('input.txt', "r")

def is_run(arr):
    return (arr[0] + 2) == (arr[1] + 1) == (arr[2])

def is_triplet(arr):
    return arr[0] == arr[1] == arr[2]

def is_baby_gin(arr):
    for perm in permutations(arr):
        first_group = perm[:3]
        second_group = perm[3:]

        if (is_run(first_group)) == True:
            if (is_run(second_group) == True) or (is_triplet(second_group) == True):
                return True
        elif (is_triplet(first_group)) == True:
            if (is_run(second_group) == True) or (is_triplet(second_group) == True):
                return True
    return False

# 통과 안 됨.........
# T = int(input())
# for tc in range(1, T+1):
#     num_list = list(map(int, list(input())))
#     # print(num_list)
#     result = 'true' if is_baby_gin(num_list) else 'false'
#     print(f'{tc} {result}')

# 통과 됨.........
T = int(input())
for tc in range(1, T+1):
    num_str = input().strip()  # 문자열 입력 (예: "667767")
    if len(num_str) != 6:
        print(f"{tc} false")  # 입력 길이가 잘못된 경우 처리
        continue
    num_list = list(map(int, num_str))
    result = 'true' if is_baby_gin(num_list) else 'false'
    print(f'#{tc} {result}')