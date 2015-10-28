#!/usr/bin/env python
# coding=utf-8
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