# Python Fraction 모듈 간단히 사용하기

from fractions import Fraction

def rounding_floats(x, places):
    return round(x, places)

def float_to_fractions(number):
    return Fraction(*number.as_integer_ratio())

def get_denominator(x, y):
    # 분모 반환
    a = Fraction(x, y)
    return a.denominator

def get_numerator(x, y):
    # 분자 반환
    a = Fraction(x, y)
    return a.numerator

# 테스트 코드 작성
def test_testing_floats():
    x = 1.25
    y = 1
    x2 = -1
    y2 = 5/4
    z = 6

    assert(rounding_floats(x, y) == 1.2)
    assert(rounding_floats(x*10, x2) == 10)
    assert(float_to_fractions(x) == y2)
    assert(get_denominator(y, z) == z)
    assert(get_numerator(y, z) == y)
    print("테스트 완료")

if __name__ == "__main__":
    test_testing_floats()