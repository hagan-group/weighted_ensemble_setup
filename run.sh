#!/bin/bash

# Make sure environment is set
source env.sh

# Clean up
#rm -f west.log
export OPENBLAS_NUM_THREADS=1
# Run w_run
w_run --work-manager processes "$@" 
