#!/bin/bash
#runseg.sh
# Make sure environment is set
#this script is run for each trajectory segment. westpa supplies environment variables unique to each segment.
#west_current_seg_ref: path to where the current trajectory segment's data is stored. Become west_parent_date_ref  if any child segment spawns from this segment.
#west_parent_data_ref: path to file or directory containing data for parent segment.


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

# Trajectory segment will start off where it's parent segment left off. 
## Whatever trajectory file we continue the next bin from. Change the name of last trajectory segment to parent trajectory.
ln -sv $WEST_PARENT_DATA_REF/seg.dcd ./parent.dcd
ln -sv $WEST_PARENT_DATA_REF/seg.xml ./parent.xml
## Run dynamics for this new trajectory
python $WEST_SIM_ROOT/run_oligomer_simulation.py --Erepulsion 0.15 --Enative 0.4 > seg.log
###python script for calculating progress coodinate for current trajectory
python $WEST_SIM_ROOT/commonfiles/sum_interface.py > pc.dat
cat pc.dat > $WEST_PCOORD_RETURN
echo $WEST_PCOORD_RETURN

# Clean up this is optional if you are storing restart coordinates or checkpoints during runs and want to clean up space
#rm -f dist.dat run_md.py

