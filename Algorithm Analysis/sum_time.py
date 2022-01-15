import time

# With iteration
def sum_of_n(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    end = time.time()

    return the_sum, end - start


# Without iteration
def sum_of_n2(n):
    start = time.time()
    the_sum = n * (n + 1) / 2
    end = time.time()
    return the_sum, end - start


# See how time change as n grows
print("\nIteration: ")
for i in [10000, 100000, 1000000, 10000000, 100000000]:
    print("Sum is %d required %10.7f seconds" % sum_of_n(i))

print("\nNo iteration: ")
for i in [10000, 100000, 1000000, 10000000, 100000000]:
    print("Sum is %d required %10.7f seconds" % sum_of_n2(i))
