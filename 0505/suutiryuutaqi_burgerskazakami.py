#burgers方程式 風上でやったらなにも起こらない
import numpy as np
import matplotlib.pyplot as plt

c = 1
dt = 0.05
dx = 0.1



jmax = 100
nmax = 100
display_interval=10  #この数の整数倍のみ表示

x = np.linspace(0-dx*jmax/2,dx*(jmax-1)-dx*jmax/2,jmax)

q = np.zeros(jmax)

def initialize(): #初期化
    for i in range(jmax//2):
        q[i]=1
    return q




def cumpute(q):#計算
    cnt=0
    while(cnt<nmax):
        qcopy = q.copy()
        for i in range(1,jmax-1):
            q[i]-=dt/dx/2*((qcopy[i]+abs(qcopy[i]))*(qcopy[i]-qcopy[i-1])+(qcopy[i]-abs(qcopy[i]))*(qcopy[i+1]-qcopy[i]))
        if (cnt%display_interval==0):
            plt.plot(x,q)
        cnt+=1
    plt.title("None")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
q=initialize()
cumpute(q)
