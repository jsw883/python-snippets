#!/usr/bin/python

# import modules

import psutil as ps
import time
import sys
from contextlib import closing

# verbose / logging functions

global verbose
verbose = True

def verbcat(string,*args,**kwargs):
    if verbose: print (string + "\n").format(*args,**kwargs),

def LOG_append(filename,string,*args,**kwargs):
    with open(filename,"a") as fid: fid.write((string + "\n").format(*args,**kwargs))

# parameters and initialisations (should make these command line args)

if len(sys.argv) == 1: 
    print "sys_tracking_append.py: missing argv - exited with code 1" 
    sys.exit(1)

pathname = sys.argv[1]
fcpu = pathname + "/cpu_tracking.LOG"
fmem = pathname + "/mem_tracking.LOG"

open(fcpu, 'w').close()
open(fmem, 'w').close()

interval = 0.1

memtotal = float(ps.virtual_memory().total)/(1024**3)

# cpu / memory tracking

LOG_append(fcpu,"# LOG FILE {0} [{1}]",time.strftime("%Y-%m-%d %H:%M:%S"),sys.argv[0])
LOG_append(fcpu,"# time | [cpu %]")

LOG_append(fmem,"# LOG FILE {0} [{1}]",time.strftime("%Y-%m-%d %H:%M:%S"),sys.argv[0])
LOG_append(fmem,"# time | mem GB | mem %")

init_time = time.time()

while True: # infinite loop (with sleep)
    
    epoc_time = time.time() - init_time # somewhat hacky
    
    # cpu tracking
    
    cpu_usage = ps.cpu_percent(interval=interval,percpu=True)
    cpu_usage = [float(cpu)/100 for cpu in cpu_usage]
    cpu_field = " ".join(str(cpu) for cpu in cpu_usage)
    
    LOG_append(fcpu,"{0} {1}",epoc_time,cpu_field)
    
    # memory tracking
    
    mem_fixed = float(ps.virtual_memory().total - ps.virtual_memory().available)/(1024**3)
    mem_usage = float(ps.virtual_memory().percent)/100
    mem_field = " ".join([str(mem_fixed),str(mem_usage)])
    
    LOG_append(fmem,"{0} {1}",epoc_time,mem_field)
    
    # time.sleep(interval) # not be needed as ps.cpu_percent waits interval