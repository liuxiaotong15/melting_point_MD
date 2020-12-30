# melting_point_MD

calculate the melting point based on MD.

# dependency

ASE, openkim ("All models are wrong, but some are useful." George E. P. Box)

## openkim building process

1. https://openkim.org/doc/usage/obtaining-models/#source_install to install kim-api-collection-management

2. pip install kimpy

3. pip install git+https://github.com/openkim/kim-python-utils

4. pip install git+https://gitlab.com/ase/ase.git

## model install

kim-api-collection-management install user EAM_NN_Johnson_1988_Cu__MO_887933271505_002 (or ***)

# workflow

1. Berendsen NPT dynamics: volume at different temprature

2. find the inflection point of the volume
