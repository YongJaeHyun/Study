# %%
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
from matplotlib import rc
import matplotlib as mpl

font_location = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

font_name = fm.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)

# -------- 기본 수치 ----------#

# 공통부분
T0 = 0.08
Ts = 0.4
TL = 5

# 다른부분(500년, 2400년)

# 500년
Sd1_500 = 0.3
Sds_500 = 0.75

# 2400년
Sd1_2400 = 0.6
Sds_2400 = 1.5

# -------- 기본 수치 끝 ----------#


def Sa1(Sds, T):
    ans = 0.6*(Sds/T0)*T + 0.4*Sds
    return ans


def Sa3(Sd1, T):
    ans = Sd1/T
    return ans


def Sa4(Sd1, T):
    ans = (Sd1*TL)/(T**2)
    return ans


start = -0.03
end = 7.0

plt.xlim(-0.9, 6.5)
plt.ylim(0, 1.7)

T = np.arange(start, end, 0.001)
T1 = np.arange(start, T0, 0.001)
T2 = np.arange(T0, Ts, 0.001)
T3 = np.arange(Ts, TL, 0.001)
T4 = np.arange(TL, end, 0.001)

Sa_500 = np.array([])
Sa_500 = np.append(Sa_500, [Sa1(Sds_500, T1)])
Sa_500 = np.append(Sa_500, [Sds_500]*len(T2))
Sa_500 = np.append(Sa_500, [Sa3(Sd1_500, T3)])
Sa_500 = np.append(Sa_500, [Sa4(Sd1_500, T4)])
T_circle_500 = np.array([start, T0, Ts, 1.0, TL])
Sa_circle_500 = np.array(
    [Sa_500[1], Sds_500, Sds_500, Sa3(Sd1_500, 1.0), Sa_500[TL*1000]])

Sa_2400 = np.array([])
Sa_2400 = np.append(Sa_2400, [Sa1(Sds_2400, T1)])
Sa_2400 = np.append(Sa_2400, [Sds_2400]*len(T2))
Sa_2400 = np.append(Sa_2400, [Sa3(Sd1_2400, T3)])
Sa_2400 = np.append(Sa_2400, [Sa4(Sd1_2400, T4)])
T_circle_2400 = np.array([start, T0, Ts, 1.0, TL])
Sa_circle_2400 = np.array(
    [Sa_2400[1], Sds_2400, Sds_2400, Sa3(Sd1_2400, 1.0), Sa_2400[TL*1000]])

mpl.rcParams['axes.unicode_minus'] = False
plt.rc('font', family='NanumGothic')
plt.plot(T, Sa_500[:len(T)], "-", label='500년')
plt.plot(T_circle_500, Sa_circle_500, "bo", markersize=3)
plt.plot(T, Sa_2400[:len(T)], "r-", label='2400년')
plt.plot(T_circle_2400, Sa_circle_2400, "ro", markersize=3)
plt.legend()
plt.savefig('500년+2400년.png')
plt.show()

# %%
