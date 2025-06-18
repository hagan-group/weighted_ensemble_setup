import MDAnalysis as mda
import numpy as np
def interaction_energy(u,energy_repulsion,energy_attraction):
    ABCDpairs=np.asarray([(36,15), (36,18),(33,18),(37,120),(29,127),(32,127),(25,129), (23,132), (137,132), (139,134),(32,18), (33,124), (36,120),(37,18), (37,124),(36,14),(36,123), (37,124)])
    ABCDindex=ABCDpairs-1
    total_interaction_energy=0
    count=0
    for i in range(len(ABCDindex)):
        Abindex=ABCDindex[i][0]+149
        AB=u.select_atoms("index {}".format(Abindex))
    
        pos1=AB.atoms.positions
        Cdindex=ABCDindex[i][1]+298
    #print(Cdindex)
        CD=u.select_atoms("index {}".format(Cdindex))
        pos2=CD.atoms.positions
    #pos2=ABCD_universe.atoms[ABCDindex[i][1]].positions
        delta=pos2[0]-pos1[0]
    #print(pos2[0])
    #print(pos1[0])
    #print(delta)
        r_cutoff=15
        distance = np.sqrt(np.dot(delta, delta))
        repulsive_energy=0.1184*energy_repulsion*(1+np.cos((np.pi*distance)/r_cutoff))
        #expr_gaussian_native_contacts="-Eatt*(A*exp(-B*r^2)+C*exp(-D*r^2))*step(r_ncg-r)"
        r_nc=30
        attractive_energy=-energy_attraction*(4.6*np.exp(-0.1*distance**2)+8.368*np.exp(-0.01*distance**2))*np.heaviside(r_nc-distance,1)
        int_energy=attractive_energy+repulsive_energy
        #print(int_energy)
        if(int_energy<-0.5):
            count=count+1
        total_interaction_energy=total_interaction_energy+int_energy
    #print(total_interaction_energy)
    return count/18
