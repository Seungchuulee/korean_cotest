def solution(n, lost, reserve):
    # 전체 학생 목록
    ex1 = set([i + 1 for i in range(n)])  

    # 도난 목록
    ex2 = set(lost)

    # 여벌 목록
    exr = set(reserve)

    # 교집합 (여벌도 있고 도난도 당한 학생)
    ex3 = ex2 & exr  

    # 교집합 제거: 스스로 해결한 학생
    lost = sorted(ex2 - ex3)
    reserve = sorted(exr - ex3)

    # 체육복 있는 학생 (도난당하지 않은 사람)
    answer = n - len(lost)

    # 빌려준 사람 기록용
    used = set()

    # 여벌 학생들이 빌려주기
    for r in reserve:
        # 왼쪽 학생에게 먼저 빌려줌
        if r - 1 in lost:
            lost.remove(r - 1)
            answer += 1
        # 오른쪽 학생에게 빌려줌
        elif r + 1 in lost:
            lost.remove(r + 1)
            answer += 1

    return answer
