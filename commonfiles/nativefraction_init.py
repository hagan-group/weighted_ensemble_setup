#!/usr/bin/env/python
#nativefraction_init.py
#Calculate fraction of native contacts between two dimers
import MDAnalysis as mda
from MDAnalysis.analysis import rms, contacts
import MDAnalysis.lib.util
import numpy as np
import pickle
from numpy.linalg import norm
import nativecontacts_gen
import os
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/trimer_avg.pdb')
u=mda.Universe(home_dire+'/trimer_separate.pdb')


native_frac_AA=nativecontacts_gen.interaction_energy(ref,'A2','A1',energy_repulsion=0.15,energy_attraction=0.35)
native_frac_BC=nativecontacts_gen.interaction_energy(ref,'B1','C1',energy_repulsion=0.15,energy_attraction=0.35)
native_frac_DB=nativecontacts_gen.interaction_energy(ref,'D1','B2',energy_repulsion=0.15,energy_attraction=0.35)
native_frac_systemAA=nativecontacts_gen.interaction_energy(u,'A2','A1',energy_repulsion=0.15,energy_attraction=0.35)
native_frac_systemBC=nativecontacts_gen.interaction_energy(u,'B1','C1',energy_repulsion=0.15,energy_attraction=0.35)
native_frac_systemDB=nativecontacts_gen.interaction_energy(u,'D1','B2',energy_repulsion=0.15,energy_attraction=0.35)

print(f'{native_frac_BC}')
print(f'{native_frac_systemBC}')

