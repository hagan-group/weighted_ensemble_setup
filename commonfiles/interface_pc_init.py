#!/usr/bin/env/python
#combo_pc_init.py
import com_interface
import MDAnalysis as mda
import os
import nativecontacts_gen
import argparse
home_dire=os.environ["WEST_SIM_ROOT"]
#ref=mda.Universe(home_dire+'/pentamer_avg.pdb')
#initial=mda.Universe(home_dire+'/pentamer_separate.pdb')
class ParameterReader:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Parameter Reader')
        self.parser.add_argument('--dimer1', type=str)
        self.parser.add_argument('--dimer2', type=str)
        # Add more parameters as needed

    def read_parameters(self):
        args = self.parser.parse_args()
        return args



def combined_cf(u,m1,m2,erep,eatt):
    com=com_interface.com(u,m1,m2)
    if(com<50.0):
        native_frac=nativecontacts_gen.interaction_energy(u,m1,m2,energy_repulsion=erep,energy_attraction=eatt)
        #print(native_frac)
        #print(com)
        return com*(1-native_frac)
    else:
        return com




if __name__ == "__main__":
    reader = ParameterReader()
    params = reader.read_parameters()

    # Accessing parameters
    #psfile=params.psfpath
    #pdbfile=params.pdbpath
    d1= params.dimer1
    d2= params.dimer2
    combined_cf(ref,d1,d2,0.15,0.4)
    combined_cf(initial,d1,d2,0.15,0.4)
