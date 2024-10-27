def solution(n, m):
    answer = []
    
    # 최대 공약수 구하기
    def gcd(n, m):
        for i in range(min(n, m), 0, -1):
            if n % i == 0 and m % i == 0:
                return i

    # 최소 공배수 구하기
    def lcm(n, m, gcd_value):
        return (n * m) // gcd_value

    # 최대 공약수 구하기
    gcd_value = gcd(n, m)
    answer.append(gcd_value)

    # 최소 공배수 구하기
    lcm_value = lcm(n, m, gcd_value)
    answer.append(lcm_value)

    return answer
