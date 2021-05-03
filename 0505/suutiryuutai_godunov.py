#burgers方程式 Godunov
import numpy as np
import matplotlib.pyplot as plt

c = 1
dt = 0.05
dx = 0.1



jmax = 100
nmax = 500
display_interval=50  #この数の整数倍のみ表示

x = np.linspace(0,dx*(jmax-1),jmax)

q = np.zeros(jmax)
f = np.zeros(jmax)
#初期化関数を階段とガウスの二種類にしました
"""
def initialize(): #初期化　階段
    for i in range(jmax//2):
        q[i]=1
"""
def initialize(): #初期化  ガウス
    q = np.exp(-(x-jmax*dx/2)**2/jmax**2/dx**2*400)
    return q
  





def cumpute(nmax):#計算
    cnt=0
    while(cnt<nmax):
        for i in range(jmax-1):
            f[i]=max((q[i+1]-abs(q[i+1]))**2,(q[i]+abs(q[i]))**2)/4
        for i in range(1,jmax-1):
            q[i]=q[i]-dt/dx*(f[i]-f[i-1])
            #q[i]=max(min(q[i]-dt/dx*(f[i]-f[i-1]),10),-10)  #minmaxは発散防止　いらないかも
        if (cnt%display_interval==0):
            plt.plot(x,q)
        cnt+=1
    plt.title("Godunov")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
q=initialize()
cumpute(nmax)
