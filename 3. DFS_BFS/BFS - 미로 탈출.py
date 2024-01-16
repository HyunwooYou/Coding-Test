"""
* Title: BFS - 미로 탈출
졸은 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
졸의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 졸이 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

* Input
5 6
101010
111111
000001
111111
111111

* Output
10
"""
from collections import deque

n, m = map(int, input().split())
graph = []

dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

for _ in range(n):
    graph.append(list(map(int, input())))

def out_of_range(y, x):
    return y < 0 or x < 0 or y >= n or x >= m

def bfs(y, x):
    q = deque()
    q.append((y ,x))

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if out_of_range(ny, nx) or graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

    return graph[n - 1][m - 1]

print(bfs(0, 0))
