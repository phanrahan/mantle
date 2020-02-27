from setuptools import setup

setup(
    name='mantle',
    version='2.0.5',
    url='https://github.com/phanrahan/mantle',
    license='MIT',
    maintainer='Lenny Truong',
    maintainer_email='lenny@cs.stanford.edu',
    description='The magma standard library',
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
        "fault>=1.0.*",
        "magma-lang>=2.0.0",
    ],
    python_requires='>=3.6'
)
