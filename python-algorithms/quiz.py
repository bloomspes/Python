'''
함수 g(n)에 대해서

g(4) = 13,
g(n) = g(n-1) + gcd(n, g(n-1)) for n > 4
라고 정의할때

g(1 000) = 2524, g(1 000 000) = 2624152 입니다.
g(10^15)를 구할 수 있는 코드를 작성하십시오.
'''

# 최대공약수 구하는 재귀함수 로직 짜기

def gcd_method(x, y):

    if y == 0:
        return x
    return gcd_method(y, x%y)

print(gcd_method(2524, 2624152))

# 2524 와 2624152의 최대 공약수는 4 이다.
# 10^15 = 10^6^2 * 10^3
# g(gcd(10^3, 10^6)) = 13

def result(value):
    value = gcd_method(x, y*y)
    return value

