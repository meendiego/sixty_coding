def quiz_1():
    print('\'응답하라 1988\'은 많은 시청자들에게 사랑을 받은 드라마예요.\n데카르트는 "나는 생각한다. 고로 존재한다."라고 말했다.\n영화 \'신세계\'에서 "드루와~"라는 대사가 유행했다.')


def quiz_2():
    wage = 5  # 시급 (1시간에 5달러)
    exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)
    
    # "1시간에 5달러 벌었습니다." 출력
    print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))
    
    # "5시간에 25달러 벌었습니다." 출력
    print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))  # 코드를 채워 넣으세요.
    
    # "1시간에 5710.8원 벌었습니다." 출력
    print(f'{1}시간에 {wage * 1 * exchange_rate}{"원"} 벌었습니다')  # 코드를 채워 넣으세요.
    
    # "5시간에 28554.0원 벌었습니다." 출력
    working_time = 5
    print(f'{working_time}시간에 {wage * working_time * exchange_rate:.1f}{"원"} 벌었습니다')  # 코드를 채워 넣으세요.


def quiz_3():
    def decode_mose(mos):
        dic = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z'
        }
        mos_list = mos.split(' ')
        result = list()
        for word in mos_list:
            try:
                result.append(dic[word])
            except KeyError:
                result.append(' ')
                continue
        
        return ''.join(result)
    print(decode_mose('... -.-. .. -.- .. - .-.. . .- .-. -.  '))


def quiz_4():
    import hashlib
    from itertools import product
    
    hide_number = '010098**567'  # '*' 처리된 전화번호
    count_hide = hide_number.count('*')
    number_hash = '0ead17f76766304fa71d0896463d7b125b08c016e9cd372596ad6967addf2b22f9d9a7672564ea75e5c62957fc7e89fab056e3ab85c6b452c518f70604ce5ea9'  # SHA512 Hash 데이터
    guess_charset = product('01234567890', repeat=count_hide)  # product('*에 들어갈 수 있는 문자 종류', repeat='*문자 길이')
    for charsets in guess_charset:
        guess_number = hide_number
        for charset in charsets:
            guess_number = guess_number.replace('*', charset, 1)
        guess_number_hash = hashlib.sha512(guess_number.encode('utf-8')).hexdigest()
        if guess_number_hash == number_hash:
            print(guess_number)
            print(guess_number_hash)
            return guess_number


def quiz_5():
    list1 = [n for n in range(1, 101) if n % 8 == 0]
    print("list1 : ", list1)


if __name__ == '__main__':
    quiz_1()
    print('--------------------------------------------------------\n')
    quiz_2()
    print('--------------------------------------------------------\n')
    quiz_3()
    print('--------------------------------------------------------\n')
    quiz_4()
    print('--------------------------------------------------------\n')
    quiz_5()
