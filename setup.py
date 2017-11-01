from setuptools import setup

from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=False)

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='mantleextra',
    version='0.1-alpha',
    description='Library of hardware primitives forprogramming FPGAs',
    packages=[
        "mantle",
        "mantle.common",
        "mantle.coreir",
        "mantle.lattice",
        "mantle.verilog",
        "mantle.primitives",
        "mantle.util",
        "mantle.util.lfsr",
        "mantle.util.sort",
        "mantle.util.compressor",
        "mantle.util.lhca",
    ],
    
    install_requires=reqs
    )
