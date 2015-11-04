from station import Station
from rhoa import rho_a
import matplotlib.pyplot as plt
import sys

from itertools import cycle

def plot(x, y, err):
    plt.errorbar(x, y, yerr=err, fmt=fmts.next(), color=colors.next(), mec='white')
    plt.semilogx()
    plt.semilogy()
     
if (__name__=="__main__"):
    stn=Station()
    
    argts = []
    components = []
    files = []
    argts = sys.argv[1:]
    
    for a in argts:
        if a in ('ZXX', 'ZYY', 'ZXY', 'ZYX'):
            components.append(a)
        else:
            files.append(a)
            
    if len(components) == 1:
        colors = cycle(['blue', 'red', 'green', 'yellow'])
        fmts = cycle(['o'])
    
    elif len(components) == 2:
        colors = cycle(['blue','blue', 'red', 'red', 'green', 'green', 'yellow', 'yellow'])
        fmts = cycle(['s', 'o'])
        
    elif len(components) == 3:
        colors = cycle(['blue','blue', 'blue', 'red', 'red', 'red', 
                        'green', 'green', 'green', 'yellow', 'yellow', 'yellow'])
        fmts = cycle(['s', 'o', '^'])

    else:
        colors = cycle(['blue','blue', 'blue', 'blue', 'red', 'red', 'red', 'red', 
                        'green', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow', 'yellow'])
        fmts = cycle(['s', 'o', '^', 'd'])
        
    plt.figure()
    
    for arq_jformat in files:
        for component in components:
            stn.read(arq_jformat)
            T, rho, rho_err = rho_a(stn.Z[component])
            plot(T, rho, rho_err)
           
    plt.show()