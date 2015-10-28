#!/usr/bin/env python
# coding=utf-8
import numpy as np

def phi(Z):
    val=np.angle(Z.val, deg=True)
    err=np.rad2deg(Z.err/abs(Z.val))
    return Z.T, val, err

if (__name__=="__main__"):
    pass