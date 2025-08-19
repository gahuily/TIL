import sys
sys.stdin = open('sample_input.txt', 'r')


def make_set(N):
    return [i for i in range(N+1)]


def find_set(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    parent = make_set(N)
    for idx in range(0, len(paper), 2):
        union(paper[idx], paper[idx+1])
    result = list(set(parent))
    print(f'#{tc} {len(result)}')
