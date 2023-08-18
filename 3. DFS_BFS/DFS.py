"""
* Title: DFS

* Output
1 2 7 6 8 3 4 5
"""


def dfs(graph, cur_node, visited):
    # 현재 노드를 방문 처리
    visited[cur_node] = True
    print(cur_node, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for adjacent_node in graph[cur_node]:
        if not visited[adjacent_node]:
            dfs(graph, adjacent_node, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
