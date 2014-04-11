# Author: James Williams
#   Simple recipe for matplotlib single figure which is saved to disk as png.

import numpy as np
from matplotlib import pyplot as pp
from matplotlib import rc
from pyplotpractical import io

# data for plotting
x = np.linspace(0,10,1000)
y = np.random.normal(0,1,1000)

# quality and appearance settings
res = (15,10)
dpi = 72
smfont = {'family':'sans-serif','style':'normal','weight':'normal','size':18}
lgfont = {'family':'sans-serif','style':'normal','weight':'normal','size':25}

# plotting
fig, ax = pp.subplots(nrows=1,ncols=1,figsize=res,dpi=dpi)

fig.patch.set_alpha(0.0)
ax.patch.set_facecolor('white')

pp.plot(x,y)

pp.rc('font', **smfont)
pp.xlim(0,10)
pp.ylim(-5,5)
pp.xlabel('linspace(0,10,1000)')
pp.ylabel('N(0,1)')
pp.title('Normal',**lgfont)

io.savefig('normal.png',dpi=dpi,format='png')
pp.show()