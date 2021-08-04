dictionary = {
    1: 1,
    2: 2
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]

    output = fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output

print("fibo(10): ", fibonacci(10))
print("fibo(20): ", fibonacci(20))
print("fibo(30): ", fibonacci(30))
print("fibo(40): ", fibonacci(40))
print("fibo(50): ", fibonacci(50))

