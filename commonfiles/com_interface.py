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


def com(u,sel1,sel2):
    AB=u.select_atoms('segid '+sel1)
    CD=u.select_atoms('segid '+sel2)
    ABx=AB.center_of_mass()
    CDx=CD.center_of_mass()
    dist=np.linalg.norm(ABx-CDx)
    return dist

