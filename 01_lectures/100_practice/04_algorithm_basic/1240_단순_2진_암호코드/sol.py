import sys

# 예제 입력 (코드 제출 시 제외할 부분)
sys.stdin = open('input.txt', 'r')

code_map = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

def solve():
    # N, M 입력
    N, M = map(int, input().split())
    # 2차원 배열 입력
    arr = [input().strip() for _ in range(N)]

    found = False
    # 2차원 배열 순회하며 마지막으로 1이 나타난 인덱스 저장
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                end_idx = j
                # 마지막 1이 나타난 지점부터 56개의 문자열 code에 저장
                code = arr[i][(end_idx - 55):(end_idx + 1)]
                # Gemini 첨언
                found = True
                break
        if found:
            break
    # Gemini 첨언) 만약 찾은 암호코드가 없다면 0 반환
    if not found:
        return 0

    # num_list: code에서 7개씩 슬라이싱한 문자열 암호 코드 숫자 저장
    num_list = []
    for idx in range(0, 56, 7):
        seven_bits = code[idx : idx + 7]
        code_number = code_map[seven_bits]
        num_list.append(code_number)

    odd_sum = 0
    even_sum = 0
    # num_list에 저장한 암호 코드로 odd_num, even_num 계산
    for idx in range(8):
        if idx % 2 == 0:
            odd_sum += num_list[idx]
        else:
            even_sum += num_list[idx]

    result = (odd_sum * 3) + even_sum
    # odd_num과 even_num을 통해 result 계산
    # result를 통해 올바른지 잘못됐는지 확인
    if result % 10 == 0:
        return sum(num_list)
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    answer = solve()
    print(f'#{tc} {answer}')
