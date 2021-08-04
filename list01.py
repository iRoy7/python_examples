list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트 ")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

print("# 리스트 기본 연산자")
print("list_a + list_b = ", list_a+list_b)
print("list_a * 3 = ", list_a * 3)
print()

print("# 길이 구하기")
print("len(list_a) = ", len(list_a))


#extend()
list_a.extend(list_b)
print("list_a = ", list_a)
print("list_b = ", list_b)


#del
del list_a[1]
print("del list_a[1]: ", list_a)

#pop
list_a.pop(2)
print("pop(2) :", list_a)

#remove
list_a.remove(5)
print("remove(5) :", list_a)

#clear
list_a.clear()
print("clear() :", list_a)


array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))


#reversed(range(5))
for i in reversed(range(len(array))):
    print("현재 반복 변수: {}, 값{}".format(i, array[i]))


#list comprehensions
arr = [i*i for i in range(0,20,2)]
print(arr)


#list comprehensions with condition
arr2 = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in arr2 if fruit != "초콜릿"]
print(output)

