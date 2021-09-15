mydict = { }
mydict['홍길동'] = '010-111-1111'
mydict['이순신'] = '010-222-2222'
print(mydict)

del mydict['이순신']
print(mydict)


#딕셔너리에 포함된 값들은 keys, values, items 함수들을 사용하여 리스트의 형태로 얻을 수 있다.'

mydict2 = {'kim':'111', 'park':'2222', 'lee':'3333'}
for k in mydict2.keys() :
    v = mydict2[k]
    print("{0:10s} {1:10s}".format(k,v))


for item in mydict2.items() :
    print(item)
    print(item[0]) # key
    print(item[1]) # value
