#!/usr/bin/env/python

import MDAnalysis as mda
#from MDAnalysis.tests.datafiles import PSF, DCD, CRD
from MDAnalysis.analysis import rms,contacts
import MDAnalysis.lib.util
import numpy as np
import pickle
import os, sys
import nativecontacts_gen

this=os.getcwd()

home_dire=os.environ["WEST_SIM_ROOT"]
u = mda.Universe(home_dire+'/trimer_separate.pdb', 'seg.dcd')
u_parent = mda.Universe(home_dire+'/trimer_separate.pdb', 'parent.dcd')
#ds = pickle.load(open( "../../../commonfiles/contactIndices.npy", "rb" ) )
def nativefrac_traj(u,trajBeg=0,trajEnd=None):
    for ts in u.trajectory[trajBeg:trajEnd]:
        print(nativecontacts_gen.interaction_energy(u,'B1','C1',energy_repulsion=0.15,energy_attraction=0.35))

nativefrac_traj(u_parent,trajBeg=-1)
nativefrac_traj(u)

