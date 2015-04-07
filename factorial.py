"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal

def factorial_recursive(n):
    # TODO Define your logic for factorial here
    if n <= 1:
        return n
    else:
        return n * factorial_recursive(n-1)


def test_factorial():
    assert_equal(factorial_recursive(1), 1)
    # TODO: add more

if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print("Number of possible trial orders: " + str(norders))
