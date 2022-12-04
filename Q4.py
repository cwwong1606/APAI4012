import numpy as np
from copy import deepcopy

dx = 0.02
dt = 0.001
r = dt/((dx)**2)
x = np.arange(0, 1 + dx, dx)
u_0 = (np.sin(np.pi*x))**2

A = np.zeros((len(x), len(x)))
A[np.arange(len(x)), np.arange(len(x))] = (1 - 2*r)
A[np.arange(len(x)) - 1, np.arange(len(x))] = r
A[np.arange(len(x)), np.arange(len(x)) - 1] = r
A[0, -1] = 0
A[-1, 0] = 0
A[0, 1] = 2*r
A[-1, -2] = 2*r

u = deepcopy(u_0)
for i in range(5):
    u = A@u + dt*u**2
print('When T_f = 5, u(x, T_f) = ')
print(u)

u = deepcopy(u_0)
for i in range(5):
    u = A@u + dt*u**2
print('When T_f = 5, u(x, T_f) = ')
print(u)

u = deepcopy(u_0)
for i in range(10):
    u = A@u + dt*u**2
print('When T_f = 10, u(x, T_f) = ')
print(u)

u = deepcopy(u_0)
for i in range(20):
    u = A@u + dt*u**2
print('When T_f = 20, u(x, T_f) = ')
print(u)

u = deepcopy(u_0)
for i in range(40):
    u = A@u + dt*u**2
print('When T_f = 40, u(x, T_f) = ')
print(u)

u = deepcopy(u_0)
for i in range(40):
    dx = 0.02
    dt = 0.5*(2*(dx**2))/(4 - (1 - u.min())*(dx**2))
    r = dt/((dx)**2)
    
    A = np.zeros((len(x), len(x)))
    A[np.arange(len(x)), np.arange(len(x))] = (1 - 2*r)
    A[np.arange(len(x)) - 1, np.arange(len(x))] = r
    A[np.arange(len(x)), np.arange(len(x)) - 1] = r
    A[0, -1] = 0
    A[-1, 0] = 0
    A[0, 1] = 2*r
    A[-1, -2] = 2*r
    u = A@u + dt*u**2

print('-----------------------------------------------------------')
print('After computing dt dynamic according to the stable condition')
print('When T_f = 40, u(x, T_f) =')
print(u)

u = deepcopy(u_0)
for i in range(100):
    dx = 0.02
    dt = 0.5*(2*(dx**2))/(4 - (1 - u.min())*(dx**2))
    r = dt/((dx)**2)
    
    A = np.zeros((len(x), len(x)))
    A[np.arange(len(x)), np.arange(len(x))] = (1 - 2*r)
    A[np.arange(len(x)) - 1, np.arange(len(x))] = r
    A[np.arange(len(x)), np.arange(len(x)) - 1] = r
    A[0, -1] = 0
    A[-1, 0] = 0
    A[0, 1] = 2*r
    A[-1, -2] = 2*r
    u = A@u + dt*u**2
    
print('After computing dt dynamic according to the stable condition')
print('When T_f = 100, u(x, T_f) =')
print(u)