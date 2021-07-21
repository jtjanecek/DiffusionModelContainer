# py2jags

# Usage

1. Initialization of chains
'''
singularity run py2jags.sif --name test --mode init --conditions conditions.csv --rts rts.csv --groups groups.csv --bind example_inputs/:/inputs,.:/workdir --nchains 6 --niter 1000 --nthin 1
'''

2. Execution
'''
singularity run py2jags.sif --name test --mode exec --bind model_1:/workdir --chain_num all --parallel True
'''

3. Convergence, formatting, and analysis
'''
singularity run py2jags.sif --name test --mode format --bind model_1:/workdir --chain_num all --parallel True
'''
