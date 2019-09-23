# 재귀 함수를 사용한 진법 변환

def convert_dec_to_any_base_rec(number, base):
    convertString = "012345679ABCDEF"
    if number < base:
        return convertString[number]

    else:
        return convert_dec_to_any_base_rec(number // base, base) \
            + convertString[number % base]
# 테스트 코드 작성
def test_convert_dec_to_any_base_rec():
    number = 9
    base = 2
    # assert는 뒤의 조건이 true가 아니면 assertError를 반환한다.
    # 성능을 높이기 위해, 반드시 정수를 입력받아 처리하는 경우 assert를 예외처리 대신 사용한다.
    assert(convert_dec_to_any_base_rec(number, base) == "1001")
    print("테스트 완료")

# main 함수를 분기하는 경우 == 함수로 부터 전달 받아야 하는 레퍼런스가 2가지 이상일 때

if __name__ == "__main__":
    test_convert_dec_to_any_base_rec()
    print(convert_dec_to_any_base_rec(number=8, base=2))