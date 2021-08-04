def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("hello", 5)


def print_n_times2(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times2(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

print()