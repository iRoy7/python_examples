def print_n_times(*values, n = 2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍",  n = 3)


def sum_all(start=0, end=100, step=1):
    output = 0

    for i in range(start, end+1, step):
        output += i

    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))

