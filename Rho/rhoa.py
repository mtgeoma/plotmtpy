#!/usr/bin/env python
# coding=utf-8
import numpy as np

def rho_a(Z):
    uo=4.e-7*np.pi
    w=2.*np.pi/Z.T
    rho=abs(Z.val)**2/(w*uo)
    err=2*rho*Z.err/abs(Z.val)
    return Z.T, rho, err

if (__name__=="__main__"):
    pass