#!/bin/bash
cd ../"$1" || exit
rm -rf build
mkdir build
cd build || exit
cmake .. -DCMAKE_CXX_COMPILER=g++ -DCMAKE_C_COMPILER=gcc
make
./"$1"

cd ..
rm -rf build
mkdir build
cd build || exit
emcmake cmake .. -DCMAKE_CXX_COMPILER=em++ -DCMAKE_C_COMPILER=emcc
emmake make
node ./"$1".js
