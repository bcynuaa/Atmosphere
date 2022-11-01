# Atmosphere

A model for atmosphere used in aircraft performance calculation

Here is a simple atmosphere model to calculate aircraft performance. I build this model via textbook$^{[1]}$, inspired by my teacher Wu Dongsu and Gong Zheng. 

You can easily use `Python` or `Julia` to obtain the atmosphere parameters at any altitude below 27km like temperature $T$, density $\rho$, pressure $p$ and air speed $c$.

# If you use python

For `Python` just use:
```python
import Atmosphere as atm

h = 1000. # height = 1000m

atm.T(h) # temperature at 1000m
atm.p(h) # pressure at 1000m
atm.rho(h) # density at 1000m
atm.a(h) # air speed at 1000m
```

If you wanna parse a `np.ndarray` type into the function, I recommand you to modify the function as below:

```python
import numpy as np
import atmosphere as atm

def T(h):
    if type(h) == np.ndarray:
        N = len(h)
        T = np.zeros(N)
        for i in range(N):
            T[i] = atm.T(h[i])
            pass
        pass
    return T
    pass
```

# If you use Julia

For `Julia` just use:

```julia
include("Atmosphere.jl");
import Atmosphere as atm;

h = 1000.; # height = 1000m

atm.T(h); # temperature at 1000m
atm.p(h); # pressure at 1000m
atm.rho(h); # density at 1000m
atm.a(h); # air speed at 1000m
```

As broadcast is available in `Julia`, you can call the function to work on any kind of data:

```julia
h = 0.: 100.: 15000.; # from 0 to 15km, interval 100m

T = atm.T.(h); # T is an array of temperature from 0 to 15km, interval 100m
```

[1]：丁松滨编著. 飞行性能与飞行计划[M]. 北京：科学出版社, 2013著者-出版年制：丁松滨编著. 2013. 飞行性能与飞行计划[M]. 北京：科学出版社