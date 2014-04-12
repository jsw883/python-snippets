import sys
import os
from datetime import datetime
from matplotlib import pyplot as pp

def printtolog(pathname, header='', timestamp=True, verbose=True):
    """
    Initialises log file, automatically creating a directory if it is missing
    and appending a timestamp. Note that all python stdout will be redirected
    into this log.
    
    Parameters:
      pathname    string (directory set to local when it is missing)
      header      string (optional)
      verbose     boolean (default is verbose)
    """
    
    if verbose:
        print "printtolog:",
    
    dirname, filename = os.path.split(pathname)
    
    # create directory if missing
    if not dirname:
        dirname = os.path.abspath('.')
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        dirflag = 1
    else:
        dirflag = 0
    
    # append timestamp
    stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    if timestamp:
        filename = filename + '-' + stamp + '.log'
    else:
        filename = filename + '.log'
    
    pathlog = os.path.join(dirname,filename)
    
    if verbose:
        print pathlog
        print "  all following stdout will be redirected"
    
    sys.stdout = open(pathlog,'w')
    
    # open and print header if provided
    print "[LOG FILE " + stamp + "]"
    print ""
    if header:
        print header
    

def savefig(pathname, format='png', timestamp=True, verbose=True, **kwargs):
    """
    Wrapper for pyplot.savefig that does some idiot proofing and adds some
    practical features such as automatically creating a directory if it is
    missing, appending a timestamp, and being verbose about everything.
 
    Parameters:
      pathname    string (directory set to local when it is missing)
      format      string (default is png when extension is missing)
      timestamp   boolean (default is to prepend a timestamp to filename)
      verbose     boolean (default is verbose)
      kwargs      dict (passed to pyplot.savefig)
    """
    
    if verbose:
        print "savefig:",
    
    dirname, filename = os.path.split(pathname)
    
    # create directory if missing
    if not dirname:
        dirname = os.path.abspath('.')
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        dirflag = 1
    else:
        dirflag = 0
    
    # check if extension provided
    if len(filename.rsplit('.',1)) > 1:
        filename, format = filename.rsplit('.',1)
    
    # append timestamp
    stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    if timestamp:
        filename = filename + '-' + stamp + '.' + format
    else:
        filename = filename + '.' + format
    
    path = os.path.join(dirname,filename)
    
    pp.savefig(path,**kwargs)
    
    if verbose:
        print path
        if dirflag:
            print "  created missing directory"
        if timestamp:
            print "  appended timestamp " + stamp