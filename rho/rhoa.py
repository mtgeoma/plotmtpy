#!/usr/bin/env python
# coding=utf-8
import sys
import numpy as np
import jformat

class Impedance:
    def __init__(self, period, value, error):
        self.T = period
        self.val = value
        self.err= error

class Station:
    def __init__(self):
        self.stationName=""
        self.azimuth=0
        self.latitude=0
        self.longitude=0
        self.altitude=0
        self.Z={}

    def read(self,file_name):
        J=jformat.readJformat(file_name)

        self.stationName=J["HEAD"]["STATION"]
        self.azimuth=J["HEAD"]["AZIMUTH"]
        self.latitude=J["HEAD"]["LATITUDE"]
        self.longitude=J["HEAD"]["LONGITUDE"]
        self.altitude=J["HEAD"]["ELEVATION"]

        for component in (["ZXX","ZYY","ZXY","ZYX"]):
            tmp=np.array(J[component])
            T=np.array(tmp[:,0])
            R=np.array(tmp[:,1])
            I=np.array(tmp[:,2])
            std=np.array(tmp[:,3])
            self.Z[component]=Impedance(T,R+1j*I,std)

def rho_a(Z):
    uo=4.e-7*np.pi
    w=2.*np.pi/Z.T
    rho=abs(Z.val)**2/(w*uo)
    err=2*rho*Z.err/abs(Z.val)
    return Z.T, rho, err

def phi(Z):
    val=np.angle(Z.val, deg=True)
    err=np.rad2deg(Z.err/abs(Z.val))
    return Z.T, val, err

if (__name__=="__main__"):
    arq_jformat=sys.argv[1]
    component=sys.argv[2]
    
    stn=Station()
    stn.read(arq_jformat)
    
    T, rho, rho_err = rho_a(stn.Z[component])
    
    T, phi, phi_err = phi(stn.Z[component])

    print "> %s %s" % (stn.stationName, component)
    for j in range(0,len(T)):
        print "%10.4e %10.4e %10.4e %10.4e %10.4e" % \
            (T[j], rho[j], rho_err[j],phi[j],phi_err[j])
