from station import Station
from rhoa import rho_a
from phi import phi
import matplotlib.pyplot as plt
import sys

def plot(x, y, err):
    plt.errorbar(x, y, yerr=err, fmt='o', color='red', mec='white')
    plt.semilogx()
    plt.semilogy()
    plt.ylim(0.1, 100000)
     
if (__name__=="__main__"):
    arq_jformat=sys.argv[1]
    component=sys.argv[2]

    stn=Station()
    stn.read(arq_jformat)

    T, rho, rho_err = rho_a(stn.Z[component])
    plot(T, rho, rho_err)
    
    T, phi, phi_err = phi(stn.Z[component])
    # plot(T, phi, phi_err)
    
    print "> %s %s" % (stn.stationName, component)
    for j in range(0,len(T)):
        print "%10.4e %10.4e %10.4e %10.4e %10.4e" % \
            (T[j], rho[j], rho_err[j],phi[j],phi_err[j])
    
    plt.show()