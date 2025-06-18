#!/usr/bin/env/python
#combo_pc_init.py
import interface_pc
import MDAnalysis as mda
import os
home_dire=os.environ["WEST_SIM_ROOT"]
u=mda.Universe(home_dire+'/cg_ABCD_119.pdb','seg.dcd')
u_parent=mda.Universe(home_dire+'/cg_ABCD_119.pdb','parent.dcd')

for ts in u_parent.trajectory[-1:]:
    print(interface_pc.combined_cf(u_parent,'B1','C1',0.15,0.4)+interface_pc.combined_cf(u_parent,'A1','A5',0.15,0.4))
for ts in u.trajectory[0:]:
    print(interface_pc.combined_cf(u,'B1','C1',0.15,0.4)+interface_pc.combined_cf(u_parent,'A1','A5',0.15,0.4))
