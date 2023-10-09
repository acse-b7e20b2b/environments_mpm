from envtest import my_shape
from sympy.matrices import Matrix, MatrixSymbol
import pandas as pd

A = Matrix([[2, 1, 3], [4, 7, 1], [2, 6, 8]])
x = my_shape(A)

print(x)
