
<h1> How to get setup and started with Weighted Ensemble Simulations: Links to tutorials, papers, basic setup   <h1>

## Conda setup

 **Create  conda package and install westpa:**
  https://github.com/westpa/westpa/wiki/Installing-WESTPA

`conda create -n westpa2 python=3.11`

`conda activate westpa`

`    conda install -c conda-forge westpa`

Checkout the link for alternative installation methods

## Steps,folders and description
- Make sure to have a python script/alternative script that runs your MD simulations with OpenMM/HOOMD/simulation package. 
    - In this setup this file is: `./run_oligomer_simulation.py`
-    Make sure to have a file that calculates your progress coordinate. Here you probably alreaady have a good idea about your progress coordinate and are testing it with WE simulations now. 
        - For more resources on what's  a good progress coordinate/ reaction coordinate look into 
- Calculation of progress coordinate for WE trajectories has two parts:
  - The first file calculates value of progress coordinate at source state and target state. 
  - In this setup this file is: `./commonfiles/sum_interface_init.py`
  - The second file is `./commonfiles/sum_interface.py` This calculates the progress coordinate for each trajectory at a frequency we want. We don't want the frequency to be too high.


### ./westpa_scripts has all the files that we actually need to run the simulations. 
- Two important files here are : 
  - `./westpa_scripts/get_pcoord.sh` which calculates source pcoord and feeds it into $WEST_PCOORD_RETURN
  -  `./westpa_scripts/runseg.sh` actually takes care of running dynamics, propragating trajectories, pcoord calculation

### WE configuration file: `./west.cfg`
- Define dimensionality of progress coordinate. Starting with dimension=1 is the most practical. Try to keep the dimension $\leq 2$ Otherwise the number of parallel running trajectories will blow up.
- Pcoord len takes care of how frequently we are calculating prog coord for each trajectory. Depending on how closely you monitor prog c for each traj.
- Mapper: Probably good idea to start with rectilinear map but MAB is the smarter way especially if the binding/assembly process possibly takes a long time.
- bin_target_counts: number of traj you want in each bin
- max_total_iterations: how many iterations you want to run WE simulation for and also maximum wall clock time.

## other miscellaneous but important files/forders
- `./env.sh` sets up environment variables.
- `./init.sh` takes care of starting from ieration 0. Don't execute this if you're restarting WE run.
- `./tstate.file` has the value of target prog coord
- `./bstates` contains the starting trajectories/ source trajectories we start our simulations from. `/bstates/bstates.txt` contains probability of each of this starting trajectory