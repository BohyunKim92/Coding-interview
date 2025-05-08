"""This is a function for executing bisection method """
from typing import Callable

def bisection_minus_plus(f: Callable[[float],float], left: float, right: float) -> float:
    """
    Perform bisection method on the interval [left, right] where f(left) < 0 and f(right) > 0.  
    return approximate zero of f i.e. x satisfying abs(f(x)) = 1e-15.
    return left as a default if right-left < 1e-15.
    1e-15 is chosen for the tolerance since float is double-precision

    Args: 
        f: function of interest
        left: minimum value of the interval
        right: maximum value of the interval 
    
    Output: 
        x: approximation of zero of f, f(x) = 0.  
    """
    zero_tolerance = 1e-15
    if right-left < zero_tolerance:
        return left
    
    mid = (right+left)/2
    print(f"mid = {mid}")

    if abs(f(mid)) < 1e-15:
        return mid
    if f(mid) < 0:
        left = mid
    if f(mid) > 0:
        right = mid

    return bisection_minus_plus(f, left, right)

def bisection_plus_minus(f: Callable[[float],float], left: float, right: float):
    """
    Perform bisection method on the interval [left, right] where f(left) > 0 and f(right) < 0.  
    Can be similarly written as bisection_minus_plus(f, left, right)
    """
    pass


def bisection(f: Callable[[float],float], left: float, right: float) -> float:
    """
    Perform bisection method on the interval [left, right] for either
        1. f(left) < 0 and f(right) > 0 -- using bisection_minus_plus(f, left, right)
        2. f(left) > 0 and f(right) < 0 -- using bisection_plus_minus(f, left, right)
    Args: 
        f: function of interest
        left: minimum value of the interval
        right: maximum value of the interval 
    
    Output: 
        x: approximation of zero of f, f(x) = 0.  
    """
    # error raised if not (f(left) < 0 and f(right) > 0) or (f(left) > 0 and f(right) < 0)

    if f(left) < 0 and f(right) > 0:
        return bisection_minus_plus(f, left, right)
    
    if f(left) > 0 and f(right) < 0:
        return bisection_plus_minus(f, left, right)

def main():
    """
    The driver of testing bisection method
    """
    # testing case 1
    f = lambda x : x
    x = bisection(f,-2.0,1.0)
    print(f"The approximate solution of f(x) = x is {x}.")

if __name__ == '__main__':
    main()

