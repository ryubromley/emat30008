from solveODE import solve_ode
import numpy as np
import matplotlib.pyplot as plt
from ode_functions import ode_1
from ode_functions import f_s
from ode_functions import X_analytic
import math

f = ode_1
true_sol = math.e
t = [0, 1]


def error_plot(f, x0, t, true_sol):
    h_val = np.logspace(-4, -1, 50)
    euler_list = np.zeros(int(len(h_val)))
    rk4_list = np.zeros(int(len(h_val)))

    for i in range(len(h_val)):
        euler_sol = solve_ode(f, x0, t, 'euler', h_val[i])
        error = abs(euler_sol[-1] - true_sol)
        euler_list[i] = error

    for i in range(len(h_val)):
        rk4_sol = solve_ode(f, x0, t, 'rk4', h_val[i])
        error = abs(rk4_sol[-1] - true_sol)
        rk4_list[i] = error

    # print(rk4_list)
    # print(euler_list)
    ax = plt.gca()
    ax.scatter(h_val, euler_list)
    ax.scatter(h_val, rk4_list)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.legend(['Euler', 'RK4'], loc='best')
    plt.show()


# This needs to be moved to future euler test
def euler_run(f, t, true_sol):
    method = 'euler'
    x0 = [1]
    dt_max = 0.01
    euler = solve_ode(f, x0, t, method, dt_max)[-1]
    print('Euler approximation = ' + str(euler))


# This needs to be moved to future rk4 test
def rk4_run(f, t, true_sol):
    method = 'rk4'
    x0 = [1]
    dt_max = 0.01
    rk4 = solve_ode(f, x0, t, method, dt_max)[-1]
    print('Runge-kutta approximation = ' + str(rk4))


euler_run(f, t, true_sol)
rk4_run(f, t, true_sol)

t_lim = [0, 1]
error_plot(f, [1], t_lim, true_sol)

t = np.linspace(0, 1, 100)

x0 = [1, 0]
t = np.linspace(0, 20, 100)
eul_sol = solve_ode(f_s, x0, t, 'euler', 0.001)
rk4_sol = solve_ode(f_s, x0, t, 'rk4', 0.001)
xeul = eul_sol[:, 0]
xeuldot = eul_sol[:, 1]
xrk4 = rk4_sol[:, 0]
xrk4dot = rk4_sol[:, 1]

x_analytic, xdot_analytic = X_analytic(t, x0)

plt.plot(t, xeul, t, xrk4, t, x_analytic)
plt.xlabel('time, t')
plt.ylabel('x')
plt.show()

plt.plot(xeuldot, xeul, xrk4dot, xrk4)
plt.xlabel('xdot')
plt.ylabel('x')
plt.show()