#!/usr/bin/env/python
#com_init.py
#Calculate center of mass distance between two dimers
import MDAnalysis as mda
from MDAnalysis.analysis import rms, contacts
import MDAnalysis.lib.util
import numpy as np
import pickle
from numpy.linalg import norm
import os


def com(u):
    AB=u.select_atoms('segid A1 or segid B1')
    CD=u.select_atoms('segid C1 or segid D1')
    ABCD=u.select_atoms('segid A1 or segid B1 or segid C1 or segid D1')
    EF=u.select_atoms('segid A2 or segid B2')
    ABx=AB.center_of_mass()
    CDx=CD.center_of_mass()
    ABCDx=ABCD.center_of_mass()
    EFx=EF.center_of_mass()
    distBC=np.linalg.norm(ABx-CDx)
    distAA = np.linalg.norm(ABx-EFx)
    return distBC, distAA
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/trimer_avg.pdb')
initial=mda.Universe(home_dire+'/trimer_separate.pdb')
com_ref=com(ref)
com_intial=com(initial)
print(com_ref)
print(com_intial)
