---
layout: page
title: "Roadmap"
subheadline: "ToDo-List &amp; Ideas"
teaser: "Here are some ideas we hope to cover/implement in the future."
header:
   image_fullwidth: "header_roadmap_3.jpg"
permalink: "/roadmap/"
---

### Time: Friday 10:00 am CST

### Location: Loomis 322

## Current schedule (2020 Spring)

|:-------|:--------|:---------------------------:|
|  Date  | Person  | Subject                     |
|:-------|:--------|:---------------------------:|
|Feb. 14 | Ryan    |  Maximum Entropy - From Image Processing to Analytic Continuation  |
| <s>Feb. 28</s> | <s>???</s>     |    <s>? ?</s>  |
|Mar. 13 | Chad    |  Simulated Annealing  |
|Mar. 26 | Zeqian   |  Python Visualization |
|Apr. 10 | Matt    |  Modeling polarization on social media platforms   |
|Apr. 24 | Greg    |  Graph Cuts and Portfolio Optimization  |
|May. 08 | Kevin L.  | ? ?  |
|:-------|:--------|:---------------------------:|

[2016 schedule][1]

[2017sp schedule][2]

[2017fa schedule][3]

[2018sp schedule][4]

[2019sp schedule][5]

[2019fa schedule][6]


## Speaker Guidelines

**TL;DR** Do unto others as you would have them do unto you.

At minimum, an AIG presenter should prepare a few slides and an example code.
  1. The slides should explain:
    - what the algorithm is
    - how a minimum example works
    - why the algorithm might be practically useful
  2. A code that demonstrates the simplest problem the algorithm solves.
  3. Make a pull-request (PR) to the [website repository][repo] to make your presentation and code eternal. Follow instructions in the README.md file.

The presentation should be 30-50 min if given without interruptions. Interactive elements are encouraged. e.g. a Jupyter notebook demo. with tweakable parameters given by the audience.

## Ideas for presentations

 - Machine learning.
   - Back propogation.
   - Clustering.
   - ~~Boltzmann machine.~~
 - Control theory and signal processing.
   - Model reduction.
   - ~~Kalman filter.~~
   - ~~Hidden markov model.~~
   - ~~Proportional-integral (PI) controller.~~
 - Stochastic algorithms.
   - The Metropolis approach to sampling and alternatives
   - Global balance (pentalty method).
   - Quasi-random numbers.
   - Ant Colony Optimization
   - Parallel tempering.
   - Stochastic hill climbing.
   - Bayesian networks.
   - ~~Simulated annealing~~
   - ~~Evolutionary, and genetics algorithms.~~
   - ~~Particle Swarm Optimization~~
   - ~~Belief propogation~~
   - ~~Gibbs sampling~~
 - Encryption.
   - Symmetric-key, Public-key (RSA) cryptography
   - Cryptanalysis (breaking encryption).
   - Hashing.
 - Optimzation.
   - Global Newton methods
     - line search
     - trust region
     - iterative solution of linear equations
     - matrix free
   - Generalized minimal residual method (GMRES)
     - preconditioning
     - additive Schwarts
     - Algebraic and geometric multi-grid
     - Block Jacobi
   - Quadratic optimization.
   - Convex optmization.
   - Steepest descent, Conjugate gradiant, Quasi-Newton, ....
   - Noisy optimization.
   - Compilers (fortan).
   - ~~Simplex method.~~
 - Linear Algebra.
   - Random matrix theory.
   - ~~QR / SVD. principle component analysis~~
   - ~~Diagnolization~~, inversion.
   - ~~Lanczos~~
   - ~~Fast Fourier transforms (FFT).~~
 - Numerical solutions to differential equations.
   - Finite differences
   - ~~Finite elements~~
   - Finite volumes
   - Spectral elements
   - PDE solvers (additional problems from multivariate)
   - Energy conserving or time-reversal invariant versions.
   - ~~Runge-Kutta and family.~~
 - Data compression.
   - Image compression techniques (one or more).
   - Compressed sensing (probabilistic approach and connections to stat mech).
   - ~~Compressed sensing (l-1 technique).~~
 - Image Processing
   - Image recognition
   - ~~Automatic focus~~
 - Visualization
   - ~~Marching Cubes~~
 - Quantum computing.
   - Quantum annealing.
   - Quantum error correction.
   - Quantum encryption.
   - Quantum stabilizers.
   - ~~Grover algorithm.~~
   - ~~Shor algorithm.~~
 - Parallelism.
   - Parallel linear algebra.
   - OpenMP and MPI
   - GPU, Cuda, ...
 - Computer networks/the internet.
   - ~~Google search bar, page rank.~~
   - The Internet protocal suite.
   - Packet switching vs. cell-based switching.
   - Mobile networks.
   - Error detection and correction, Hamming codes.
   - Internet security.
   - Network routing.
 - Classic CS algorithms
   - Quicksort, Graph theory, ...
   - ~~Cellular atomata~~.
   - ~~Theory of computation~~ (Turing, finite state machine, definition of language, regular expressions).
   - ~~complexity theory.~~

[1]: {{ site.url }}/pages/2016roadmap.md
[2]: {{ site.url }}/pages/2017sp_roadmap.md
[3]: {{ site.url }}/pages/2017fa_roadmap.md
[4]: {{ site.url }}/pages/2018sp_roadmap.md
[5]: {{ site.url }}/pages/2019sp_roadmap.md
[6]: {{ site.url }}/pages/2019fa_roadmap.md
[repo]: https://github.com/Paul-St-Young/algorithms
