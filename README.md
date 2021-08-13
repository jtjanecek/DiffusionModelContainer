# DiffusionModelContainer
This document is an all inclusive guide on how to run hierarchical Bayesian diffusion modeling for detecting group differences based on the models written for the Old/Young group comparison project. This code is inspired by the  [Trinity MATLAB toolbox](https://github.com/joachimvandekerckhove/trinity) adapted to Python and containerized in order to better parallelize and to execute on high computing clusters. This container uses [JAGS](https://en.wikipedia.org/wiki/Just_another_Gibbs_sampler) as the MCMC sampler.

## Getting Started
First, read a few papers on diffusion modeling in order to understand the parameters and assumptions. It will be important to understand the basics of hierarchical diffusion modeling. Recommended readings: 
- [Hierarchical diffusion models for two-choice response times.](https://lirias.kuleuven.be/retrieve/157366)
- [A Bayesian approach to diffusion models of decision-making and response time](https://digital.library.adelaide.edu.au/dspace/bitstream/2440/68612/2/hdl_68612.pdf)

Second, you'll need to understand some basics about MCMC simulation and Bayesian statistics. Recommended resources:
- https://www.youtube.com/watch?v=OTO1DygELpY&t=3s
- [Bayesian Cognitive Modeling: A Practical Course](https://bayesmodels.com/)
- UCI Bayesian Experts:
        - [Michael Lee](https://faculty.sites.uci.edu/mdlee/bgm/) (Bayesian modeling)
        - [Joachim Vandekerckhove](https://www.faculty.uci.edu/profile.cfm?faculty_id=6237) (Bayesian modeling, Diffusion modeling)

Third, you will need to have Singularity installed. This is the only software requirement needed.


## Repo structure
This repo contains the [Singularity](https://sylabs.io/guides/3.5/user-guide/introduction.html) definition file for building a Singularity image. This container pulls from the [Python Diffusion Model base code repo](https://github.com/jtjanecek/DiffusionModel). This container will containerize Python, JAGS, and jags-wiener-module. 

If you don't have access to the Python repo, contact John Janecek. You will need your github credentials to access the Python repo when you build the image.

## Setting up your data
You will need to format your data in a way that the model can read it. For the GroupComparison models, you will need the following CSVs:

| CSV            | Column Header? | Row Header? | Data                                                                    | Data type                                                               |
|----------------|----------------|-------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Groups         | Yes            | Yes         | The group number                                                        | Integer, starting at 1                                                  |
| Conditions     | Yes            | Yes         | The condition for this trial                                            | Integer, starting at 1                                                  |
| Reaction times | Yes            | Yes         | The reaction time. Positive = upper boundary, negative = lower boundary | Decimal, in seconds. Bounds are [-max_reaction_time,+max_reaction_time] |

[Example randomly generated data](https://github.com/jtjanecek/DiffusionModel/tree/master/example_inputs)


## Set up your directory structure
```
project_folder
|-- code
|    |-- # This is where the container and code will be stored
|-- data
|    |-- conditions.csv 
|    |-- groups.csv
|    |-- rts.csv 
|-- workdir
|    |-- # This is where the models will be stored and executed
```
Right now you won't have anything in your code and workdir folders, but we will change that next. 

## Downloading and building the Singularity Image
```
cd code
git clone git@github.com:jtjanecek/DiffusionModelContainer.git
sudo singularity build diffusion.simg DiffusionModelContainer/DiffusionModelRecipe.def
rm -rf DiffusionModelContainer
```
Your directory structure will now look like:
```
project_folder
|-- code
|    |-- diffusion.simg
|-- data
|    |-- conditions.csv 
|    |-- groups.csv
|    |-- rts.csv 
|-- workdir
|    |-- # This is where the models will be stored and executed
```
## Python Script to execute your code
You will be writing Python scripts to execute your code. Your new singularity compiled image, `diffusion.simg`, is only the environment for executing your Python scripts (with everything installed already!). The Python scripts will be responsible for telling the container what to execute. All paths within your Python scripts must be the paths based on the container. [Python code documentation](https://github.com/jtjanecek/DiffusionModel). [Example Python script that the image can run](test)

## Running the Singularity Image
The image requires you to mount your code, data, and workdir folders. It will also require you to pass in the name of the Python script you want to execute.  

Example running a script while in the `project_folder`:
```
singularity run -B workdir:/workdir,code:/code,data:/data code/diffusion.simg /code/run.py
```
Code breakdown:
```
# Runs the singularity image
singularity run 
# This binds directories in your computer into the image. This will bind the local workdir directory to /workdir in the container, etc
-B workdir:/workdir,code:/code,data:/data 
# The singularity image
code/diffusion.simg 
# The path (in the container) to the Python script you want to execute
/code/run.py
```
## Example SLURM script for the Stark Grid
Notes: 
- Change the `6` in `#SBATCH -c 6` to be the number of chains (so that the container can properly parallelize)
```
#!/bin/bash
# Setup qsub options
#  Nothing needed for this
#SBATCH -c 6
#SBATCH -o /mnt/yassamri2/MDTO-Diffusion/young_vs_old/code/logs/dm-%j.out
#SBATCH --partition=large
#SBATCH -w wario02

# Change directory to your project folder
cd /mnt/yassamri2/MDTO-Diffusion/young_vs_old/
echo Job ID: $SLURM_JOB_ID
echo Job name: $SLURM_JOB_NAME
echo Submit host: $SLURM_SUBMIT_HOST
echo "Node(s) used": $SLURM_JOB_NODELIST
echo "CPUS PER TASK: $SLURM_CPUS_PER_TASK"
echo "CPUS PER TASK: $SLURM_NPROCS"

# Run the code
singularity run -B workdir:/workdir,code:/code,data:/data code/diffusion.simg /code/run.py
```




