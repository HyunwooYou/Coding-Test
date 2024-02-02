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


def recur(cur, x): # 숫자버튼으로 만들 수 있는 수(세 자리 이하)
    if cur == 3:
        return

    for num in num_input:
        nxt_num = x * 10 + num
        visited[nxt_num] = cur + 1  # 클릭 횟수를 배열에 담는다.

        q.append(nxt_num)           # 큐에 담는다.
        nums.append(nxt_num)        # 숫자들을 담아준다.
        recur(cur + 1, nxt_num)


t = int(input())
for tc in range(1, t + 1):
    n, o, m = map(int, input().split())
    num_input = list(map(int, input().split()))
    oper_input = list(map(int, input().split()))
    nums = []
    w = int(input())

    INF = int(1e9)
    visited = [INF for _ in range(1000)]
    q = deque()
    recur(0, 0)

    if visited[w] < INF: # 숫자만 눌러서 만들 수 있는 경우
        print(f'#{tc} {visited[w]}')
        continue

    while q:
        cur = q.popleft()

        for num in nums:
            click_cnt = visited[cur] + 1 + len(str(num)) # 1은 연산 횟수를 의미

            if click_cnt >= m: # Enter 연산 고려
                continue

            for oper in oper_input:
                nxt = calc(oper, cur, num)
                if nxt == -1:
                    continue
                if click_cnt < visited[nxt]:
                    visited[nxt] = click_cnt
                    q.append(nxt)


    if visited[w] < INF:
        print(f'#{tc} {visited[w] + 1}')
    else:
        print(f'#{tc} -1')

