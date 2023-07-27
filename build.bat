@echo off

g++ -O3 -o .\build\cpp(linux) .\src\fib.cpp
gcc -O3 -o .\build\c(linux) .\src\fib.c
rustc -C opt-level=3 -o .\build\rust(linux) .\src\fib.rs
fpc -O3 -o.\build\pascal(linux) .\src\fib.pas
move .\build\fib.o .\build\pascal(linux)
