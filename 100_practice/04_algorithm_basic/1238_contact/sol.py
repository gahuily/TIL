import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def BFS_last_contact(start_vertex):
    visited = set()
    queue = deque()
    queue.append((start_vertex, 0))
    visited.add(start_vertex)

    depth_dict = {}

    max_depth = 0
    while queue:
        node, depth = queue.popleft()
        
        if depth not in depth_dict:
            depth_dict[depth] = []
        depth_dict[depth].append(node)

        max_depth = max(max_depth, depth)

        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

    last_nodes = depth_dict[max_depth]
    return max(last_nodes)


# result = BFS_last_contact(2)
# print(f"BFS 마지막 도달 노드: {result}")

tc = 0

try:
    while True:
        tc += 1
        N, S = map(int, input().split())
        num_list = list(map(int, input().split()))

        start = []
        end = []
        for idx in range(0, len(num_list), 2):
            start.append(num_list[idx])
            end.append(num_list[idx+1])

        nodes = set(start + end)

        adj_list = {node: [] for node in nodes}
        for idx in range(len(start)):
            u = start[idx]
            v = end[idx]
            adj_list[u].append(v)

        result = BFS_last_contact(S)
        print(f"#{tc} {result}")
except EOFError:
    pass