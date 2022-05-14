def quiz_1():
    import random
    total = 50
    count_matching = 0
    for i in range(total):
        random_time = random.randint(5, 50)
        if 5 <= random_time <= 15:
            count_matching += 1
            print(f'[O] {i + 1}번째 손님 (소요시간 : {random_time}분)')
        else:
            print(f'[ ] {i + 1}번째 손님 (소요시간 : {random_time}분)')
    print(f'총 탑승 승객 : {count_matching} 분')


def quiz_2():
    import datetime
    now = datetime.time(4, 20, 0)
    test = datetime.timedelta(seconds=50)
    print(now+test)


def quiz_3():
    line_two = [
        '성수', '뚝섬', '한양대', '왕십리', '상왕십리', '신당', '동대문역사문화공원', '을지로4가', '을지로3가',
        '을지로입구', '시청', '충정로', '아현', '이대', '신촌', '홍대입구', '합정', '당산', '영등포구청', '문래',
        '신도림', '대림', '구로디지털단지', '신대방', '신림', '봉천', '서울대입구', '낙성대', '사당', '방배',
        '서초', '교대', '강남', '역삼', '선릉', '삼성', '종합운동장', '잠심새내', '잠실', '잠실나루', '강변',
        '구의', '건대입구'
    ]
    chance = 10
    count = 0
    for i in range(chance):
        print('지하철역 이름을 입력하세요~')
        answer = input()
        if answer in line_two:
            print('정답')
            count += 1
        else:
            print('땡! 해당 역은 2호선이 아닙니다!')
    print(f'총 {count} 개의 정답을 맞추셨습니다.')


if __name__ == '__main__':
    # quiz_1()
    # quiz_3()
    quiz_2()