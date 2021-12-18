import timeit

def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        s += 1
        i += 1
    return s

def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += 1
    return s

def sum_range(n=100_000_000):
    return sum(range(n))

def math_sum(n=100_000_000):
    return (n * (n - 1)) // 2

def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for loop\t\t', timeit.timeit(for_loop, number=1))
    print('sum range\t\t', timeit.timeit(sum_range, number=1))
    print('math sum\t\t', timeit.timeit(math_sum, number=1))

if __name__ == '__main__':
    main()

# while loop               10.596477700000001
# for loop                 4.9276768