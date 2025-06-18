for i in `tail -n +9 $1|awk '{print $1"-"$2}'`;
do
# We need the iteration/walker indices as strings
# so we can name the file properly
iter=`echo $i|sed 's/-[0-9]*//'`
p_iter=`printf "%06d" $iter`
#echo $1
walk=`echo $i|sed 's/^[0-9]*//'|sed 's/-//'`
p_walk=`printf "%06d" $walk`
# Make the full path to the seg.xtc
TRJ_PATH=`printf "traj_segs/%06d/%06d" $iter $walk`
#echo $traj_segs
#echo $TRJ_PATH
# Copy into the folder!

#echo FULL_TRJ
cp $TRJ_PATH/seg.dcd FULL_TRJ/${p_iter}_${p_walk}.dcd
done
