def test():
    print("A spot")
    yield 1
    print("B spot")
    yield 2
    print("C spot")

output = test()

print("D spot")
a = next(output)
print(a)

print("E spot")
b = next(output)
print(b)

print("F spot")
c = next(output)
print(c)
print()

