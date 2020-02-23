import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':20})

# constants
v0=input('Enter initial velocity(in m/s) : ')
theta=input('Enter initial angle(in degree) : ')
theta=(np.pi*theta)/180 
g=9.81 # gravitational constant in m/s^2

timestep=0.0001
t=0
x=[]
y=[]

yval=1 # create a dummy value >0 to enter into the loop 
while yval>=0:
	xval=v0*t*np.cos(theta)
	yval=v0*t*np.sin(theta)-0.5*g*(t)**2
	if yval<0:
		break
	x=np.append(x, xval)
	y=np.append(y, yval)
	t=t+timestep

print('Flight time = '+str(t)+' seconds')
print('Maximum Height = '+str(np.max(y))+' m')

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(x,y, linewidth=2)
plt.xlabel('Horizontal Distance(m)')
plt.ylabel('Vertical Distance(m)')
plt.title('Flight time = '+str(t)+' seconds')
plt.grid()
plt.show()
