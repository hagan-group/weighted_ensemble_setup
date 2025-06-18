#!/bin/bash
#SBATCH --job-name=trimers_westpa_msm
#SBATCH --partition=skx
##SBATCH --nodelist=compute-1-9,compute-3-16,compute-5-[3,12]
#SBATCH --nodes=1
##SBATCH --cpus-per-task=48
#SBATCH --ntasks=48
#SBATCH --output=slurm.out
#SBATCH --error=slurm.err
#SBATCH --time=23:00:00
#SBATCH --mail-type=all
##SBATCH -mail-type=end
##SBATCH -mail-type=fail
#SBATCH --mail-user=smritipradhan@brandeis.edu
#
# run.sh
#
# Run the weighted ensemble simulation. Make sure you ran init.sh first!
#
#module purge
#module load intel/2017.1.132 amber/16
#module unload python
#export WEST_PYTHON=($which python2.7)
#module load share_modules/NAMD/2.13b2_mpi_sp
#module load gcc/13.2.0 
#module load intel/24.0  
#module load impi/21.11  
# Setup our OpenMM environment. 
# You have to set MSBS_ROOT correctly for your system 
#eval "$(conda shell.bash hook)" 
source /home1/09816/smritipradhan/.bashrc 
conda activate westpa_0.09
export OPENBLAS_NUM_THREADS=1
source env.sh
#source init.sh
#export OMPI_MCA_pml=ob1
#export OMPI_MCA_btl="self,tcp"
#export OMPI_MCA_opal_warn_on_missing_libcuda=0
#export LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH
#which mpirun
#rm -f west.log
#~/miniconda3/envs/benchmark/bin/mpirun -n $SLURM_NTASKS w_run --work-manager mpi "$@" &> west160.log
w_run --work-manager processes "$@" &>> west.log

