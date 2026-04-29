# Overview
A Python simulation for Brownian motion trajectory prediction based on Einstein's 1905 paper on Brownian motion, this repo includes single-particle 2D trajectories, Gaussian distribution verification, Multi-particle + mean-squared displacement(MSD) verification, and Avogadro's number calculation.

## Mathematical formulae used
- Random walk: x = δx<sub>1</sub> + δx<sub>2</sub> + ... + δx<sub>n</sub>
- MSD prediction: <x<sup>2</sup>> = 2Dt ------------------ (Einstein §4 Eq.32)
- Stokes-Einstein: D = RT/(6πηrN) -------------- (Einstein §3 Eq.21)
- Avogadro's number: N = RT/(3πηr·λ<sub>x</sub><sup>2</sup>/t) ----- (Einstein §5 Eq.35)

## Libraries used: Numpy and matplotlib
If you wish to download and run this program, clone this instruction into the terminal.

```bash
pip install numpy matplotlib
```

## Planned extensions
- 3D simulation
- Stochastic differential equation methods (Euler-Maruyama)
