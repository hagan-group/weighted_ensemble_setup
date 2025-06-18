import os
import MDAnalysis as mda
import interface_pc_init
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/trimer_avg.pdb')
initial=mda.Universe(home_dire+'/trimer_separate.pdb')
print(interface_pc_init.combined_cf(ref,'B1','C1',0.15,0.4)+interface_pc_init.combined_cf(ref,'A2','A1',0.15,0.4)+interface_pc_init.combined_cf(ref,'D1','B2',0.15,0.4))
print(interface_pc_init.combined_cf(initial,'B1','C1',0.15,0.4)+interface_pc_init.combined_cf(initial,'A2','A1',0.15,0.4)+interface_pc_init.combined_cf(initial,'D1','B2',0.15,0.4))
