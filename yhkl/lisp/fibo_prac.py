
def fib(n):
    return fib_iter(2, 1, 0, n)


def fib_iter(a, b, c, count):
    if count == 0:
        return c
    return fib_iter(a + 2*b + 3*c, a, b, count - 1)


def f(n):
    if n >= 3:
        return f(n-1) + 2*f(n-2) + 3 * f(n-3)
    return n



if __name__ == "__main__":
    print(fib(4))
    print(fib(5))
    print("-" * 100)
    print(fib(100))

