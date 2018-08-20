from setuptools import setup

setup(
    name='mantle',
    version='0.1',
    description='Library of hardware primitives for programming FPGAs',
    packages=[
        "mantle",
        "mantle.common",
        "mantle.coreir",
        "mantle.lattice",
        "mantle.lattice.mantle40",
        "mantle.lattice.ice40",
        "mantle.verilog",
        "mantle.primitives",
        "mantle.util",
        "mantle.util.lfsr",
        "mantle.util.sort",
        "mantle.util.compressor",
        "mantle.util.lhca",
    ],

    install_requires=[
        "six",
        "coreir",
        "fault==0.20",
        "coreir==0.23a0",
        "bit_vector==0.30a0"
    ],
    url='https://github.com/phanrahan/mantle',
    maintainer='Leonard Truong',
    maintainer_email='lenny@cs.stanford.edu',
    python_requires='>=3.6'
)
