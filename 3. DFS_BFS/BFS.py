"""
* Title: BFS

* Output
1 2 3 8 7 4 5 6
"""
from collections import deque

# BFS 메서드 정의
def bfs(graph, cur_node, visited):
    # 큐(Queue), 구현을 위해 deque 라이브러리 사용
    queue = deque([cur_node])
    # 현재 노드를 방문 처리
    visited[cur_node] = True

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        popped_node = queue.popleft()
        print(popped_node, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for adjacent_node in graph[popped_node]:
            if not visited[adjacent_node]:
                queue.append(adjacent_node)
                visited[adjacent_node] = True

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

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

