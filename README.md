# DiffusionModelContainer
This document is an all inclusive guide on how to run hierarchical Bayesian diffusion modeling for detecting group differences based on the models written for the Old/Young group comparison project.

To get access to the DiffusionModel repo, contact John Janecek.
https://github.com/jtjanecek/DiffusionModel
## 

## Getting Started
First, read a few papers regarding the assumptions made in diffusion modeling. It will be important to understand the basics of hierarchical diffusion modeling. 
Recommended readings: 
- Paper 1
- Paper2

Secondly, you'll need to understand some basics about MCMC simulation and Bayesian statistics.
Recommended resources:
- https://www.youtube.com/watch?v=OTO1DygELpY&t=3s
- 


## Installation
```
git clone git@github.com:jtjanecek/DiffusionModelContainer.git
sudo singularity build diffusion.simg DiffusionModelContainer/DiffusionModelRecipe.def
rm -rf DiffusionModelContainer
```

## Executing a model script
Recommended folder structure:
```
diffusion_folder
|-- diffusion.simg
|-- code
|    |-- script_1.py 
|    |-- script_2.py
|-- data
|    |-- conditions.csv 
|    |-- groups.csv
|    |-- rts.csv 
|-- workdir
```

Example running a script
```
singularity run -B workdir:/workdir,code:/code,data:/data diffusion.simg code/script_1.py
```

## What do I put in the python script?
Follow the instructions here: https://github.com/jtjanecek/DiffusionModel

