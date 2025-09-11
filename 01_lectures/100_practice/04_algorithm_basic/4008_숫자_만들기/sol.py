import sys
sys.stdin = open('sample_input.txt', 'r')

from itertools import permutations

def changing_oper(oper):
    new_operator = []
    for _ in range(oper[0]):
        new_operator.append('+')
    for _ in range(oper[1]):
        new_operator.append('-')
    for _ in range(oper[2]):
        new_operator.append('*')
    for _ in range(oper[3]):
        new_operator.append('/')
    return new_operator

def calc(formula):
    result = formula[0]
    for i in range(1, len(formula), 2):
        op = formula[i]
        next_num = formula[i + 1]
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num
        elif op == '*':
            result *= next_num
        elif op == '/':
            if result < 0:
                result = -(-result // next_num)
            else:
                result = result // next_num
    return result


T = int(input())                                # 테스트 케이스 수
for tc in range(1, T+1):                        # 테스트 케이스 입력
    N = int(input())                            # 수식에 사용될 숫자 개수
    oper = list(map(int, input().split()))      # 연산자 수 입력('+', '-', '*', '/' 순)
    num = list(map(int, input().split()))       # 수식에 사용될 숫자
    operator = changing_oper(oper)
    results = set()

    for comb in set(permutations(operator)):
        formula = [None] * (2 * N - 1)
        for i in range(N):
            formula[2*i] = num[i]
        for i in range(N-1):
            formula[2*i+1] = comb[i]
        value = calc(formula)
        results.add(value)

    print(f'#{tc} {max(results)-min(results)}')


# print(T)
# print(N)
# print(oper)
# print(num)


