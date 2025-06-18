
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
    - In this setup this file is: ./run_oligomer_simulation.py
-    Make sure to have a file that calculates your progress coordinate. This has two parts:
    - The first file that calculates 


