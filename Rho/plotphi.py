from station import Station
from phi import phi
from plot import plot
from defineargs import args, lines
import matplotlib.pyplot as plt
import sys

def plotphi(files, components, stn, fmts, colors):
    for arq_jformat in files:
        for component in components:
            stn.read(arq_jformat)
            T, ph, ph_err = phi(stn.Z[component])
            plot(T, ph, ph_err, fmts, colors)
            
     
if (__name__=="__main__"):
    stn=Station()
    argts = []
    argts = sys.argv[1:]
    
    components, files, z = args(argts)
    
    colors, fmts = lines(components)
        
    plt.figure()

    plotphi(files, components, stn, fmts, colors)
    
    plt.show()