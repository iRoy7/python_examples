try:
    number_input_a = int(input(" 정수 입력 > "))

    print("원의 반지름:",  number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이: ", 3.14*number_input_a*number_input_a)

except:
    print("무언가 잘못되었습니다.")



#try except else

try:
    number_input_b = int(input("정수 입력 > "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:",  number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이: ", 3.14*number_input_a*number_input_a)
    print()


# try except finally

try :
    text = input("출생년도 입력: ")
    year = int(text)
    age = 2021 - year + 1
    print("당신은 %d 살입니다." % age)
except :
    print("예상치 못한 상황으로 종료합니다.")
finally :
    print("이용해주셔서 감사합니다.")
    