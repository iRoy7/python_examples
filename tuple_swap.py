a, b = 10, 20

print("# 교환 전 값:")
print("a: ", a)
print("b: ", b)
print()

#swap
a, b = b, a

print("# 교환 후 값:")
print("a: ", a)
print("b: ", b)
print()


# return multiple values
def test():
    return (10, 20)

a, b = test()

print("a:", a)
print("b:", b)

