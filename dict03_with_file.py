dic = {}
fp = open("prog_lang.txt", "r")
for line in fp.readlines() :
    x = line.split(",")
    dic[x[0]] = int(x[1])
fp.close()

while 1 :
    query = input("\n 무엇이 궁금하세요? ")
    query = query.lower()

    for key in dic.keys() :
        if key in query :
            year = dic.get(key)
            print("{} 언어는 {} 년에 태어났어요".format(key, year))
            break
    else :
        print("제가 이해할 수 없는 질문입니다.")

