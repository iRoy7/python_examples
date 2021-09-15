# 리스트와 튜플의 차이점은 "자료가 변경될 수 있는가? "
# 튜플은 한번 생성되면 그 항목들이 추가되거나 삭제될 수 없다.
# 튜플은 리스트보다 빠른 사용속도를 지원


mylist = [10,20,30,40,50]
mytuple = (10,20,30,40,50)
print(mylist)
print(mytuple)

len(mytuple)

30 in mytuple


mytuple[0]

for x in mytuple :
    print(x)



mylist2 = list(mytuple)
mylist2.append(60)
mylist2.remove(20)
newtuple = tuple(mylist2)
print(newtuple)

