def exercise_1():
    pass


def exercise_2():
    # 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
    def fahrenheit_to_celsius(fahrenheit):
        pass
        # 코드를 입력하세요.

    temperature_list = [40, 15, 32, 64, -4, 11]
    print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

    # 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
    print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력


def exercise_3():
    # 원화(￦)에서 달러($)로 변환하는 함수
    def krw_to_usd(krw):
        # 코드를 입력하세요.
        pass

    # 달러($)에서 엔화(￥)로 변환하는 함수
    def usd_to_jpy(usd):
        # 코드를 입력하세요.
        pass

    # 원화(￦)으로 각각 얼마인가요?
    prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
    print("한국 화폐: " + str(prices))

    # prices를 원화(￦)에서 달러($)로 변환하기
    # 코드를 입력하세요.

    # 달러($)로 각각 얼마인가요?
    print("미국 화폐: " + str(prices))

    # prices를 달러($)에서 엔화(￥)으로 변환하기
    # 코드를 입력하세요.

    # 엔화(￥)으로 각각 얼마인가요?
    print("일본 화폐: " + str(prices))


def exercise_4():
    pass


def exercise_5():
    # 투표 결과 리스트
    votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', '최만수', '김영자', '최만수', '김영자',
             '김영자', '최만수', '최만수', '최만수', '강승기', '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기',
             '김영자']

    # 후보별 득표수 사전
    vote_counter = {}

    # 리스트 votes를 이용해서 사전 vote_counter를 정리하기
    for name in votes:
        pass            # 코드를 작성하세요.

    # 후보별 득표수 출력
    print(vote_counter)


def exercise_6():
    # 자리수 합 리턴
    def sum_digit(num):
        # 코드를 입력하세요.
        pass

    # sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
    # 코드를 입력하세요.


def exercise_7():
    def mask_security_number(security_number):
        # 코드를 입력하세요.
        pass

    # 테스트
    print(mask_security_number("880720-1234567"))
    print(mask_security_number("8807201234567"))
    print(mask_security_number("930124-7654321"))
    print(mask_security_number("9301247654321"))
    print(mask_security_number("761214-2357111"))
    print(mask_security_number("7612142357111"))


def exercise_8():
    def is_palindrome(word):
        # 코드를 입력하세요.
        pass

    # 테스트
    print(is_palindrome("racecar"))
    print(is_palindrome("stars"))
    print(is_palindrome("토마토"))
    print(is_palindrome("kayak"))
    print(is_palindrome("hello"))


def exercise_9():
    import random

    # 코드를 작성하세요.


def exercise_10():
    pass


if __name__ == '__main__':
    print('--------------------------------------------------------[1]\n')
    exercise_1()
    print('--------------------------------------------------------[2]\n')
    exercise_2()
    print('--------------------------------------------------------[3]\n')
    exercise_3()
    print('--------------------------------------------------------[4]\n')
    exercise_4()
    print('--------------------------------------------------------[5]\n')
    exercise_5()
    print('--------------------------------------------------------[6]\n')
    exercise_6()
    print('--------------------------------------------------------[7]\n')
    exercise_7()
    print('--------------------------------------------------------[8]\n')
    exercise_8()
    print('--------------------------------------------------------[9]\n')
    exercise_9()
    print('--------------------------------------------------------[10]\n')
    exercise_10()
