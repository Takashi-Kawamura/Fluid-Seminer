#p38 方向に依存しない一次風上法


import numpy as np
import matplotlib.pyplot as plt

c = -1
dt = 0.05
dx = 0.1

nu=c*dt/dx #くーらんすー

jmax = 100
nmax = 100
display_interval=10  #この数の整数倍のみ表示

x = np.linspace(0,dx*(jmax-1),jmax)





def initialize(): #初期化
    q = np.zeros(jmax)
    for i in range(jmax//2):
        q[i]=1
    return q


"""
本来このようなプログラムは書くべきでない
ループ内処理を複雑化させることは計算量に大きな不可を与えることになるため、
可能な限り初期値等で対応するべきである。
今回の場合、以下のようにすればループをいじる必要はない
(左右反転した解が得られるが本質的に問題はない。気になるなら表示をいじると良い)


nu=abs(c)*dt/dx

def initialize(): #初期化
    q = np.zeros(jmax)
    if (c>0):
        for i in range(jmax//2):
            q[i]=1
        return q
    else:
        for i in range(jmax//2,jmax):
            q[i]=1
        return q
    
"""





def cumpute(q):#計算
    cnt=0
    while(cnt<nmax):
        qcopy = q.copy()
        for i in range(1,jmax-1):
            q[i]-=(nu+abs(nu))*(qcopy[i]-qcopy[i-1])/2+(nu-abs(nu))*(qcopy[i+1]-qcopy[i])/2
        if (cnt%display_interval==0):
            plt.plot(x,q)
        cnt+=1
    plt.title("kazakami")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
q=initialize()
cumpute(q)
