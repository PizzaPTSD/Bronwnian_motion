Overview

A python simulation for Brownian motion trajectory prediction based on Einstein's 1905 paper on Brownian motion, this repo includes single particle 2D trajectory, Gaussian distribution verification, Multi-particle + mean-sqaured displacement(MSD) verification and Avogadro's number calculation.

Mathematics formulae used
- Random walk: x = δx_1 + δx_2 + ... + δx_n
- MSD prediction: <x^2> = 2Dt ----------------- (Einstein §4 Eq.32)
- Stokes-Einstein: D = RT/(6πηrN) ------------ (Einstein §3 Eq.21)
- Avogadro's number: N = RT/(3πηr·λₓ^2/t) ----- (Einstein §5 Eq.35)

Libraries used: Numpy and matplotlib
If you wish to download and run this program, copy and paste this intruction into terminal.
pip install numpy matplotlib

Planned extensions
- 3D simulation
- Stochastic differential equation methods (Euler-Maruyama)
