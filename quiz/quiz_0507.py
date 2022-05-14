def quiz_1():   # https://hcnoh.github.io/2018-09-27-effective-python-way16
    def index_words(text):      # 띄어쓰기로 구분된 단어들의 시작 인덱스를 return 하는 함수
        result = []
        if text:
            result.append(0)
        for index, letter in enumerate(text):
            if letter == ' ':       # 띄어쓰기가 존재하면
                result.append(index + 1)    # index에 1을 더한 값을 result 리스트에 추가해준다(모든 인덱스는 0부터 시작하기 때문)
        return result

    def index_words_iter(text):
        if text:
            yield 0
        for index, letter in enumerate(text):
            if letter == " ":
                yield index + 1
    print(index_words('chloe lovely girl'))
    print(list(index_words_iter('chloe lovely girl')))


def quiz_2():
    import json
    result = dict()
    with open('..//data/vocabulary.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        if data:
            result = json.loads(data)
    with open('..//data/vocabulary.txt', 'w', encoding='utf-8') as f:
        while True:
            english = input('영단어를 입력해주세요')
            if english == 'q':
                break
            korean = input('한글을 입력해주세요')
            if korean == 'q':
                break
            result[english] = korean
        f.write(json.dumps(result))


def quiz_3():
    import json

    with open('..//data/vocabulary.txt', 'r', encoding='utf-8') as susu:
        words = json.loads(susu.read())
    mode = int(input('영어모드 : 1, 한글모드 : 2'))
    if mode == 1:
        for eng, kor in words.items():
            answer = input(f'{eng} >?')
            if answer == kor:
                print('정답입니다.')
            else:
                print(f'아쉽습니다. 정답은 {kor} 입니다.')
    elif mode == 2:
        for eng, kor in words.items():
            answer = input(f'{kor} >?')
            if answer == eng:
                print('정답입니다.')
            else:
                print(f'아쉽습니다. 정답은 {eng} 입니다.')
    else:
        print('모드를 정확히 입력해주세요.')


def quiz_4():
    string = """always
American
among
but
buy
by
call
camera
campaign
Mrs
much
music
player
PM
point
1000
10000
100000
1000000"""
    words_list = string.split('\n')
    result = list()
    for word in words_list:
        if 'a' in word:
            result.append(word)
    print(result)


def quiz_5():
    b = [6.5, 2.2, 1.2, 4, 5.3, 9.1]        # 실수를 정수로
    # 나는 comprehension으로~~
    print([int(x) for x in b])


def quiz_6():
    import collections
    def solution(participant, completion):
        answer = list(set(participant) - set(completion))
        return answer[0]    # 미완주자를 한명으로 간주하였으므로

    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    # print(solution(participant, completion))
    counter_p = collections.Counter(participant)    # Counter({'marina': 1, 'josipa': 1, 'nikola': 1, 'vinko': 1, 'filipa': 1})
    counter_c = collections.Counter(completion)     # Counter({'josipa': 1, 'filipa': 1, 'marina': 1, 'nikola': 1})
    minus_result = counter_p - counter_c            # Counter({'vinko': 1})
    print(list(minus_result)[0])


if __name__ == '__main__':
    # quiz_1()
    # quiz_3()
    # quiz_2()
    # quiz_4()
    # quiz_5()
    quiz_6()
