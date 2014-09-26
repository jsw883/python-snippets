# basic recipe for matplotlib that saves the plot as a png

# pyplotpractical is module in local directory
import numpy as np
from matplotlib import pyplot as pp
from pyplotpractical import io
from pyplotpractical import figtool

# io.printtolog('normal',timestamp=False)

# parameters and data for plotting
N = 1000

x = np.linspace(0,10,N)
y = np.random.normal(0,1,N)

# quality and appearance settings
res = (15,10)
dpi = 72
smf = {'family':'sans-serif','style':'normal','weight':'medium','size':18}
lgf = {'family':'sans-serif','style':'normal','weight':'medium','size':18}

pp.rc('font', **smf)
pp.rc('lines',lw=2)

# plotting
fig, ax = pp.subplots(nrows=1,ncols=1,figsize=res,dpi=dpi)

figtool.axes_weight_global(ax,weight=2,ticksize=5)
fig.patch.set_alpha(0.0)
ax.patch.set_facecolor('white')

pp.plot(x,y)

ax.text(1.0/20,2.0/30,'gaussian noise',color='blue',transform=ax.transAxes)

pp.xlim(0,10)
pp.ylim(-5,5)
pp.xlabel('linspace(0,10,1000)',**smf)
pp.ylabel('N(0,1)',**smf)
pp.title('Normal model N(0,1) sampled N = ' + str(N),**lgf)

io.savefig('normal.png',dpi=dpi,format='png',timestamp=False)
pp.show()