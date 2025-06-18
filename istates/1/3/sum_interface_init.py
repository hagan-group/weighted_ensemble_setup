import os
import MDAnalysis as mda
import interface_pc_init
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/abcd_capsid.pdb')
initial=mda.Universe(home_dire+'/cg_ABCD_119.pdb')
print(interface_pc_init.combined_cf(ref,'B1','C1',0.15,0.4)+interface_pc_init.combined_cf(ref,'A1','A5',0.15,0.4))
print(interface_pc_init.combined_cf(initial,'B1','C1',0.15,0.4)+interface_pc_init.combined_cf(ref,'A1','A5',0.15,0.4))
