# DiffusionModelContainer
This document is an all inclusive guide on how to run hierarchical Bayesian diffusion modeling for detecting group differences based on the models written for the Old/Young group comparison project. This code is inspired by the  [Trinity MATLAB toolbox](https://github.com/joachimvandekerckhove/trinity) adapted to Python and containerized in order to better parallelize and to execute on high computing clusters. This container uses [JAGS](https://en.wikipedia.org/wiki/Just_another_Gibbs_sampler) as the MCMC sampler.

## Getting Started
First, read a few papers on diffusion modeling in order to understand the parameters and assumptions. It will be important to understand the basics of hierarchical diffusion modeling. Recommended readings: 
- Paper 1
- Paper 2

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
R


Example running a script
```
singularity run -B workdir:/workdir,code:/code,data:/data diffusion.simg code/script_1.py
```

## What do I put in the python script?
Follow the instructions here: https://github.com/jtjanecek/DiffusionModel


