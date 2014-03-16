#!/bin/bash -x
PWD=$(cd swap; pwd)
for x in cwm cwm_py
do
    ln -sf $PWD/$x.py /usr/bin/$x
done
