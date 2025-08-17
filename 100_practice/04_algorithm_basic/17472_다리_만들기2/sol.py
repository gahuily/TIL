import sys
from collections import deque


# Union-Find 관련 함수들은 그대로 사용
# find_parent, union_parent 함수는 여기에 포함
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# find_islands, find_bridges, kruskal 함수들도 그대로 사용
def find_islands(N, M, grid):
    island_num = 2
    visited = [[False] * M for _ in range(N)]
    islands = {}

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                islands[island_num] = []

                while q:
                    x, y = q.popleft()
                    grid[x][y] = island_num
                    islands[island_num].append((x, y))

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and \
                                grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

                island_num += 1
    return island_num - 2, islands


def find_bridges(N, M, num_islands, grid, islands):
    bridges = []

    for island_num, coords in islands.items():
        for x, y in coords:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                dist = 0

                while 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] != 0:
                        if grid[nx][ny] != island_num and dist >= 2:
                            bridges.append((dist, island_num, grid[nx][ny]))
                        break

                    nx += dx
                    ny += dy
                    dist += 1

    bridges = sorted(list(set(bridges)))
    return bridges


# def kruskal(num_islands, bridges):
#     parent = [i for i in range(num_islands + 2)]
#     total_cost = 0
#     num_edges = 0
#
#     for cost, u, v in bridges:
#         if find_parent(parent, u) != find_parent(parent, v):
#             union_parent(parent, u, v)
#             total_cost += cost
#             num_edges += 1
#
#     if num_edges == num_islands - 1:
#         return total_cost
#     else:
#         return -1


# # 메인 로직 수정
# def solve():
#     try:
#         # 첫 줄의 N, M을 입력받음
#         line1 = input()
#         if not line1:
#             return None
#         N, M = map(int, line1.split())
#
#         # N x M 격자를 입력받음
#         grid = [list(map(int, input().split())) for _ in range(N)]
#
#         num_islands, islands = find_islands(N, M, grid)
#
#         if num_islands <= 1:
#             return -1
#
#         bridges = find_bridges(N, M, num_islands, grid, islands)
#
#         result = kruskal(num_islands, bridges)
#         return result
#     except EOFError:
#         return None
#
#
# tc = 1
# while True:
#     answer = solve()
#     if answer is None:
#         break
#     print(f'{answer}')
#     tc += 1

from itertools import combinations

def solve_with_bruteforce(num_islands, bridges):
    min_cost = float('inf')

    # 2개부터 모든 다리까지 모든 조합을 시도
    for i in range(1, len(bridges) + 1):
        for combo in combinations(bridges, i):
            # 선택된 다리들로 모든 섬이 연결되는지 확인
            # Union-Find를 사용하여 연결 여부 확인
            parent = [j for j in range(num_islands + 2)]
            cost = 0
            edges = 0

            for c, u, v in combo:
                if find_parent(parent, u) != find_parent(parent, v):
                    union_parent(parent, u, v)
                    cost += c
                    edges += 1

            # 모든 섬이 연결되었을 때 (n-1개의 간선이 필요)
            if edges == num_islands - 1:
                min_cost = min(min_cost, cost)

    return min_cost if min_cost != float('inf') else -1

# 메인 로직
def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    num_islands, islands = find_islands(N, M, grid)

    if num_islands <= 1:
        return -1

    bridges = find_bridges(N, M, num_islands, grid, islands)

    result = solve_with_bruteforce(num_islands, bridges)
    return result


# 단일 테스트 케이스를 위한 호출
answer = solve()
print(answer)