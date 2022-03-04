import time


def return_abc():
    # alphabets = []
    # for ch in "ABC":
    #     # time.sleep(1)
    #     alphabets.append(ch)
    # map, lambda, filter 를 사용하기보다 comprehension을 사용하는 것이 보다 파이써닉하다.
    alphabets = [x for x in "ABC"]
    return alphabets


def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch


def yield_from_abc():
    yield from ["A", "B", "C"]


def list_comprehension():
    start_time = time.time()
    numbers = [i for i in range(100000) if i % 2 == 0]
    print(time.time() - start_time)
    return numbers


def generator_comprehension():
    start_time = time.time()
    numbers = (i for i in range(100000) if i % 2 == 0)
    print(time.time() - start_time)
    return numbers
    # yield numbers


def test_zip():
    from itertools import zip_longest
    fruit = ['바나나', '토마토', '귤']
    color = ['yellow', 'red', 'yellow', 'test']
    # 두 iterator의 길이가 다른 경우 zip의 결과가 예상과 다르다.
    if len(fruit) == len(color):
        for fruit, color in zip(fruit, color):
            print(fruit, color)
    # 두 iterator의 길이가 다를 경우 zip_longest 를 사용
    else:
        for fruit, color in zip_longest(fruit, color):
            print(fruit, color)


if __name__ == '__main__':
    # for ch in return_abc():
    #     print(ch)
    #
    # # comprehension 의 표현식이 2개이상일 경우 if, for 문을 사용하는 것이 적절.
    # # generator comprehension은 입력이 클 경우(파일, DB) 혹은 네트워크 소켓을 사용할 경우 적절히 활용.
    #
    # for ch in yield_abc():
    #     print(ch)
    #
    # print(yield_from_abc())

    # test1 = list_comprehension()
    # print(test1)
    # print('=======================================================')
    # test2 = generator_comprehension()
    # print(test2)
    # print(next(test2))
    # print(next(test2))

    test_zip()
