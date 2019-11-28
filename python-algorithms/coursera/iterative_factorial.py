# 단순 팩토리얼 계산
# python 3

def factorial(n):
    result = 1
    if n == 0:
        return result
    else:
        for i in range(1, n+1):
            result = result * i
    return result

def recursive(n):
    result = 1
    if n == 0:
        return result
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(5))
    print(factorial(100))

    print(recursive(5))