#!/bin/bash
set -x

err=0
# Use a trap to check for errors, we do this over set -e so that all the tests
# run (so that we may catch multiple errors)
trap 'err=1' ERR

py.test --target verilog tests/test_verilog
py.test --target coreir tests/test_coreir

py.test --target ice40 tests/test_ice40
#py.test --target ice40 tests/test_ice40 tests/test_mantle40
py.test --target spartan3 tests/test_spartan3
py.test --target spartan6 tests/test_spartan6
py.test --target greenpak4 tests/test_greenpak4

py.test --target coreir tests/test_mantle
py.test --target ice40 tests/test_mantle
py.test --target spartan3 tests/test_mantle
py.test --target spartan6 tests/test_mantle

# Return code is nonzero if an error occured
test $err = 0
