def exercise_1():
    index = 0
    first = 1
    second = 1
    while index < 50:
        if index < 2:
            print(first)
        else:
            result = first + second
            print(result)
            first = second
            second = result
        index += 1


def exercise_2():
    # 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
    def fahrenheit_to_celsius(fahrenheit):
        index = 0

        while index < len(fahrenheit):
            fahrenheit[index] = ((fahrenheit[index] - 32) * 5) / 9
            fahrenheit[index] = round(fahrenheit[index], 1)
            index += 1
        return fahrenheit

    temperature_list = [40, 15, 32, 64, -4, 11]

    print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

    # 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
    temperature_list = fahrenheit_to_celsius(temperature_list)

    print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력


def exercise_3():
    # 원화(￦)에서 달러($)로 변환하는 함수
    def krw_to_usd(krw):
        index = 0

        while index < len(krw):
            krw[index] = krw[index] / 1000
            index += 1

        return krw

    # 달러($)에서 엔화(￥)로 변환하는 함수
    def usd_to_jpy(usd):
        index = 0

        while index < len(usd):
            usd[index] = usd[index] * 1000 / 8
            index += 1

        return usd

    prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]

    print("한국 화폐: " + str(prices))

    print("미국 화폐:", krw_to_usd(prices))

    print("일본 화폐:", usd_to_jpy(prices))


def exercise_4():
    a = 1
    b = 2
    c = 3
    while True:
        while True:
            while True:
                if a+b+c > 400:
                    break
                if a+b+c == 400 and (a*a) + (b*b) == (c*c):
                    print(a * b * c)
                c += 1
            b += 1
            c = b+1
            if a + b + c > 400:
                break
        a += 1
        b = a+1
        c = b+1
        if a + b + c > 400:
            break


def exercise_5():
    # 투표 결과 리스트
    votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', '최만수', '김영자', '최만수', '김영자',
             '김영자', '최만수', '최만수', '최만수', '강승기', '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기',
             '김영자']

    # 후보별 득표수 사전
    vote_counter = {}

    # 리스트 votes를 이용해서 사전 vote_counter를 정리하기
    for name in votes:
        if name in vote_counter:
            vote_counter[name] += 1
        else:
            vote_counter[name] = 1

    # 후보별 득표수 출력
    print(vote_counter)


def exercise_6():
    def result_digit(num):
        str_data = str(num)
        length = len(str_data)
        sum_data = 0

        for index in range(0, length, 1):
            sum_data += int(str_data[index])

        return sum_data

    result = 0
    for i in range(1, 1001, 1):
        result += result_digit(i)

    print(result)


def exercise_7():
    def mask_security_number(security_number):
        length = len(security_number)
        flag = False

        for i in range(0, length, 1):
            if security_number[i] == '-':
                flag = True
                break

        if flag:
            string_size = security_number[0:10]
            string_size += "****"
        else:
            string_size = security_number[0:9]
            string_size += "****"
        return string_size

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
        start = 0
        length = len(word) - 1

        while True:
            if word[start] != word[length]:
                return False

            start += 1
            length -= 1

            if start == length:
                return True

    # 테스트
    print(is_palindrome("racecar"))
    print(is_palindrome("stars"))
    print(is_palindrome("토마토"))
    print(is_palindrome("kayak"))
    print(is_palindrome("hello"))


def exercise_9():
    import random

    def quiz():
        digit = random.randint(1, 20)
        count = 1
        for nChance in range(4, 0, -1):
            print("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:".format(nChance))
            answer = int(input(""))
            if answer < digit:
                print("Up")
            else:
                print('Down')

            if digit == answer:
                print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(count))
                return True
            count += 1

        print("아쉽습니다. 정답은 {}였습니다.".format(digit))
        return False

    quiz()


def exercise_10():
    line_count = 0
    total = 0

    with open('..//data/chicken.txt', 'r', encoding='utf-8') as f:
        for line in f:
            for i in range(0, len(line), 1):
                if line[i] == ":":
                    total += int(line[i + 1: len(line)])
                    break

            line_count += 1

        print(total / line_count)


if __name__ == '__main__':
    exercise_1()
    print('--------------------------------------------------------\n')
    exercise_2()
    print('--------------------------------------------------------\n')
    exercise_3()
    print('--------------------------------------------------------\n')
    exercise_4()
    print('--------------------------------------------------------\n')
    exercise_5()
    print('--------------------------------------------------------\n')
    exercise_6()
    print('--------------------------------------------------------\n')
    exercise_7()
    print('--------------------------------------------------------\n')
    exercise_8()
    print('--------------------------------------------------------\n')
    exercise_9()
    print('--------------------------------------------------------\n')
    exercise_10()
