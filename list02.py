a = [10,20,30]
print(a[0])
print(a[1])
print(a[2])


for item in a :
    print(item)



# scores = []
# for i in range(5) :
#     value = int(input("%dth score of student: " % (i+1)))
#     scores.append(value)

# print(scores)

# sum = 0

# for i in range(5) :
#     sum += scores[i]

# print("Sum = ", sum)
# print("Avg = ", (sum/5))



#수식을 활용한 리스트 생성하기

# xlist = list(range(0,10,1))
# ylist = [5*x+10 for x in xlist]

# print(xlist)
# print(ylist)


#키와 표준 몸무게 리스트 저장하기

hlist = list(range(150,181,3))
wlist = [(h-100)*0.9 for h in hlist]

for i in range(len(hlist)) :
    print("{0:2d}  {1:5d} cm {2:6.1f} kg ".format(i+1, hlist[i], wlist[i]))


#sine  graph
import math as m
import turtle as t

xlist2 = list(range(0,721,10))
ylist2 = [ m.sin(m.radians(x)) for x in xlist2]

for i in range(len(xlist2)) :
    x = xlist2[i]
    y = ylist2[i]
    t.goto(x/1.6,y*150)
    print("%3d ----> %6.2f " % (x,y))

