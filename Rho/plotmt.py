from station import Station
from defineargs import args, lines
from plotrhoa import plotrhoa
from plotphi import plotphi
import matplotlib.pyplot as plt
import sys
     
if (__name__=="__main__"):
    stn=Station()
    argts = []
    argts = sys.argv[1:]

    components, files, z = args(argts)
    
    for i in range(len(z)):
        if z[i] == 'rhoa':
            plt.subplot(len(z),1,i+1)
            colors, fmts = lines(components)
            plotrhoa(files, components, stn, fmts, colors)
        else:
            plt.subplot(len(z),1,i+1)
            colors, fmts = lines(components)
            plotphi(files, components, stn, fmts, colors)
    
    plt.show()