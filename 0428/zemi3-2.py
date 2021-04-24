import matplotlib.pyplot as plt
import numpy as np

#初期化
dt = 0.05
dx = 0.1

jmax = 21
nmax = 6

#x,qの初期化
def init(q1, q2, dx, jmax):
    x = np.linspace(0, dx * (jmax - 1), jmax)
    q = np.array([(float(q1) if i < 0.5 * jmax else float(q2)) for i in range(jmax)])
    return (x, q)

#それぞれの方法で流束を返す関数を作る
#一次精度風上法
def UPWIND1(q, c, dt, dx, j):
    ur = q[j + 1]
    ul = q[j]
    fr = c * ur
    fl = c * ul
    return 0.5 * (fr + fl - abs(c) * (ur - ul))

#二次精度風上法
def UPWIND2(q, c, dt, dx, j):
    ur = 1.5 * q[j + 1] - 0.5 * q[j+2]
    ul = 1.5 * q[j] - 0.5 * q[j-1]
    fr = c * ur
    fl = c * ul
    return 0.5 * (fr + fl - abs(c) * (ur - ul))

#グラフを描く
def do_computing(q1, q2, c, dt, dx, nmax, f):
    fig = plt.figure(figsize=(9, 6), dpi=100)
    plt.rcParams["font.size"] = 10
    for k in range(2):
        #qの初期化
        x, q = init(q1, q2, dx, jmax)

        #初期分布
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        ax = fig.add_subplot(2, 2, k + 1)
        ax.plot(x, q, marker='o', markersize=1, lw=2, label='n=0')

        #各場合の計算
        ff = f[k]
        for n in range(1, nmax + 1):
            qold = q.copy()
            for j in range(k + 1, jmax - (k + 1)):
                ff1 = ff(qold, c, dt, dx, j)
                ff2 = ff(qold, c, dt, dx, j-1)
                q[j] = qold[j] - dt / dx * (ff1 - ff2)

            #各ステップのプロット
            if n % 2 == 0:
                ax.plot(x, q, marker='o', markersize=1, lw=1, label=f'n={n}')
            
        #グラフの描画
        ax.grid(color='black', linestyle='dashed', linewidth=0.5)
        plt.xlim([0, jmax * dx])
        plt.xlabel('x')
        plt.ylabel('q')
        ax.legend()
        plt.ylim([-1, 1.1])
        plt.yticks(np.arange(-1, 1.1, 0.2))

dt = 0.05
dx = 0.1

jmax = 21
nmax = 6

q1 = 1
q2 = 0
do_computing(q1, q2, 1, dt, dx, nmax, [UPWIND1, UPWIND2])

q1 = 0
q2 = 1
do_computing(q1, q2, -1, dt, dx, nmax, [UPWIND1, UPWIND2])

plt.show()