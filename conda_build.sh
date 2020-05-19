#!/bin/bash

set -e

ARRAY=( 3.6 3.7 3.8 )

export CONDA_BLD_PATH=~/conda-bld

for i in "${ARRAY[@]}"
do
	conda-build conda.recipe/ --python $i
done

# convert package to other platforms
platforms=( osx-64 linux-64 win-64 )
find $CONDA_BLD_PATH/ -name *.tar.bz2 | while read file
do
    echo $file
    #conda convert --platform all $file  -o $HOME/conda-bld/
    for platform in "${platforms[@]}"
    do
       conda convert --platform $platform $file  -o $CONDA_BLD_PATH/
    done
done

# upload packages to conda
find $CONDA_BLD_PATH/ -name *.tar.bz2 | while read file
do
    echo $file
    anaconda upload -u mrossol $file
done

echo "Building and uploading conda package done!"
conda build purge