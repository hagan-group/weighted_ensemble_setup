#!/usr/bin/env/python
#combo_pc_init.py
import com_interface
import MDAnalysis as mda
import os
import nativecontacts_gen
home_dire=os.environ["WEST_SIM_ROOT"]
u=mda.Universe(home_dire+'/trimer_separate.pdb','seg.dcd')
u_parent=mda.Universe(home_dire+'/trimer_separate.pdb','parent.dcd')
def combined_cf(u,erep,eatt):
    com=com_interface.com(u,'A1','A2')
    if(com<40.0):
        native_frac=nativecontacts_gen.interaction_energy(u,'A2','A1',energy_repulsion=erep,energy_attraction=eatt)
        return com*(1-native_frac)
    else:
        return com
def calcpcUniv(u,trajBeg=0,trajEnd=None):
    for ts in u.trajectory[trajBeg:trajEnd]:
        print(combined_cf(u,0.15,0.35))
    
calcpcUniv(u_parent,trajBeg=-1)
calcpcUniv(u)
