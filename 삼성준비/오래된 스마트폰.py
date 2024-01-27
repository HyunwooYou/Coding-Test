from collections import deque


# 1 : '+',  2 : '-',  3 : '*',  4 : '/'
def calc(oper, num, num2):
    if oper == 1:       # 더하기
        num += num2
    elif oper == 2:     # 빼기
        num -= num2
    elif oper == 3:     # 곱하기
        num *= num2
    elif oper == 4:     # 나누기
        if num2 == 0:
            return -1
        num //= num2
    if 0 <= num < 1000:
        return num
    else:
        return - 1


def recur(cur, x):
    if cur == 3:
        return

    for num in num_input:
        nxt_num = x * 10 + num
        if visited[nxt_num] <= cur + 1:
            continue
        visited[nxt_num] = cur + 1
        q.append(nxt_num)
        nums.append(nxt_num)
        recur(cur + 1, nxt_num)


t = int(input())
for tc in range(1, t + 1):
    n, o, m = map(int, input().split())
    num_input = list(map(int, input().split()))
    oper_input = list(map(int, input().split()))
    nums = []
    w = int(input())
    INF = m + 1
    visited = [INF for _ in range(1000)]
    q = deque()
    recur(0, 0)

    if visited[w] < INF:
        print(f'#{tc} {visited[w]}')
        continue

    while q:
        cur = q.popleft()
        for num in nums:
            click_cnt = visited[cur] + len(str(num)) + 1
            if click_cnt + 1 > m:
                continue
            for oper in oper_input:
                nxt = calc(oper, cur, num)
                if nxt == -1:
                    continue
                if visited[nxt] <= click_cnt:
                    continue
                visited[nxt] = click_cnt
                q.append(nxt)


    if visited[w] < INF:
        print(f'#{tc} {visited[w] + 1}')
    else:
        print(f'#{tc} -1')

