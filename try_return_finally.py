from os import write


def write_text_file(filename, text):

    try:
        file = open(filename, "w")

        # 여러 가지 처리를 수행합니다.
        return

        #파일에 텍스트를 입력합니다.

    except Exception as e:
        print(e)
    finally:
        file.close()

write_text_file("test.txt", "Hello Python!")