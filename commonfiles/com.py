#!/usr/bin/env/python
import MDAnalysis as mda
#from MDAnalysis.tests.datafiles import PSF, DCD, CRD
from MDAnalysis.analysis import rms,contacts
import MDAnalysis.lib.util
import numpy as np
import pickle
from numpy.linalg import norm
import os
import sys
home_dire=os.environ["WEST_SIM_ROOT"]
u = mda.Universe(home_dire+'/trimer_separate.pdb', 'seg.dcd')
u_parent = mda.Universe(home_dire+'/trimer_separate.pdb', 'parent.dcd')

def com_dist_dimers(u):
    AB=u.select_atoms('segid A1 or segid B1')
    CD=u.select_atoms('segid C1 or segid D1')
    ABCD=u.select_atoms('segid A1 or segid B1 or segid C1 or segid D1')
    EF=u.select_atoms("segid A2 or segid B2")
    ABx=AB.center_of_mass()
    CDx=CD.center_of_mass()
    #ABCDx=ABCD.center_of_mass()
    EFx=EF.center_of_mass()
    dist1 = np.linalg.norm(CDx-ABx)
    dist2=np.linalg.norm(EFx-CDx)
    return dist1
def calcComDistUniv(u, trajBeg=0, trajEnd=None):
    for ts in u.trajectory[trajBeg:trajEnd]:
             print(com_dist_dimers(u))

calcComDistUniv(u_parent, trajBeg=-1)
calcComDistUniv(u)

