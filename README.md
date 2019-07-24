# Discretization couplings for Darcy and heat transport in discrete fracture network simulations
Source code and examples for the paper<br>
AAAAA

# Reproduce results from paper
Runscripts for all test cases of the work available [here](./examples).<br>
Note that you may have to revert to an older version of [PorePy](https://github.com/pmgbergen/porepy) to run the examples.

# Abstract
This study considers conceptual models to simulate single phase flow and heat transport on fracture networks. Fractures are commonly found in the underground and have a dramatic impact in the exploitation and management of natural resources therein present. We consider a Darcy model to compute the advective field (Darcy velocity) used in a subsequent heat transport and diffusion equation. In several applications, the rock matrix has a permeability which is several orders of magnitude lower than the one of the fractures and it can be thus ignored in the flow computation, giving the commonly known discrete fracture network model. For the heat equation, the matrix response is modeled as a zeroth-order operator. One of the most challenging aspects in these simulations is how to couple the fracture grids. Our aim is to compare solution strategies presented in the literature to understand the impact of assumptions and algorithm choices on the accuracy of the outcomes. Conforming and non-matching couplings among fractures lead to different approaches, with pros and cons. We present the mathematical and numerical schemes and with three examples of increasing difficulties we carefully compare the results obtained.

# Citing
If you use this work in your research, we ask you to cite the following publication AAAA

# PorePy version
If you want to run the code you need to install [PorePy](https://github.com/pmgbergen/porepy) and revert to commit f82a91c1b6ef83b6954ecd26723f8b7443880891 <br>
Newer versions of PorePy may not be compatible with this repository.

# License
See [license md](./LICENSE.md).
