# %%
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# -------- 기본 수치 ----------#

# 공통부분
T0 = 0.08
Ts = 0.4
TL = 5

# 다른부분(500년, 2400년)

# 500년
# Sd1 = 0.3
# Sds = 0.75

# 2400년
Sd1 = 0.6
Sds = 1.5

# -------- 기본 수치 끝 ----------#


def Sa1(T):
    ans = 0.6*(Sds/T0)*T + 0.4*Sds
    return ans


def Sa3(T):
    ans = Sd1/T
    return ans


def Sa4(T):
    ans = (Sd1*TL)/(T**2)
    return ans


young, old = False, False
start = -0.03
end = 7.0

# 500년
# young = True
# plt.xlim(-0.9, 6.5)
# plt.ylim(0, 0.85)

# 2400년
old = True
plt.xlim(-0.9, 6.5)
plt.ylim(0, 1.7)

T = np.arange(start, end, 0.001)
T1 = np.arange(start, T0, 0.001)
T2 = np.arange(T0, Ts, 0.001)
T3 = np.arange(Ts, TL, 0.001)
T4 = np.arange(TL, end, 0.001)

Sa = np.array([])
Sa = np.append(Sa, [Sa1(T1)])
Sa = np.append(Sa, [Sds]*len(T2))
Sa = np.append(Sa, [Sa3(T3)])
Sa = np.append(Sa, [Sa4(T4)])
T_circle = np.array([start, T0, Ts, 1.0, TL])
Sa_circle = np.array([Sa[1], Sds, Sds, Sa3(1.0), Sa[TL*1000]])

plt.plot(T, Sa[:len(T)], "-", T_circle, Sa_circle, "bo")

ax = plt.gca()
if young:
    plt.savefig('500년.png')
if old:
    plt.savefig('2400년.png')
plt.show()

# %%
