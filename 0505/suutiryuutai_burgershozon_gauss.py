
a=10 #ガウス分布の広がりを決める定数

#burgers方程式
import numpy as np
import matplotlib.pyplot as plt

c = 1
dt = 0.05
dx = 0.1
dtdx=dt/dx


jmax = 100
nmax = 500
display_interval=50  #この数の整数倍のみ表示

x = np.linspace(0,dx*(jmax-1),jmax)



def initialize(): #初期化
    q = np.exp(-(x-jmax*dx/2)**2/jmax**2/dx**2*400)
    return q

def MC(q,j):
    fr=0.5*q[j+1]**2
    fl=0.5*q[j]**2
    return 0.5*(fr+fl-np.sign(q[j]+q[j+1])*(fr-fl))
    



def cumpute(q):#計算
    cnt=0
    while(cnt<nmax):
        qcopy = q.copy()
        for i in range(1,jmax-1):
            q[i]-=dtdx*(MC(qcopy,i)-MC(qcopy,i-1))
        if (cnt%display_interval==0):
            plt.plot(x,q)
        cnt+=1
    plt.title("hozonn!")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
q=initialize()
cumpute(q)
