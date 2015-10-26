from rhoa import Station, rho_a
import matplotlib.pyplot as plt
import sys

def plot(T, rho, rho_err):
    plt.errorbar(T, rho, yerr=rho_err, fmt='o', color='red', mec='white')
    plt.semilogx()
    plt.semilogy()
    plt.ylim(0.1, 100000)
     
     
if (__name__=="__main__"):
    arq_jformat=sys.argv[1]
    component=sys.argv[2]

    stn=Station()
    stn.read(arq_jformat)
    # rho, stdRho = rhoa(stn.T[component],stn.Z[component],stn.Zstd[component])
    T, rho, rho_err = rho_a(stn.Z[component])
    
    plot(T, rho, rho_err)
    
    plt.show()