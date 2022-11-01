import numpy as np

gamma = 1.4 # ratio of specific heat
R = 287.06 # gas constant
T_absolute = -273.15 # absolute zero
T_h = -56.5 - T_absolute # temperature in stratosphere

# standard parameters (0 altitude)
T0 = 15. - T_absolute
p0 = 1013.25e2
rho0 = 1.225
c0 = 340.294
g0 = 9.80665

# heat descing per meter
lam = 6.5 / 1000
ratio = 5.494e-4 / -3.567e-3
lam2 = lam * ratio

h1 = 11e3 # troposphere height
h2 = 20e3 # tropopause height
h3 = 27432. # stratosphere height

T11 = 216.65 # temperature at troposphere height
T20 = 216.65 # temperature at tropopause height
p11 = 226.32e2 # pressure at trotosphere height
p20 = 5475.06 # pressure at tropopause height
# rho11 = 0.36392 # rho at trotosphere height

def T(h):
    if h < 0.:
        return T0
    elif 0<= h <= h1:
        return T0 - lam * h
    elif h1 < h <= h2:
        return T_h
    elif h2 < h <= h3:
        return T20 - lam2 * (h - h2)
    else:
        return T(h3)
     


def p(h):
    if h < 0.:
        return p0
    elif 0<= h <= h1:
        return p0 * (T(h) / T0) ** (g0 / R / lam)
    elif h1 < h <= h2:
        return p11 * np.exp( -g0 * (h - h1) / R / T11 )
    elif h2 < h <= h3:
        return p20 * (T(h) / T20) ** (g0 / R / lam2)
    else:
        return p(h3)
    


def rho(h):
    return p(h) / T(h) / R


def a(h):
    return air_speed(T(h))


def air_speed(T):
    return np.sqrt(gamma * R * T)


# def air_speed(p, rho):
#     return np.sqrt(gamma * p / rho)
