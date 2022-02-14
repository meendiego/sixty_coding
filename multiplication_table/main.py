import time


def daemon():
	import sys
	try:
		while True:
			print("""[사용방법]\n1 : 구구단 출력 모드\n2 : 구구단 외기 모드\n3 : 구구단 퀴즈 모드\n4 : 프로그램 종료""")
			mode = int(input('모드를 선택해주세요.'))
			if mode == 1:
				input_int = int(input('알고싶은 구구단의 숫자를 입력해주세요.'))
				_multiplication_table(input_int)
			elif mode == 2:
				input_int = int(input('알고싶은 구구단의 숫자를 입력해주세요.'))
				_multiplication_table(input_int, 2)
			elif mode == 3:
				_quiz()
			else:
				if mode != 4:
					print('모드를 잘못 입력하셨습니다.')
				else:
					raise KeyboardInterrupt
	except KeyboardInterrupt:
		print("구구단 프로그램을 종료합니다.")
	except ValueError:
		print('올바른 숫자를 입력해주세요.')
	except Exception as e:
		print(e)
	finally:
		sys.exit()


def _multiplication_table(input_int, sleep=0):
	print(f'-----{input_int}단-----')
	
	for i in range(1, 10):
		print(input_int, 'X', i, '=', input_int * i)
		time.sleep(sleep)


def _quiz():
	import random
	start = int(time.time())
	correct = 0
	for i in range(10):
		x = random.randint(2, 9)
		y = random.randint(2, 9)
		answer = int(input(f'[문제 {i + 1}] {x} X {y} = ?'))

		if x * y == answer:
			print('정답입니다!')
			correct = correct + 1
		else:
			print('틀렸습니다..')
			print(f'[정답] {x * y}')
	print(f'[소요 시간] {int(time.time() - start)} 초')
	print(f'[정답률] {correct}/10')
	

if __name__ == '__main__':
	daemon()
