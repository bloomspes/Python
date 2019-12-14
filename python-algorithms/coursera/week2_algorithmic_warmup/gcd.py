def gcd(a, b):
    # b가 0이 될때까지 반복 작업 수행
    if b == 0:
        return b
    while b:
        # b를 a에 대입
        # a를 b로 나눈 나머지를 y에 대입
        a, b = b, a%b
    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))


print(gcd(86, 42))