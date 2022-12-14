from typing import Callable
import numpy as np
import cvxpy as cp
import time
import matplotlib.pyplot as plt
from cvxopt import matrix


def linear_equations(size):
    A = np.random.randint(1, 10000, size=(size, size))
    B = np.random.randint(1, 100, size=(size, 1))
    return A, B


def my_timer(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        orig_func(*args, **kwargs)
        t2 = time.time() - t1
        return t2

    return wrapper


@my_timer
def numpy_solution(A, B):
    """
    returns the solution to the equation system using by numpy.
    """
    return np.linalg.solve(A, B)


@my_timer
def cvxpy_solution(A, B, size):
    """
    returns the solution to the equation system using by cvxpy.
    """
    x = cp.Variable(shape=(size, 1))
    constraints = [cp.matmul(matrix(A), x) == B]
    objective = cp.Minimize(0)
    problem = cp.Problem(objective, constraints)
    problem.solve()
    return x.value


def my_plot():
    size = [s for s in range(10, 1000, 10)]
    numpy_list = []
    cvxpy_list = []

    for s in size:
        A, B = linear_equations(s)
        numpy_list.append(numpy_solution(A, B))
        cvxpy_list.append(cvxpy_solution(A, B, s))

    plt.xlabel("size")
    plt.ylabel("time")
    plt.title("cvxpy (orange) vs. numpy (purple)")
    plt.plot(size, cvxpy_list, 'orange')
    plt.plot(size, numpy_list, 'purple')
    plt.show()


if __name__ == '__main__':
    my_plot()
