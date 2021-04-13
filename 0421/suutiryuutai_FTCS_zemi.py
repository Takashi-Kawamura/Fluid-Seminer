#p24 FTCS法の実装
import numpy as np    #パッケージのインポート
import matplotlib.pyplot as plt


#各種定数の設定
c = 1
dt = 0.05
dx = 0.1
nu=c*dt/dx

jmax = 100
nmax = 10
display_interval=3  #この数の整数倍のみ表示


#初期化フェーズ
x = np.linspace(0,dx*(jmax-1),jmax)



def initialize(): #初期化
    q = np.zeros(jmax)
    for i in range(jmax//2):
        q[i]=1
    return q




def cumpute(q):#計算用の関数を作成
    
    cnt=0  #回数を数えるための変数を設定
    
    while(cnt<nmax):  #条件を満たす間繰り返す
        qcopy = q.copy()  #qをコピー
        for i in range(1,jmax-1):
            q[i]-=nu/2*(qcopy[i+1]-qcopy[i-1])
        if (cnt%display_interval==0):
            plt.plot(x,q)
        cnt+=1 #回数を+1している

    #表示関係
    plt.title("FTCS")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

#実行
q=initialize()
cumpute(q)
