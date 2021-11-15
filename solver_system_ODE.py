import numpy as np
import math

def euler_int(f, x_ini, x_end, y_ini, u_ini, step):
    n = math.ceil((x_end - x_ini) / step) + 1

    x = np.linspace(x_ini, x_end, n)[:, np.newaxis]     # Vectores en columna
    u = np.zeros(x.size)[:, np.newaxis]                 # Vectores en columna
    y = np.zeros(x.size)[:, np.newaxis]                 # Vectores en columna

    u[0] = u_ini
    y[0] = y_ini

    for i in range(1, x.size):
        y[i] = y[i-1] + step*u[i-1]
        u[i] = u[i-1] + step*f(x[i-1], y[i-1], u[i-1])

    return np.concatenate((x, y, u), axis=1)

def runge_kutta_int(f, g, t_ini, t_end, x_ini, y_ini, step):
    n = math.ceil((t_end - t_ini) / step) + 1

    t = np.linspace(t_ini, t_end, n)[:, np.newaxis]     # Vectores en columna
    x = np.zeros(t.size)[:, np.newaxis]                 # Vectores en columna
    y = np.zeros(t.size)[:, np.newaxis]                 # Vectores en columna

    x[0] = x_ini
    y[0] = y_ini

    for i in range(t.size-1):
        m1 = f(t[i], x[i], y[i])
        k1 = g(t[i], x[i], y[i])

        m2 = f(t[i] + (1/2)*step, x[i] + (1/2)*step*m1, y[i] + (1/2)*step*k1)
        k2 = g(t[i] + (1/2)*step, x[i] + (1/2)*step*m1, y[i] + (1/2)*step*k1)

        m3 = f(t[i] + (1/2)*step, x[i] + (1/2)*step*m2, y[i] + (1/2)*step*k2)
        k3 = g(t[i] + (1/2)*step, x[i] + (1/2)*step*m2, y[i] + (1/2)*step*k2)

        m4 = f(t[i] + step, x[i] + step*m3, y[i] + step*k3)
        k4 = g(t[i] + step, x[i] + step*m3, y[i] + step*k3)

        x[i+1] = x[i] + (step/6)*(m1 + 2*m2 + 2*m3 + m4)
        y[i+1] = y[i] + (step/6)*(k1 + 2*k2 + 2*k3 + k4)

    return np.concatenate((t, x, y), axis = 1)