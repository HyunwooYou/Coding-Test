def solution(id_list, report, k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    counter = defaultdict(int)

    for r in report:
        # report의 첫번째 값은 신고자 id, 두번쨰 값은 신고당한 id
        reporter, assignee = r.split()
        # 신고자가 신고한 id 추가
        user[reporter].add(assignee)
        # 신고당한 id의 신고 횟수 추가
        counter[assignee] = counter[assignee] + 1

    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if counter[u] >= k:
                result += 1
        answer.append(result)

    return answer
