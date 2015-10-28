from station import Station
from rhoa import rho_a
from phi import phi
import sys

if (__name__=="__main__"):
    arq_jformat=sys.argv[1]
    component=sys.argv[2]

    stn=Station()
    stn.read(arq_jformat)

    T, rho, rho_err = rho_a(stn.Z[component])
    
    T, phi, phi_err = phi(stn.Z[component])
    
    print "> %s %s" % (stn.stationName, component)
    print "\tT \tRho \tRho_err \tPhi \tPhi_err"
    for j in range(0,len(T)):
        print "%10.4e %10.4e %10.4e %10.4e %10.4e" % \
            (T[j], rho[j], rho_err[j],phi[j],phi_err[j])