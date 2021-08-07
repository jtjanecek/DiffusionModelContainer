# DiffusionModelContainer
To get access to the DiffusionModel repo, contact John Janecek.
https://github.com/jtjanecek/DiffusionModel

# Installation
```
git clone git@github.com:jtjanecek/DiffusionModelContainer.git
sudo singularity build diffusion.simg DiffusionModelContainer/DiffusionModelRecipe.def
rm -rf DiffusionModelContainer
```

# Executing
Write a script that utilizes the DiffusionModel library.

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
singularity run -B workdir:/workdir,code:/code,data:/data diffusion.simg code/script.py
```

# What do I put in the python script?
Follow the instructions here: https://github.com/jtjanecek/DiffusionModel
