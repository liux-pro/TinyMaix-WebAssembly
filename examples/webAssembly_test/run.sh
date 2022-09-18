#!/bin/bash
cd ../$1
rm -rf build
mkdir build
cd build
cmake .. -DCMAKE_CXX_COMPILER=g++ -DCMAKE_C_COMPILER=gcc
make
./$1


cd ..
rm -rf build
mkdir build
cd build
emcmake cmake .. -DCMAKE_CXX_COMPILER=em++ -DCMAKE_C_COMPILER=emcc
emmake make
node ./$1.js