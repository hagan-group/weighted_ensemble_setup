#!/bin/bash
export WEST_SIM_ROOT="$PWD"
#export WEST_SIM_ROOT= "$PWD"
[ -z "$WEST_SIM_ROOT" ] &&
    exit 1
[ ! -d $WEST_SIM_ROOT/traj_segs ] &&
    exit 1
#cd $WEST_SIM_ROOT
echo "$PWD"
cd $WEST_SIM_ROOT/traj_segs
echo "$PWD"
#echo $WEST_SIM_ROOT
ITERS=($(ls | grep '^[0-9][0-9][0-9][0-9][0-9][0-9]$'))
ITERS=("${ITERS[@]:0:${#ITERS[@]}-1}")
for ITER in ${ITERS[@]}; do
    [ ! -f $ITER.tar ] &&
        tar -cvf $ITER.tar $ITER
done

