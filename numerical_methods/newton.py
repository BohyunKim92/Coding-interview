""" This is a module for executing newton's method """

from typing import Callable
import math

MATH_PI = math.pi

def newton_method(f: Callable[[float],float], fprime: Callable[[float],float], x0: float) -> float:
    """ Given a function f(x), and an initial guess x0, find x such that f(x) = 0

        Argument: 
            f: function of interest
            fprime: derivative of f
            x0: initial guess
        
            make sure that f'(x) !=0.
        Output: x that satisfies f(x) = 0.
    """
    max_iteration = 12 # for newton's method
    tol = 1e-12 
    x_previous = x0
    for iter in range(max_iteration):
        x_current = x_previous - f(x_previous)/fprime(x_previous)

        if abs(f(x_current)) < tol or abs(x_current-x_previous) < tol:
            return x_current
        x_current = x_previous

    return x_current

def main():
    """ driver function """
    # test example 1
    f = lambda x : math.cos(x)
    # our function is f(x) = cos(x) so x = pi/2 will be a solution.
    fprime = lambda x : -math.sin(x)
    # derivative of f.
    x0 = MATH_PI/4
    x = newton_method(f, fprime, x0)
    print(f"The answer is x = {x}")

if __name__ == '__main__':
    main()
