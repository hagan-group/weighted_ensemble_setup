#!/usr/bin/env/python
#combo_pc_init.py
import com_interface
import MDAnalysis as mda
import os
import nativecontacts_gen
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/trimer_avg.pdb')
initial=mda.Universe(home_dire+'/trimer_separate.pdb')
def combined_cf(u,erep,eatt):
    com=com_interface.com(u,'B1','C1')
    if(com<40.0):
        native_frac=nativecontacts_gen.interaction_energy(u,'B1','C1',energy_repulsion=erep,energy_attraction=eatt)
        #print(native_frac)
        #print(com)
        return com*(1-native_frac)
    else:
        return com
print(combined_cf(ref,0.15,0.35))
print(combined_cf(initial,0.15,0.35))
