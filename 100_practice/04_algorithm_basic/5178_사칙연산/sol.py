import sys
sys.stdin = open('sample_input.txt', 'r')

# T = int(input())                                # T: 테스트 케이스 수
# test_case = list(map(int, input().split()))     # N(노드 수), M(리프 노드 수), L(출력할 노드 번호)
# leaf_idx = []
# leaf_value = []
# for idx in range(test_case[1]):
#     a, b = map(int, input().split())
#     leaf_idx.append(a)
#     leaf_value.append(b)

# # 후위 순회
# def postorder_traversal(N, idx):
#     if idx <= N:
#         postorder_traversal(N, idx * 2)
#         postorder_traversal(N, idx * 2 + 1)
#         # print(tree[idx], end=' ')

# # postorder_traversal(1)

# def parent_node(idx, tree):
#     left_child = idx * 2
#     right_child = idx * 2 + 1
#     sum = tree[left_child] + tree[right_child]
#     tree[idx] = sum

def postorder_traversal(N, idx, tree):
    if idx > N:
        return 0

    # 왼쪽, 오른쪽 자식 값을 재귀적으로 계산
    left = postorder_traversal(N, idx * 2, tree)
    right = postorder_traversal(N, idx * 2 + 1, tree)

    # 현재 노드가 리프 노드가 아니면 자식 합 저장
    if idx * 2 <= N:
        tree[idx] = left + right

    return tree[idx]


# def sum_of_node(test_case, leaf_idx, leaf_value):
#     N = test_case[0]
#     M = test_case[1]
#     L = test_case[2]
#     tree = [0] * (N+1)                          # tree 구조 생성
#     for i in range(M):                          # leaf nod 값 채우기
#         tree[leaf_idx[i]] = leaf_value[i]
#     # print(tree)
#     if not postorder_traversal(N, idx):
#         parent_node(idx, tree)
#     print(tree)

# sum_of_node(test_case, leaf_idx, leaf_value)

# result = []
# def sum_of_node(test_case, leaf_idx, leaf_value):
#     N = test_case[0]  # 총 노드 개수
#     M = test_case[1]  # 리프 노드 개수
#     L = test_case[2]  # 출력할 노드 번호

#     tree = [0] * (N + 1)

#     # 리프 노드 값 채우기
#     for i in range(M):
#         tree[leaf_idx[i]] = leaf_value[i]

#     # 트리 계산
#     postorder_traversal(N, 1, tree)

#     result.append(tree[L])

def solve():
    T = int(input())
    for t in range(1, T + 1):
        N, M, L = map(int, input().split())
        tree = [0] * (N + 1)

        for _ in range(M):
            idx, val = map(int, input().split())
            tree[idx] = val

        postorder_traversal(N, 1, tree)
        print(f"#{t} {tree[L]}")

solve()


# T = int(input())                                # T: 테스트 케이스 수

# test_case = []
# leaf_idx = []
# leaf_value = []
# for tc in range(1, T+1):
#     test_case = list(map(int, input().split()))     # N(노드 수), M(리프 노드 수), L(출력할 노드 번호)
#     for idx in range(test_case[1]):
#         a, b = map(int, input().split())
#         leaf_idx.append(a)
#         leaf_value.append(b)

# sum_of_node(test_case, leaf_idx, leaf_value)

# for i in range(T):
#     print(f'#{i+1} {result[i]}')