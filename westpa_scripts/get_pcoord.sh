#!/bin/bash
#
# get_pcoord.sh
#
# This script is run when calculating initial progress coordinates for new 
# initial states (istates).  This script is NOT run for calculating the progress
# coordinates of most trajectory segments; that is instead the job of runseg.sh.

# If we are debugging, output a lot of extra information.
if [ -n "$SEG_DEBUG" ] ; then
  set -x
  env | sort
fi

# Make sure we are in the correct directory
cd $WEST_SIM_ROOT
source env.sh
echo $PWD
#python script to calculate progress coordinate for starting state
python $WEST_SIM_ROOT/commonfiles/sum_interface_init.py > pc.dat

tail -n 1 pc.dat > $WEST_PCOORD_RETURN
echo $WEST_PCOORD_RETURN
# Remove the temporary file to clean up
#rm $DIST

if [ -n "$SEG_DEBUG" ] ; then
  head -v $WEST_PCOORD_RETURN
fi
