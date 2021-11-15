import solver_ODE as sol
import solver_system_ODE as sys_sol
import math
#import matplotlib.pyplot as plt

def f(t, x, y):
    return y

def g(t, x, y):
    return -t*y - x

# print("Metodo de Euler normal")
# print(sol.euler_int(f1, 1, 1.5, 1, 0.05))

# print("Metodo de euler mejorado")
# print(sol.euler_int_improved(f1, 1, 1.5, 1, 0.05))

# print("Metodo runge kutta")
# print(sol.runge_kutta_int(f1, 1, 1.5, 1, 0.05))

# print("Metodo multipasos utilizando RK4")
# print(sol.multistep_int(f1, sol.runge_kutta_int, 0, 2.4, 2, 0.6))

print("SODE con Euler")
print(sys_sol.euler_int(f, g, 0, 0.2, 1, 2, 0.1))

# print("SODE con RK4")
# print(sys_sol.runge_kutta_int(f, g, 1, 1.2, 2, 2, 0.1))

# solution = sys_sol.runge_kutta_int(f, g, 0, 0.2, 1, 1, 0.01)
# plt.plot(solution[:, 0], solution[:, 1], 'b', solution[:, 0], solution[:, 2], 'r')
# plt.show()