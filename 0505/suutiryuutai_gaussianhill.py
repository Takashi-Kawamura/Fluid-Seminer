#計算時間長め　ガウシアンひる
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

c = 1
d = 1
dt = 0.05
dx = 0.1
dy = 0.1
nu=c*dt/dx
mu=d*dt/dy

liscol=["purple","blue","skyblue","green","lightgreen","yellow","orange","pink","red"] #見やすくするためこのリストを使って色を変える

jmax = 100
kmax = 100
nmax = 100
display_interval=10 #この数の整数倍のみ表示

x = np.linspace(0,dx*(jmax-1),jmax)
y = np.linspace(0,dx*(kmax-1),kmax)
listtmp=[[0.0]*kmax]*jmax
q = np.array(listtmp)
a = 10 #ガウス分布のとがり具合の調整　大きいほど鋭くなる 推奨値:10
b = 0.8 #ガウス分布の高さ　1以下で指定


for i in range(jmax):
    for k in range(kmax):
        q[i,k]=b*np.exp(-((2*x[i]/dx/jmax-1)**2+(2*y[k]/dy/kmax-1)**2)*a)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_wireframe(X,Y,q,color="black")  #初期位置は黒



def cumpute(q):#計算
    cnt=0
    while(cnt<nmax):
        qcopy = q.copy()
        for i in range(1,jmax-1):
            for k in range(1,kmax-1):
                q[i,k]-=(nu+abs(nu))/2*(qcopy[i,k]-qcopy[i-1,k])+(nu-abs(nu))/2*(qcopy[i+1,k]-qcopy[i,k])+(mu+abs(mu))/2*(qcopy[i,k]-qcopy[i,k-1])+(mu-abs(mu))/2*(qcopy[i,k+1]-qcopy[i,k])
        if (cnt%display_interval==display_interval-1):
            ax.plot_wireframe(X,Y,q,color=liscol[cnt//display_interval%len(liscol)]) #後半は色指定
            #print(np.max(q)) #コメントアウトを外すと山の頂上の高さが分かる
        cnt+=1

    plt.title("Godunov")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

cumpute(q)

