# テキスト3.2に載っているスキームのうち，一つだけ例示することにする。
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
%matplotlib inline

# 例によって，階段関数の形の初期分布を与える。
def init(q1, q2, dx, jmax):
    xs = -1 # 始点
    x = np.linspace(xs, xs + dx * (jmax-1), jmax)
    q = np.array([(float(q1) if i < 0.0 else float(q2)) for i in x])
    return (q, x)


# MacCormack法の実装。
# 呼び出し時にintervalという引数を与えなければintervalは2であると解釈し，与えればその値だと解釈する。
def do_computing_mc(x, q, c, dt, dx, nmax, interval = 2):
    plt.figure(figsize=(7,7), dpi=100) # グラフのサイズ
    plt.rcParams["font.size"] = 22 # グラフの文字サイズ

    # 初期分布をプロットする。
    plt.plot(x, q, marker='o', lw=2, label='n=0')

    # 反復計算
    for n in range(1, nmax+1 ):
        
        qbar = q.copy()
        
        for j in range(0, jmax-1):
            qbar[j] = q[j] - dt * c * (q[j+1] - q[j]) / dx
        
        for j in range(1, jmax-1): 
            q[j] = 0.5 * ((q[j] + qbar[j]) - dt * c * (qbar[j] - qbar[j-1]) / dx)
        
        if n % interval == 0:
            plt.plot(x, q, marker='o', lw=2, label=f'n={n}')            
            
    # グラフの出力
    plt.grid(color='black', linestyle='dashed', linewidth=0.5)
    plt.xlim([-1, 1])
    plt.xlabel('x')
    plt.ylabel('q')
    plt.legend()
    plt.show()

    
    
    
c  = 1
dx = 0.1
dt = 0.05

jmax = 21
nmax = 6

q1 = 1
q2 = 0
q,x = init(q1, q2, dx, jmax)
do_computing_mc(x, q, c, dt, dx, nmax, interval = 2)
