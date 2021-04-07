import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語化 (cmd からpipでインストールして下さい　macは知らん(多分ターミナル))
#日本語化 があるところは日本語化出来てないときは英語に変更してください

c = 1
dt = 0.05
dx = 0.1
nu=c*dt/dx

jmax = 100
nmax = 100
display_interval=10  #この数の整数倍のみ表示

x = np.linspace(0,dx*(jmax-1),jmax)

q = np.zeros(jmax)

def initialize(): #初期化
    for i in range(jmax//2):
        q[i]=1




def cumpute(nmax):#計算
    cnt=0
    while(cnt<nmax):
        qcopy = q.copy()
        for i in range(1,jmax-1):
            q[i]-=nu/2*(qcopy[i+1]-qcopy[i-1])
        if (cnt%10==0):
            plt.plot(x,q)
        cnt+=1
    plt.title("めっちゃ振動")#日本語化 
    plt.xlabel("エックス")#日本語化 
    plt.grid(True)
    plt.show()
initialize()
cumpute(nmax)
