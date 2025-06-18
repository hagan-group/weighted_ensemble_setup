#!/bin/bash
#runseg.sh
# Make sure environment is set
#this script is run for each trajectory segment. westpa supplies environment variables unique to each segment.
#west_current_seg_ref: path to where the current trajectory segment's data is stored. Become west_parent_date_ref  if any child segment spawns from this segment.
#west_parent_data_ref: path to file or directory containing data for parent segment.

#source env.sh

# Clean up
#rm -f west.log
#random_number=$RANDOM
#random_number1=$(echo $random_number + 1 | bc) 
#echo $random_number
#echo $random_number1
# Run w_run
#w_run --work-manager processes "$@" &> west.log!/bin/bash

if [ -n "$SEG_DEBUG" ] ; then
  set -x
  env | sort
fi
####################### Setup for running teh dynamics ####################
#setup directoryt where data for this segment is stored
cd $WEST_SIM_ROOT
mkdir -pv $WEST_CURRENT_SEG_DATA_REF
cd $WEST_CURRENT_SEG_DATA_REF
echo $WEST_CURRENT_SEG_DATA_REF

#sed "s/RAND/$WEST_RAND16/g" $WEST_SIM_ROOT/common_files/run_md.py > run_md.py

# Make symbolic links to topology and parameter files. These are not unique to each segment
# QUESTION: Is the pdb file for bounded target file or initial non-bounded basis file
#cp $WEST_SIM_ROOT/trimer_min.pdb .
#cp $WEST_SIM_ROOT/*txt .
#ln -sv $WEST_SIM_ROOT/commonfiles/AB-05.par structure1.par
#ln -sv $WEST_SIM_ROOT/commonfiles/cg_05.par structure2.par
#ln -sv $WEST_SIM_ROOT/commonfiles/SOD.par structure3.par
#Also copy the parameter files here

## uncomment the following code when HDF5 framework is off ##
# don't use symbolic links, as the folders are turned into .h5 files
#ln -sv $WEST_SIM_ROOT/common_files/bstate.psf .
#ln -sv $WEST_SIM_ROOT/common_files/bstate.pdb .
#cp $WEST_PARENT_DATA_REF/seg.xml ./parent.xml 
#cp $WEST_PARENT_DATA_REF/seg.dcd ./parent.dcd

# Run the dynamics with OpenMM
# python run_md.py SEED GPU_DEVICE
#echo 'Will run dynamics'
#echo python $WEST_SIM_ROOT/common_files/run_md.py $WEST_RAND16 $WM_PROCESS_INDEX
#python $WEST_SIM_ROOT/common_files/run_md.py $WEST_RAND16 $WM_PROCESS_INDEX
#random_number=$RANDOM
#random_number1=$(echo $random_number + 1 | bc) 
#

#Run the dynamics with NAMD
#WEighted ensemble  requires dynamics are stochatstic. 
#sed "s/RAND/$random_number1/g" \
 # $WEST_SIM_ROOT/commonfiles/md.conf > md.conf

# Trajectory segment will start off where it's parent segment left off. 
#ln -sv $WEST_PARENT_DATA_REF/seg.coor ./parent.coor
#ln -sv $WEST_PARENT_DATA_REF/seg.dcd  ./parent.dcd
#ln -sv $WEST_PARENT_DATA_REF/seg.vel  ./parent.vel
#ln -sv $WEST_PARENT_DATA_REF/seg.xsc  ./parent.xsc
ln -sv $WEST_PARENT_DATA_REF/seg.dcd ./parent.dcd
ln -sv $WEST_PARENT_DATA_REF/seg.xml ./parent.xml
#cp $WEST_SIM_ROOT/run_main_simulation.py .
#cp $WEST_SIM_ROOT/setup_system.py .
python $WEST_SIM_ROOT/run_oligomer_simulation.py --Erepulsion 0.15 --Enative 0.4 > seg.log
# Run the dynamics: Propagate the segment using namd2
#/home/smriti/Downloads/NAMD_2.14_Linux-x86_64-multicore/namd2 md.conf > seg.log
#echo $PWD
#Calculate and return data
#python $WEST_SIM_ROOT/commonfiles/com.py > $WEST_PCOORD_RETURN
#COMDIST=$(mktemp)
#echo $COMDIST
# Use a custom python script to calculate the distance between the Na+ and Cl-
# ions. This script looks for files named 'nacl.psf' and 'seg.dcd'.
#python $WEST_SIM_ROOT/commonfiles/combo_pc.py > pcAA.dat
#cat pcAA.dat
#echo $COMDIST
#NAFRAC= $(mktemp)
#echo $NAFRAC
#python $WEST_SIM_ROOT/commonfiles/comboBC_pc.py > pcBC.dat
#echo $NAFRAC
#cat pcBC.dat
python $WEST_SIM_ROOT/commonfiles/sum_interface.py > pc.dat
cat pc.dat
cat pc.dat > $WEST_PCOORD_RETURN
echo $WEST_PCOORD_RETURN
#cat $WEST_PCOORD_RETURN | tail -n 20 > $pcoord_traj
#echo $pcoord_traj > pcoord.dat 
#pcoord_traj="$(python $WEST_SIM_ROOT/commonfiles/cluster.py)"
#echo $pcoord_traj > pcoord.dat

#Calculate pcoord with MDAnalysis
#python $WEST_SIM_ROOT/commonfiles/dist.py > $WEST_PCOORD_RETURN


#cp bstate.pdb $WEST_TRAJECTORY_RETURN
#cp seg.dcd $WEST_TRAJECTORY_RETURN

#cp bstate.pdb $WEST_RESTART_RETURN
#cp seg.xml $WEST_RESTART_RETURN/parent.xml

#cp seg.log $WEST_LOG_RETURN

# Clean up
#rm -f dist.dat run_md.py
rm -f md.conf seg.pdb \
  seg.restart.coord seg.restart.coor.old seg.restart.vel seg.restart.vel.old\
  seg.restart.xsc seg.restart.xsc.old structure.psf
