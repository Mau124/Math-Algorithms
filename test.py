import solver_ODE as sol
import solver_system_ODE as sys_sol
import math
import numpy as np
import LP
#import matplotlib.pyplot as plt

def P(x):
    return -8

def Q(x):
    return 16

def F(x):
    return 1

def f1(x, y):
    return 2*x - 3*y + 1

# print("Metodo de Euler normal")
# print(sol.euler_int(f1, 0, 0.5, 2, 0.05))

# print("Metodo de euler mejorado")
# print(sol.euler_int_improved(f1, 0, 0.5, 2, 0.05))

# print("Metodo runge kutta")
# print(sol.runge_kutta_int(f1, 0, 0.5, 2, 0.1))

# print("Metodo multipasos utilizando RK4")
# print(sol.multistep_int(f1, sol.runge_kutta_int, 0, 0.8, 1, 0.2))

# print("SODE con Euler")
# print(sys_sol.euler_int(f, g, 0, 0.2, 1, 2, 0.1))

# print("SODE con RK4")
# print(sys_sol.runge_kutta_int(f, g, 1, 1.2, 2, 2, 0.1))

# solution = sys_sol.runge_kutta_int(f, g, 0, 0.2, 1, 1, 0.01)
# plt.plot(solution[:, 0], solution[:, 1], 'b', solution[:, 0], solution[:, 2], 'r')
# plt.show()

# print("Finite differences method")
# print(sol.finite_differences(Pfunc = P, Qfunc = Q, Ffunc = F, a = 0, alpha = 1, b = 1, beta = 0, points = 5))

# Test for LP

Z= "3x1+5x2"
Constraints=["4x1+x2>=4", 
             "-x1+2x2>=2", 
             "x2<=3"]
a = LP.buildMatrix(Z, Constraints)
"""a = np.array([[1, -3, -5, 0, 0, 0, LP.INF, LP.INF, 0],
              [0, 4, 1, -1, 0, 0, 1, 0, 4],
              [0, -1, 2, 0, -1, 0, 0, 1, 2],
              [0, 0, 1, 0, 0, 1, 0, 0, 3]], dtype=np.float32)"""

LP.gauss_jordan_LP(a, maximize = True)