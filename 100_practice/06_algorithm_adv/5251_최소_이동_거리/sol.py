import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(T):
    edges = []
    N, E = map(int, input().split())
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))
    print(edges)