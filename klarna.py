from sys import argv
import traceback
import sys


def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    if n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def prepare_factorial():
    n = -1
    while n < 0:
        n = input('\tEnter n for factorial: ')
        try:
            n = int(n)
        except:
            print('\tPlease provide n as a positive number. 0 to exit from function.')
            n = -1
    if n == 0:
        return -1
    result = factorial(n)
    return n, result


def prepare_ackermann():
    m, n = -1, -1
    while m < 0 and n < 1:
        m = input('\tEnter m for ackermann: ')
        try:
            m = int(m)
        except:
            print('\tPlease provide m as a positive number. 0 to exit from function')
            m = -1
        if m == 0:
            return -1
        n = input('\tEnter n: ')
        try:
            n = int(n)
        except:
            print('\tPlease provide n as a positive number.')
            m = -1
    result = ackermann(m, n)
    return m, n, result


def prepare_fibonacci():
    n = -1
    while n < 0:
        n = input('\tEnter n for fibonacci: ')
        try:
            n = int(n)
        except:
            print('\tPlease provide n as a positive number. 0 to exit from function.')
            n = -1
    if n == 0:
        return -1
    result = fibonacci(n)
    return n, result


def start_process():
    sys.setrecursionlimit(int(sys.maxsize / 10000000000))
    print('!Important: Max recursion count is %s Please do not pass it not to receive any errors. Options:\n\tfib for fibonacci\n\tack for ackermann\n\tfac for factorial function\n\te for exit.' % int(sys.maxsize / 10000000000))
    while True:
        try:
            func = input('Type algorithm: ')
            func = func.lower()
            if func == 'fib':
                n, result = prepare_fibonacci()
                print('\tfibonacci(%s) is %s' % (n, result))
            elif func == 'ack':
                m, n, result = prepare_ackermann()
                print('\tackermann(%s, %s) is %s' % (m, n, result))
            elif func == 'fac':
                n, result = prepare_factorial()
                print('\tfactorial(%s) is %s' % (n, result))
            elif func == 'e':
                print('Bye!')
                break
            else:
                print('Error. Please stick with the instructions.')
        except:
            print(traceback.format_exc())
            print('Error. Please stick with the instructions.')


if __name__ == '__main__':
    start_process()
