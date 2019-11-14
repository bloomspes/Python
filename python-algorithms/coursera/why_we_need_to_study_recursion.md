# Recursive Algorithm

## Recursive function 이란?
- 어떤 함수 내에서 함수 자기 자신을 호출하는 함수를 재귀함수라고 부릅니다. 재귀 알고리즘을 사용하면 하노이의 탑과 그래프의 DFS 같은 문제를 쉽게 풀 수 있습니다.

## How memory is allocated to different function calls in recursion?
- main()에서 호출된 함수들은 스택상에 메모리를 적재합니다. 재귀 함수는 자기 자신을 호출하고, 호출된 함수의 메모리는 호출 중인 함수에 할당 된 메모리 위에 할당되며 각 함수 호출마다 다른 지역 변수 사본이 생성됩니다 base case에 카운팅 되면, 함수는 고유 값을 리턴하고 메모리는 해제됩니다. 그리고 프로세스가 계속 이어집니다.

```
# A Python 3 program to 
# demonstrate working of 
# recursion 
  
def printFun(test): 
  
    if (test < 1): 
        return
    else: 
      
        print( test,end = " ") 
        printFun(test-1) # statement 2 
        print( test,end = " ") 
        return
      
  
test = 3
printFun(test) 
```
**Output :**
```
3 2 1 1 2 3
```

- printFun(3) 함수가 메인 함수에 의해 호출되면 메모리는 printFun(3)에 할당 됩니다. 그리고 지역 변수인 test는 3으로 초기화가 됩니다. statement 1 부터 4까지 메모리는 스택위에 쌓이게 됩니다. 그리고 첫 출력문인 3이 찍히게 됩니다. statement 2 에서, printFun(2)가 호출되고 다시 위의 과정을 반복합니다. 이처럼 printFun(2)는 연속적으로 printFun(1)을 호출하고 printFun(1)은 printFun(0)을 호출합니다. 이 때, printFun(0)는 if 조건문으로 돌아가 다시 printFun(1)을 반환합니다.



## Factorial 구하기
- Recursion 알고리즘을 설명할 때, 가장 베이스가 되는 수학 이론.
- Recursive algorithm 개념을 이해하기에 적합하다.
- for 문으로 n!을 구하는 것을 시작으로 Fibonacci와 GCD 계산으로 생각을 확장 시켜 나가는 것이 좋다.
- 해당 loop가 함수 안에서 돌 때, 각각의 변수는 초기화가 필요한 상황 인지 판단 하는 습관이 중요하다. 이를 달리 말하면, 내가 짠 코드가 어떤 동작을 거쳐서 결과를 출력하는 지 생각하는 연습을 들이는 것과 같다.

- factorial 구하는 알고리즘은 다음과 같다.
```
def factorial(n):
    result = 1
    if n == 0:
        return result
    else:
        for i in range(1, n+1):
            result = result * i
    return result

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(5))
    print(factorial(100))

```

- 이를 recursive 하게 바꾼다면, 코드를 다음과 같이 구현할 수 있다.

```
def recursive(n):
    result = 1
    if n == 0:
        return result
    else:
        return n * factorial(n-1)
```

## Fibonacci
- Factorial 구하기의 확장 편 이라고 생각하면 좋다.
- 항상 기본이 되는 개념을 바탕으로 응용 하는 것이 좋다.
- 피보나치 함수의 식을 if 조건문으로 반환 하면 다음과 같다.
```
if n <= 1:
    return n

else:
    return F(n-1) + F(n-2) +3
```

## GCD 구하기
### What is a GCD?
- for integers, a and b, either greatest common divisor or gcd(a, b) is the largest integer d so that d divides both a and b.

- G(a, b)는 a_prime = a%b 일 때, G(b, a_prime)으로 구할 수 있습니다.

### Runtime 문제 해결하기
- Each step reduces the size of numbers by about a factor of 2.
- Takes about log(ab) steps.
- GCDs of 100 digit numbers takes about 600 steps.
- Each step a single division.

## LCM 구하기
### What is a LCM?
- for integers, a and b, either least common multiple or lcm(a, b) is the smallest number L so that L is a multiples b and divides gcd(a, b)

## Divide and Conquer
### 분할 정복 이론은 큰 범주에서의 재귀와 같습니다.

- (그림 및 코드 추가 예정)