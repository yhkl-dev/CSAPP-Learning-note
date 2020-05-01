def average(x, y):
    return (x + y) / 2


def improve(guess, x):
    return average(guess, x / guess)


def square(x):
    return x * x


def good_enough(guess, x):
    if abs(square(guess) - x) < 0.001:
        return True
    else:
        return False


def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)


def sqrt_a(x):
    return sqrt_iter(1.0, x)


if __name__ == '__main__':
    print(sqrt_a(9))

