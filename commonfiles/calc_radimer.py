import os
import MDAnalysis as mda
import numpy as np
home_dire=os.environ["WEST_SIM_ROOT"]
u_parent=mda.Universe(home_dire+'/cg_ABCD_119.pdb','parent.dcd')
u_new=mda.Universe(home_dire+'/cg_ABCD_119.pdb','seg.dcd')
ref=mda.Universe(home_dire+'/abcd_capsid.pdb')
capsid_all=ref.select_atoms("all")
com_capsid=capsid_all.center_of_mass()
neighbor_list=ref.select_atoms("segid A2 or segid B2 or segid C1 or segid D1 or segid A5 or segid B5 or segid C5 or segid D5")
com_neighborlist=neighbor_list.center_of_mass()
neighbor_vec=com_neighborlist-com_capsid
def vec_frame(u):
    our_dimer=u.select_atoms("segid A1 or segid B1")
    com_dimer=our_dimer.center_of_mass()
    dimer_vec=com_dimer-com_capsid
    return dimer_vec
for ts in u_parent.trajectory[-1:]:
    angle_com=np.dot(vec_frame(u_parent),neighbor_vec)/(np.linalg.norm(vec_frame(u_parent))*np.linalg.norm(neighbor_vec))
    print(np.round(angle_com,3))
for ts in u_new.trajectory[0:]:
    angle_com=np.dot(vec_frame(u_new),neighbor_vec)/(np.linalg.norm(vec_frame(u_new))*np.linalg.norm(neighbor_vec))
    print(np.round(angle_com,3))
