import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
tree = [0] * (T+1)
for _ in range(T):
    num_list = list(input().split())
    print(num_list[0])
    # tree[num_list[0]] = num_list[1]

print(tree)