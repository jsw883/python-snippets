#!/usr/bin/python

# import packages

import numpy as np
import sys
from matplotlib import pyplot as pp

sys.path.append("/home/jsw65/Documents/utils/python-snippets/plotting")

from pyplotpractical import io
from pyplotpractical import figtool

# parameters and initialisations

if len(sys.argv) == 1: 
    print "plot_sys_tracking.py: missing argv - exited with code 1" 
    sys.exit(1)

pathname = sys.argv[1]
fcpu = pathname + "/cpu_tracking.LOG"
fmem = pathname + "/mem_tracking.LOG"

# load cpu and memory tracking

cpu_array = np.loadtxt(fcpu)
mem_array = np.loadtxt(fmem)

# plotting parameters

res = (15,10) # INCHES
dpi = 72
smf = {'family':'sans-serif','style':'normal','weight':'medium','size':18}
lgf = {'family':'sans-serif','style':'normal','weight':'medium','size':18}

pp.rc('font', **smf)
pp.rc('lines',lw=2)

# plotting

fig,ax_array = pp.subplots(nrows=2,ncols=1,figsize=res,dpi=dpi,sharex=True)

figtool.axes_weight_global(ax_array,weight=1,ticksize=5)
fig.patch.set_alpha(1.0) # set to 0.0 for transparency
for ax in ax_array:
    ax.patch.set_facecolor('white')

epoc_time = cpu_array[:,0] - cpu_array[0,0]
mem_usage = 100*mem_array[:,2]

for cpu_usage in 100*cpu_array[:,1:].T:
    ax_array[0].plot(epoc_time,cpu_usage)

ax_array[1].plot(epoc_time,mem_usage)

# ax.text(1.0/20,2.0/30,'gaussian noise',color='blue',transform=ax.transAxes)

pp.ylim(0,100)
pp.xlabel('epoc_time',**smf)
pp.ylabel('percentage (%)',**smf)
pp.title('cpu and memory tracking',**lgf)

io.savefig('sys_tracking.png',dpi=dpi,format='png',timestamp=False)
pp.show()