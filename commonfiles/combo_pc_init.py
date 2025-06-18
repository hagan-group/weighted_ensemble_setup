#!/usr/bin/env/python
#combo_pc_init.py
import com_init
import MDAnalysis as mda
import os
import nativecontacts_gen
import com_interface
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/trimer_avg.pdb')
initial=mda.Universe(home_dire+'/trimer_separate.pdb')

nativefracref=nativecontacts_gen.interaction_energy(ref,'A2','A1',energy_repulsion=0.15,energy_attraction=0.35)
nativefracsystem=nativecontacts_gen.interaction_energy(initial,'A2','A1',energy_repulsion=0.15,energy_attraction=0.35)
def combined_cf(u,erep,eatt):
    com=com_interface.com(u,'A1','A2')
    if(com<50.0):
        native_frac=nativecontacts_gen.interaction_energy(u,'A2','A1',energy_repulsion=erep,energy_attraction=eatt)
        return com*(1-native_frac)
    else:
        return com
print(combined_cf(ref,0.15,0.35))
print(combined_cf(initial,0.15,0.35))
