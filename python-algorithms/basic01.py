# 함수 알고리즘 비교

# 연산자 사용 시에, 중복되는 알고리즘이 없는지 생각하고 사용 할 것.
# 무조건 짧은 코드가 효율이 좋은 것은 아니다.
# 컴파일 혹은 번역하는 과정에서 같은 알고리즘이 중복되어 계산될 수 있기 때문에 그렇다.

def midvalue(x, y, z):

    if x >= y:

        if y >= z:
            return y
        elif x <= z:
            return x
        else:
            return z

    elif x > z:
        return x
    elif y > z:
        return z
    else:
        return y

# main 함수 분기

if __name__ == "__main__":
    
    print("세 정수의 중앙값을 구합니다. \n")
    x, y, z = map(int, input().split(" "))
    print(midvalue(x, y, z))
