def convert_to_decimal(number, base):
    multiplier, result = 1, 0

    while number > 0:
        result = result + number % 10 * multiplier
        multiplier = multiplier * base
        number = number // 10

    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("테스트 완료")

if __name__ == "__main__":
    test_convert_to_decimal()
    print(convert_to_decimal(100, 9))
