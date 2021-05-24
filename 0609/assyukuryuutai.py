#速度の絶対値の分布を3Dで表示

#モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#反復回数　推奨:100 
nmax = 100

M      = 0.1
alpha  = 1-M**2
U0     = 0.1


dx     = 0.05
dy     = 0.05

xmin,xmax = -1.0,2.0
ymin,ymax = 0.0,1.0

jmax  = int((xmax-xmin)/dx)+1
kmax  = int((ymax-ymin)/dy)+1

x = np.linspace(xmin,xmax,jmax)
y = np.linspace(ymin,ymax,kmax)

phi   =  np.zeros([jmax,kmax])
u     =  np.zeros([jmax,kmax])
v     =  np.zeros([jmax,kmax])


dxdy   =  0.2*(1.0-2.0*x)*(np.sign(x*(1-x))+1)
re     =  np.zeros(nmax)


for n in range(nmax):
    phicopy=phi.copy()

    phi[0,:]=0.0
    phi[jmax-1,:]=0.0
    phi[:,kmax-1]=0.0

    for i in range(jmax):
        phi[i,0]=phi[i,1]-dxdy[i]*dy
        #phi[i,0]=(4*phi[i,1]-phi[i,2])/3.0-dxdy[i]*dy/3.0  #二次精度？


    #ガウスサイデル法
    for i in range(1,jmax-1):
        for k in range(1,kmax-1):
            phi[i,k]=(alpha*(phi[i-1,k]+phi[i+1,k])+dx**2/dy**2*(phi[i,k-1]+phi[i,k+1]))/2.0/(alpha+dx**2/dy**2)



    #収束判定用
    re[n]=np.sqrt(((phi-phicopy)**2).sum()/jmax/kmax)

   



                      
#u,vの計算

for i in range(1,jmax-1):
    u[i,:]=U0*(1.0+(phi[i+1,:]-phi[i-1,:])/(2*dx))
u[0,:]=U0*(1.0+(phi[1,:]-phi[0,:])/dx)
u[-1,:]=U0*(1.0+(phi[-1,:]-phi[-2,:])/dx)

for k in range(1,kmax-1):
    v[:,k]=U0*(phi[:,k+1]-phi[:,k-1])/(2*dy)
v[:,0]=U0*(phi[:,1]-phi[:,0])/dy
v[:,-1]=U0*(phi[:,-1]-phi[:,-2])/dy

va=np.sqrt(u**2+v**2)


#表示系
X,Y=np.meshgrid(x,y)

fig = plt.figure()
ax =  Axes3D(fig)


ax.set_title("q", size = 20)


ax.set_xlabel("x", size = 14)
ax.set_ylabel("y", size = 14)
ax.set_zlabel("z", size = 14)



surf=ax.plot_surface(X, Y, va.transpose(1,0),rstride=1, cstride=1, cmap="viridis")
fig.colorbar(surf, ax=ax)

fig.show()
