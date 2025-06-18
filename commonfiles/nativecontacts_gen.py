import MDAnalysis as mda
import numpy as np
import pandas as pd
import os
home_dire=os.environ["WEST_SIM_ROOT"]
def interaction_energy(u,m1,m2,energy_repulsion,energy_attraction):
    count=0
    total_interaction_energy=0
    contactlist=pd.read_csv(home_dire+'/'+m1+'_'+m2+'_contacts.txt',sep='\t',header=None)
    for i in range(len(contactlist)):
        res1=contactlist.iloc[i][1]
        sel1=['segid',m1,'and','resid',str(res1)]
        sel1=' '.join(sel1)
        #print(sel1)
        dimer1=u.select_atoms(sel1)
        res2=contactlist.iloc[i][3]
        sel2=['segid',m2,'and','resid',str(res2)]
        sel2=' '.join(sel2)
        dimer2=u.select_atoms(sel2)
    
        pos1=dimer1.atoms.positions
        pos2=dimer2.atoms.positions
        delta=pos2[0]-pos1[0]
        r_cutoff=15
        distance = np.sqrt(np.dot(delta, delta))
        distancenew=contactlist.iloc[i][4]
        repulsive_energy=0.1184*energy_repulsion*(1+np.cos((np.pi*distance)/r_cutoff))
        #expr_gaussian_native_contacts="-Eatt*(A*exp(-B*r^2)+C*exp(-D*r^2))*step(r_ncg-r)"
        r_nc=30
        attractive_energy=-energy_attraction*(4.6*np.exp(-0.1*distance**2)+8.368*np.exp(-0.01*distance**2))*np.heaviside(r_nc-distance,1)
        #print(f'att={attractive_energy}')
        int_energy=attractive_energy+repulsive_energy
        #print(int_energy)
        if(int_energy<-0.5):
            count=count+1
        total_interaction_energy=total_interaction_energy+int_energy
       # print(total_interaction_energy)
    return count/len(contactlist)
