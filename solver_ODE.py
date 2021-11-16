import numpy as np
import linalg as lin
import matrix as mat
import math


def euler_int(f, x_ini, x_end, y_ini, step):
    n = math.ceil((x_end - x_ini) / step) + 1

    x = np.linspace(x_ini, x_end, n)[:, np.newaxis]     # Vectores en columna
    y = np.zeros(x.size)[:, np.newaxis]                 # Vectores en columna

    y[0] = y_ini

    for i in range(1, x.size):
        y[i] = y[i-1] + step*f(x[i-1], y[i-1])

    return np.append(x, y, axis = 1)


def euler_int_improved(f, x_ini, x_end, y_ini, step):
    n = math.ceil((x_end - x_ini) / step) + 1

    x = np.linspace(x_ini, x_end, n)[:, np.newaxis]     # Vectores en columna
    y = np.zeros(x.size)[:, np.newaxis]                 # Vectores en columna

    y[0] = y_ini

    for i in range(1, x.size):
        y_temp = y[i-1] + step*f(x[i-1], y[i-1])
        y[i] = y[i-1] + (step/2) * (f(x[i-1], y[i-1]) + f(x[i], y_temp))

    return np.append(x, y, axis = 1)


def runge_kutta_int(f, x_ini, x_end, y_ini, step):
    n = math.ceil((x_end - x_ini) / step) + 1

    x = np.linspace(x_ini, x_end, n)[:, np.newaxis]     # Vectores en columna
    y = np.zeros(x.size)[:, np.newaxis]                 # Vectores en columna
    
    y[0] = y_ini

    for i in range(0, x.size-1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + (1/2) * step, y[i] + (1/2) * step * k1)
        k3 = f(x[i] + (1/2) * step, y[i] + (1/2) * step * k2)
        k4 = f(x[i] + step, y[i] + step * k3)

        y[i+1] = y[i] + (step/6) * (k1 + 2*k2 + 2*k3 + k4)

    return np.append(x, y, axis=1)


def multistep_int(f, f_integrator, x_ini, x_end, y_ini, step):
    n = math.ceil((x_end - x_ini) / step) + 1

    x = np.linspace(x_ini, x_end, n)[:, np.newaxis]     # Vectores en columna
    y = np.zeros(x.size)[:, np.newaxis]                 # Vectores en columna
    y_temp = np.zeros(x.size)

    y[0] = y_ini

    temp = f_integrator(f, x_ini, step*3, y_ini, step)
    y[0:4] = temp[:, 1][:, np.newaxis]

    for i in range(4):
        y_temp[i] = f(x[i], y[i])

    for i in range(4, x.size):
        y_predictor = y[i-1] + (step/24)*(55*y_temp[i-1] - 59*y_temp[i-2] + 37*y_temp[i-3] - 9*y_temp[i-4])
        y_aux = f(x[i], y_predictor)
        
        y[i] = y[i-1] + (step/24)*(9*y_aux + 19*y_temp[i-1] - 5*y_temp[i-2] + y_temp[i-3])
        y_temp[i] = f(x[i], y[i])

    return np.append(x, y, axis=1)

def finite_differences(Pfunc, Qfunc, Ffunc, a, alpha, b, beta, points):
    h = (b - a)/points

    M = mat.Matrix.from_dims(points-1, points-1)
    v = mat.Matrix.from_dims(points-1, 1)

    x = np.linspace(a, b, points+1)
    y = np.zeros(x.size)

    x[0] = a
    x[points] = b

    y[0] = alpha
    y[points] = beta

    for i in range(points-1):
        if i>0:
            M[i][i-1] = (1 - (h/2)*Pfunc(x[i+1]))

        M[i][i] = (-2 + (h**2)*Qfunc(x[i+1]))

        if i<points-2:
            M[i][i+1] = (1 + (h/2)*Pfunc(x[i+1]))

        if i!=0 and i!=points-2:
            v[i][0] = (h**2)*Ffunc(x[i+1])
        elif i==0:
            v[i][0] = (h**2)*Ffunc(x[i+1]) - (1 - (h/2)*Pfunc(x[i+1]))*alpha
        else:
            v[i][0] = (h**2)*Ffunc(x[i+1]) - (1 + (h/2)*Pfunc(x[i+1]))*beta


    solution = lin.linear_solve(M, v)

    for i in range(1, points):
        y[i] = solution[1][i-1][0]

    return np.concatenate((x[:, np.newaxis], y[:, np.newaxis]), axis = 1)

    

