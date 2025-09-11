import sys
sys.stdin = open('sample_input.txt', 'r')


'''
# kruscal 알고리즘
def find_parent(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_x != root_y:
        parent[root_y] = root_x


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    # print(edges)          # [(1, 2, 1), (2, 3, 2), (1, 3, 3)]
    parent = [i for i in range(V+1)]
    edges.sort(key=lambda x: x[2])
    weight = 0
    edge = 0
    for x, y, w in edges:
        if find_parent(x) != find_parent(y):
            union(x, y)
            weight += w
            edge += 1
        if edge == V-1:
            break
    print(f'#{tc} {weight}')
'''

# prim 알고리즘


def prim():
    pass


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]