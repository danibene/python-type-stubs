#!/bin/sh

python -m pip install --upgrade pandas
python -m pip install --upgrade pyright
python -m pip install --upgrade docopt

mkdir -p stubs

# Copy over the stubs from here

for d in cv2-stubs gym-stubs matplotlib scipy-stubs sklearn-stubs transformers-stubs
do
    cp -R ../../$d stubs
done

