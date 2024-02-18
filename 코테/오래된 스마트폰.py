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


def dfs(index, cur): # 숫자버튼으로 만들 수 있는 수(세 자리 이하)
    if index == 3:
        return

    for num in num_input:
        new_num = cur * 10 + num
        d[new_num] = index + 1  # 클릭 횟수를 배열에 담는다.
        q.append(new_num)           # 큐에 담는다.
        nums.append(new_num)        # 숫자들을 담아준다.

        dfs(index + 1, new_num)


t = int(input())
for tc in range(1, t + 1):
    n, o, m = map(int, input().split())
    num_input = list(map(int, input().split()))
    oper_input = list(map(int, input().split()))
    nums = []
    w = int(input())

    inf = int(1e9)
    d = [inf] * 1000
    q = deque()
    dfs(0, 0)

    if d[w] < inf: # 숫자만 눌러서 만들 수 있는 경우
        print(f'#{tc} {d[w]}')
        continue

    while q:
        cur = q.popleft()

        for num in nums:
            new_cnt = d[cur] + len(str(num)) + 1  # 1은 연산 횟수를 의미

            if new_cnt >= m: # Enter 연산 고려
                continue

            for oper in oper_input:
                new_num = calc(oper, cur, num)

                if new_num == -1:
                    continue

                if new_cnt < d[new_num]:
                    d[new_num] = new_cnt
                    q.append(new_num)


    if d[w] < inf:
        print(f'#{tc} {d[w] + 1}')
    else:
        print(f'#{tc} -1')

