"""
* Title: 단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""
import heapq
from collections import defaultdict, deque

def dijkstra(dict_graph, start):
    queue = []
    heapq.heappush(queue, (start, 0))
    dict_distance = defaultdict(int)
    dict_distance[start] = 0

    while queue:
        dist, popped_node = heapq.heappop(queue)
        if dict_distance[popped_node] < dist:
            continue
        adjacent_list = dict_graph[popped_node]

        for i in range(len(adjacent_list)):
            adjacent_node = adjacent_list[i]
            cost = dist + 1
            if cost < dict_distance[adjacent_node]:
                dict_distance[adjacent_node] = cost
                heapq.heappush(queue, (adjacent_node, cost))

    print(dict_distance)


def bfs_shortest_path(dict_graph, cur_node, dict_visited):
    queue = deque([cur_node])
    dict_visited[cur_node] = True

    while queue:
        popped_node = queue.popleft()
        adjacent_list = dict_graph[popped_node]
        # print(popped_node)

        for i in range(len(adjacent_list)):
            adjacent_node = adjacent_list[i]
            if not dict_visited[adjacent_node]:
                queue.append(adjacent_node)
                dict_visited[adjacent_node] = True

def is_adjacent_node(cur_node, compare_node):
    count = 0
    node_len = len(cur_node)

    for i in range(node_len):
        if cur_node[i] == compare_node[i]:
            count += 1

    if node_len - 1 == count:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    dict_graph = defaultdict(list)
    dict_visited = defaultdict(bool)
    words.append(begin)

    for i in range(len(words)):
        cur_node = words[i]
        dict_visited[cur_node] = False
        for j in range(len(words)):
            if i == j:
                continue
            compare_node = words[j]
            if is_adjacent_node(cur_node, compare_node):
                dict_graph[cur_node].append(compare_node)

    bfs_shortest_path(dict_graph, begin, dict_visited)
    dijkstra(dict_graph, begin)

    return answer

begin = 'hit'
target = 'cog'

words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))