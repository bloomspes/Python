# max pairwise integer 구하기
- 이 장에서는, 첫 번째 입력 * 두 번째 입력의 최댓값을 구하는 방법을 아래의 3단계를 통해 우리가 원하는 답으로 사고를 확장시켜 나간다.

## 1. Integer overflow 수정
## 2. 알고리즘 수정
## 3. 부하 테스트 수행 (Stress Test)
- What is a stress testing?
```
In general, it is a program that generates random tests in an infinite loop, and 
for each test, it launches your solution on this test and an alternative solution on the same test and compares the results.
```

- maximum pairwise integer를 구하기 위해, 두 번째 입력에서 정수의 list 크기를 늘리고, 할당되는 값은 rand() 함수에 의해 배분된다. 실행 횟수를 1000번으로 늘려서 테스트가 통과 되는지 혹은 어느 시점에서 테스트가 멈추는지를 살펴보는 점이다. 이렇게 테스트를 통과한 시점부터는 간단한 unit test 수행하여 code의 verification 단계를 마친다.