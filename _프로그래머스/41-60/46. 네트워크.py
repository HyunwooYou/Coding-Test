"""
* Title: 네트워크
https://school.programmers.co.kr/learn/courses/30/lessons/43162
"""
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(len(computers)):
        for j in range(i):
            if computers[i][j] == 0:
                continue
            now = i + 1
            adjacent = j + 1
            graph[now].append(adjacent)
            graph[adjacent].append(now)

    for i in range(1, n + 1):
        if visited[i]:
            continue
        bfs(graph, i, visited)
        answer += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))
