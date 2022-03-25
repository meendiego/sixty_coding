def exercise_1():
    print('\'응답하라 1988\'은 많은 시청자들에게 사랑을 받은 드라마예요.\n데카르트는 "나는 생각한다. 고로 존재한다."라고 말했다.\n영화 \'신세계\'에서 "드루와~"라는 대사가 유행했다.')


def exercise_2():
    wage = 5  # 시급 (1시간에 5달러)
    exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)

    # "1시간에 5달러 벌었습니다." 출력
    print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

    # "5시간에 25달러 벌었습니다." 출력
    print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))  # 코드를 채워 넣으세요.

    # "1시간에 5710.8원 벌었습니다." 출력
    print(f'{1}시간에 {wage*1*exchange_rate}{"원"} 벌었습니다')  # 코드를 채워 넣으세요.

    # "5시간에 28554.0원 벌었습니다." 출력
    working_time = 5
    print(f'{working_time}시간에 {wage*working_time*exchange_rate:.1f}{"원"} 벌었습니다')  # 코드를 채워 넣으세요.


def exercise_3():
    def is_evenly_divisible(number):
        # 코드를 작성하세요.
        return number % 2 == 0

    # 테스트
    print(is_evenly_divisible(3))
    print(is_evenly_divisible(7))
    print(is_evenly_divisible(8))
    print(is_evenly_divisible(218))
    print(is_evenly_divisible(317))


def exercise_4():
    def calculate_change(payment, cost):
        # 코드를 작성하세요.
        result = list()
        ohman = 50000
        ilman = 10000
        ohcheon = 5000
        ilcheon = 1000
        change = payment - cost
        print(f'거스름돈 : {change}')
        while change >= ilcheon:
            if change >= ohman:
                count = int(change / ohman)
                change = change - (ohman * count)
                result.append(f'{ohman}원 {count}장')
            elif change >= ilman:
                count = int(change / ilman)
                change = change - (ilman * count)
                result.append(f'{ilman}원 {count}장')
            elif change >= ohcheon:
                count = int(change / ohcheon)
                change = change - (ohcheon * count)
                result.append(f'{ohcheon}원 {count}장')
            else:
                count = int(change / ilcheon)
                change = change - (ilcheon * count)
                result.append(f'{ilcheon}원 {count}장')
        for text in result:
            print(text)

    # 테스트
    calculate_change(100000, 33000)
    print()
    calculate_change(500000, 378000)


def exercise_5():
    i = 100
    while i >= 1:
        if i % 8 == 0 and i % 12 != 0:
            print(i)
        i -= 1


def exercise_6():
    a = 1
    b = 1
    while a < 10:
        while b < 10:
            print(f'{a} * {b} = {a*b}')
            b += 1
        a += 1
        b = 1


def exercise_7():
    def get_grade(total):
        if total >= 90:
            print('A')
        elif 80 <= total < 90:
            print('B')
        elif 70 <= total < 80:
            print('C')
        elif 60 <= total < 70:
            print('D')
        else:
            print('F')

    def print_grade(midterm_score, final_score):
        total = midterm_score + final_score
        get_grade(total)

    # 테스트
    print_grade(40, 45)
    print_grade(20, 35)
    print_grade(30, 32)
    print_grade(50, 45)


def exercise_8():
    i = 1
    total = 0
    while i < 1000:
        if i % 2 == 0 or i % 3 == 0:
            total += i
        i += 1
    print(total)


def exercise_9():
    i = 1
    count = 0
    while i <= 120:
        if 120 % i == 0:
            print(i)
            count += 1
        i += 1
    print(f'120의 약수는 총 {count}개 입니다.')


def exercise_10():
    year = 1989
    money = 50000000
    miran = 1100000000
    while year <= 2016:
        plus = money * 0.12
        money += plus
        year += 1
    money = int(money)
    if money > miran:
        print(f'{money-miran} 원 차이로 동일 아저씨 말씀이 맞습니다.')
    else:
        print(f'{miran-money} 원 차이로 미란 아주머니 말씀이 맞습니다.')


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
