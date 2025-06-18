import os
import MDAnalysis as mda
import numpy as np
home_dire=os.environ["WEST_SIM_ROOT"]
ref=mda.Universe(home_dire+'/abcd_capsid.pdb')
initial=mda.Universe(home_dire+'/cg_ABCD_119.pdb')
capsid_all=ref.select_atoms("all")
com_capsid=capsid_all.center_of_mass()
neighbor_list=ref.select_atoms("segid A2 or segid B2 or segid C1 or segid D1 or segid A5 or segid B5 or segid C5 or segid D5")
com_neighborlist=neighbor_list.center_of_mass()
our_dimer_initial=initial.select_atoms("segid A1 or segid B1")
com_dimer_initial=our_dimer_initial.center_of_mass()
dimer_vec_initial=com_dimer_initial-com_capsid
our_dimer_ref=ref.select_atoms("segid A1 or segid B1")
com_dimer_ref=our_dimer_ref.center_of_mass()
dimer_vec_ref=com_dimer_ref-com_capsid
neighbor_vec=com_neighborlist-com_capsid
angle_com_ref=np.dot(dimer_vec_ref,neighbor_vec)/(np.linalg.norm(dimer_vec_ref)*np.linalg.norm(neighbor_vec))
angle_com_ref=np.round(angle_com_ref,3)
angle_com_initial=np.dot(dimer_vec_initial,neighbor_vec)/(np.linalg.norm(dimer_vec_initial)*np.linalg.norm(neighbor_vec))
angle_com_initial=np.round(angle_com_initial,3)
print(angle_com_ref)
print(angle_com_initial)
