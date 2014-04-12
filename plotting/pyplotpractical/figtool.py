import numpy as np
from matplotlib import pyplot as pp

def axes_weight_global(ax,weight=2,ticksize=5):
    """
    Resizes and changes linewidth of all ticks in the axes provided.
    
    Parameters:
      ax          axes
      ticksize    tick length in points (default = 5)
      weight      line weight in points (default = 2)
    """
    
    for axis in ['top','bottom','left','right']:
      ax.spines[axis].set_linewidth(weight)
    
    for line in ax.xaxis.get_ticklines():
        line.set_markersize(ticksize)
        line.set_markeredgewidth(weight)
    for line in ax.yaxis.get_ticklines():
        line.set_markersize(ticksize)
        line.set_markeredgewidth(weight)