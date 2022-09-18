# WebAssembly test
Compile other example to WebAssembly.  
The script compiles several examples to linux executable files and WebAssembly at the same time , execute them and show inference time spent.
# build
```
# tested on ubuntu 22.04
apt install build-essential cmake  emscripten  git nodejs python3 
cd examples/webAssembly_test
# run build script 
python3 test.py
```