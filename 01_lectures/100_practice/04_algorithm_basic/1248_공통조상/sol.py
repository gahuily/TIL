import sys
sys.stdin = open('input.txt', 'r')

# 정점 수와 간선 수, 간선의 정보를 통해 트리를 구성하는 함수
def create_tree(V, E, E_list):
    parent = [0] * (V + 1)                  # [0, 0, ... , 0]
    children = [[] for _ in range(V + 1)]   # [[], [], ... , []]
    for idx in range(0, len(E_list), 2):
        p = E_list[idx]
        c = E_list[idx+1]
        parent[c] = p                       # [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]
        children[p].append(c)               # [[], [2, 3], [4], ... , []]
    return parent, children

# 노드의 조상을 저장하는 함수
def node_ancestor(vertex, parent):
    ancestor = []
    while vertex != 0:
        ancestor.append(vertex)
        vertex = parent[vertex]
    return ancestor

# 두 조상 리스트를 비교하여 가장 가까운 공통 조상 찾는 함수
def common_ancestor(X_anc, Y_anc):
    common = 0
    X_anc.reverse()
    Y_anc.reverse()
    idx = 0
    while idx < min(len(X_anc), len(Y_anc)) and X_anc[idx] == Y_anc[idx]:
        common = X_anc[idx]
        idx += 1
    return common

# 정점 기준 전위순회로 subtree 크기 구하는 함수
def preorder_subtree(vertex, children):
    size = 1
    for node in children[vertex]:
        size += preorder_subtree(node, children)
    return size

T = int(input())
for tc in range(1, T+1):
    V, E, X, Y = map(int, input().split())
    E_list = list(map(int, input().split()))
    parent, children = create_tree(V, E, E_list)
    X_anc = node_ancestor(X, parent)
    Y_anc = node_ancestor(Y, parent)
    common = common_ancestor(X_anc, Y_anc)
    subtree_size = preorder_subtree(common, children)
    print(f'#{tc} {common} {subtree_size}')
