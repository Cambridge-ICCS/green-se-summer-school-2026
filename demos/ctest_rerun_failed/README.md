# CTest demo

This example demonstrates how to use `ctest --rerun-failed` to run subsets of a
test suite written using CTest.

1. Take a look at the temperature conversion library in
   [conversion.c](conversion.c). Don't modify it yet.
2. Take a look at the accompanying test suite files with the pattern `test_*.c`.
   Don't modify them yet.
3. Compile the library and test suite using CMake:
```sh
mkdir build
cd build
cmake ..
cmake --build .
```
4. Try running the test suite with `ctest --verbose` and inspect the failures.
5. Track down each issue, recompiling and running
   `ctest --verbose --rerun-failed` each time you make a fix. You should see
   that fewer tests are run each time.
