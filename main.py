import numpy as np
import math

def method_of_rectangles(func, mim_lim, max_lim, delta):
    def integrate(func, mim_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - mim_lim) / n
        for x in np.arange(mim_lim, max_lim-step, step):
            integral += step * func(x + step / 2)
        return integral

    d, n = 1, 1
    while math.fabs(d) > delta:
        d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 3
        n *= 2

    a = math.fabs(integrate(func, mim_lim, max_lim, n))
    b = math.fabs(integrate(func, mim_lim, max_lim, n)) + d
    if a > b:
        a, b = b, a
    print('Метод прямоугольников:')
    print('\t%s\t%s\t%s' % (n, a, b))

def trapezium_method(func, mim_lim, max_lim, delta):
    def integrate(func, mim_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - mim_lim) / n
        for x in np.arange(mim_lim, max_lim-step, step):
            integral += step*(func(x) + func(x + step)) / 2
        return integral

    d, n = 1, 1
    while math.fabs(d) > delta:
        d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 3
        n *= 2

    a = math.fabs(integrate(func, mim_lim, max_lim, n))
    b = math.fabs(integrate(func, mim_lim, max_lim, n)) + d
    if a > b:
        a, b = b, a
    print('Метод трапеции:')
    print('\t%s\t%s\t%s' % (n, a, b))

def simpson_method(func, mim_lim, max_lim, delta):
    def integrate(func, mim_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - mim_lim) / n
        for x in np.arange(mim_lim + step / 2, max_lim - step / 2, step):
            integral += step / 6 * (func(x - step / 2) + 4 * func(x) + func(x + step / 2))
        return integral

    d, n = 1, 1
    while math.fabs(d) > delta:
        d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 15
        n *= 2

    a = math.fabs(integrate(func, mim_lim, max_lim, n))
    b = math.fabs(integrate(func, mim_lim, max_lim, n)) + d
    if a > b:
        a, b = b, a
    print('Метод симпсона:')
    print('\t%s\t%s\t%s' % (n, a, b))

method_of_rectangles(lambda x: math.sqrt(1-0.5*math.sin(x)**2), 0, math.pi/2, 0.0001)
trapezium_method(lambda x: math.sqrt(1-0.5*math.sin(x)**2), 0, math.pi/2, 0.0001)
simpson_method(lambda x: math.sqrt(1-0.5*math.sin(x)**2), 0, math.pi/2, 0.0001)