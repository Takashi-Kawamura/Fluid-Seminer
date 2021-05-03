#Hartenの流速修正法
import numpy as np
import matplotlib.pyplot as plt

c = 1
dt = 0.05
dx = 0.1
nu = c*dt/dx
de = 0.0001 #ぜろわりエラー防止



jmax = 100
nmax = 100
display_interval=10 #この数の整数倍のみ表示

x = np.linspace(0,dx*(jmax-1),jmax)

q = np.zeros(jmax)
f = np.zeros(jmax)  #数値流速 インデックスは半整数に取れないので1/2ずらしている
delta = np.zeros(jmax)
g = np.zeros(jmax)


def initialize1(): #初期化
    for i in range(jmax):
        q[i]=np.sin(i/jmax*np.pi)
    return q

def initialize2(): #初期化2
    for i in range(jmax//2):
        q[i]=1
    return q
    
def minmod(a,b):
    sgn = np.sign(a)
    return sgn*max(min(abs(a),sgn*b),0)



def cumpute(q):#計算
    cnt=0
    while(cnt<nmax):
        for i in range(jmax-1):
            delta[i]=q[i+1]-q[i]
        for i in range(1,jmax-1):
            g[i]=minmod((min(abs(c),(c**2+de**2)/2/de)-c**2*dt/dx)*delta[i]/2,(min(abs(c),(c**2+de**2)/2/de)-c**2*dt/dx)*delta[i-1]/2)
        for i in range(1,jmax-2):
            gamma=0
            if(delta[i]!=0):
                        gamma=(g[i+1]-g[i])/delta[i]
            f[i]=(c*q[i+1]+g[i+1]+c*q[i]+g[i]-abs(c+gamma)*(q[i+1]-q[i]))/2
        
        for i in range(2,jmax-1):
            q[i]-=dt/dx*(f[i]-f[i-1])
        q[-1]=q[-2]=q[-3]  #端の調整
        if (cnt%display_interval==0):
            plt.plot(x,q)
            
        cnt+=1
    plt.title("ryusoku")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
q=initialize1()
cumpute(q)
