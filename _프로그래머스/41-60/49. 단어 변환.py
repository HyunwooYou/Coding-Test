"""
* Title: 단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""
import heapq
from collections import defaultdict, deque

def dijkstra(dict_graph, start):
    INF = int(1e9)
    queue = []
    heapq.heappush(queue, (start, 0))
    dict_distance = defaultdict(int)

    for i in dict_graph.items():
        key = i[0]
        dict_distance[key] = INF

    dict_distance[start] = 0

    while queue:
        cur_node, cur_dist = heapq.heappop(queue)

        if dict_distance[cur_node] < cur_dist:
            continue

        adj_list = dict_graph[cur_node]

        for i in range(len(adj_list)):
            adj_tuple = adj_list[i]
            adj_node, adj_cost = adj_tuple
            new_cost = cur_dist + adj_cost

            if new_cost < dict_distance[adj_node]:
                dict_distance[adj_node] = new_cost
                heapq.heappush(queue, (adj_node, new_cost))

    return dict_distance

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
                cost = 1
                dict_graph[cur_node].append((compare_node, cost))

    distance_infos = dijkstra(dict_graph, begin)
    answer = distance_infos[target]

    return answer

begin = 'hit'
target = 'cog'

words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))