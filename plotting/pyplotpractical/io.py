import os
from datetime import datetime
from matplotlib import pyplot as pp

def savefig(pathname, format='png', timestamp=True, verbose=True, **kwargs):
    """Wrapper for pyplot.savefig that does some idiot proofing and adds some
    practical features, such as automatically creating the directory if it is
    missing, appending a timestamp, and being verbose about everything.
 
    Parameters:
      pathname    string (directory set to local when it is missing)
      format      string (default is png when extension is missing)
      timestamp   boolean (default is to prepend a timestamp to filename)
      verbose     boolean (default is verbose)
      kwargs      dict (passed to pyplot.savefig)"""
    
    if verbose:
        print "savefig: ",
    
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
        print "  appended timestamp"