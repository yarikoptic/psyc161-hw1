"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal
import time


def factorial_nonrecursive(n):
    """
    Computes the factorial of non-negative n, defined as n! = n*(n-1)*...*1.
    Follows standard definition of 0! = 1.
    Non-recursive implementation.
    """
    if n < 0:
        raise ValueError('n must be greater or equal than 0')
    else:
        out = 1
        for j in range(1, n+1):
            out *= j
        return out


def factorial_recursive(n):
    """
    Computes the factorial of non-negative n, defined as n! = n*(n-1)*...*1.
    Follows standard definition of 0! = 1.
    Recursive implementation.
    """
    if n < 0:
        raise ValueError('n must be greater or equal than 0')
    return 1 if n <= 1 else n * factorial_recursive(n-1)


def test_factorial():
    """
    Test that both implementations of factorial work.
    """
    implementations = [factorial_nonrecursive,
                       factorial_recursive]
    results = [(1, 1), (2, 2), (3, 6), (0, 1)]

    for factorial in implementations:
        for x, y in results:
            assert_equal(factorial(x), y)


def timethis(fn, *args):
    """
    Small helper to time the execution of function fn.
    Returns time of execution and output of function.
    """
    start = time.clock()
    output = fn(*args)
    finish = time.clock()
    return finish-start, output


def time_factorial(n=40, rep=100):
    """
    Function to time the implementations of factorial. Takes the
    maximum n to be computed and the number of repetitions for each
    computation. Computes the factorial for range(1, n+1), repeated
    `rep` times.
    """
    implementations = {'nrec': factorial_nonrecursive,
                       'rec': factorial_recursive}
    times = {'nrec': [], 'rec': []}

    for r in range(rep):
        for j in range(1, n+1):
            for key, factorial in implementations.iteritems():
                t, _ = timethis(factorial, j)
                times[key].append(t)

    avg_nrec = sum(times['nrec'])/float(n)
    avg_rec = sum(times['rec'])/float(n)
    ratio = avg_rec/avg_nrec

    print('Run first {0} factorials, {1} times'.format(n, rep))
    print('Average for non-recursive implementation: {0}s'.format(avg_nrec))
    print('Average for recursive implementation: {0}s'.format(avg_rec))
    print('Ratio recursive/non-recursive: {0}'.format(ratio))


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(int(nconditions))
    print("Number of possible trial orders: " + str(norders))
