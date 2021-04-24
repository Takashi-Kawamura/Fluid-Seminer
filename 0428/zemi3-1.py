import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline  これはjupyter notebookで使う時以外はなくていい，なんならここで使うとエラーがでた．

#初期化
dt = 0.05
dx = 0.1

jmax = 21
nmax = 6

def init(q1, q2, dx, jmax):
    x = np.linspace(0, dx * (jmax - 1), jmax)
    q = np.array([(float(q1) if i < 0.5 * jmax else float(q2)) for i in range(jmax)])
    return (x, q)

#それぞれの方法で流束を返す関数を作る
#FTCS法
def FTCS(q, c, dt, dx, j):
    return 0.5 * c * (q[j + 1] + q[j])

#一次精度風上法
def UPWIND1(q, c, dt, dx, j):
    return c * q[j]

#LAX法
def LAX(q, c, dt, dx, j):
    nu2 = 1 / (c * dt / dx)
    return 0.5 * c * ((1 - nu2) * q[j+1] + (1 + nu2) * q[j])

#LW法
def LW(q, c, dt, dx, j):
    nu = c * dt / dx
    return 0.5 * c * ((1 - nu) * q[j + 1] + (1 + nu) * q[j])

#グラフを描く
def do_computing(q1, q2, c, dt, dx, nmax, f):
    fig = plt.figure(figsize=(9, 6), dpi=100)
    plt.rcParams["font.size"] = 10
    for k in range(4):
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
            for j in range(1, jmax - 1):
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

#グラフの出力
c = 1
q1, q2 = 1, 0
do_computing(q1, q2, c, dt, dx, nmax, [UPWIND1, FTCS, LAX, LW])
plt.show()