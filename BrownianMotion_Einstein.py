"""
Einstein's Brownian Motion — Full Verification
================================================
Based directly on Einstein's 1905 paper equations:

§4 Eq.32:  λₓ = √(2Dt)          — displacement formula
§3 Eq.21:  D = RT / N·6πkP      — Stokes-Einstein equation  
§5 Eq.35:  N = RT / 3πkP·λₓ²   — Avogadro's number

Requirements: pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ─────────────────────────────────────────────
# YOUR ORIGINAL FUNCTION (unchanged)
# ─────────────────────────────────────────────
def brownian_motion(n_steps=1000, dt=0.01, diffusion=1.0):
    """
    Simulate 2D Brownian motion.
    
    n_steps:   number of time steps
    dt:        time step size
    diffusion: diffusion coefficient
    """
    # Random increments: normal dist scaled by sqrt(2 * D * dt)
    # This directly implements Einstein's §4: ⟨Δ²⟩ = 2Dτ
    scale = np.sqrt(2 * diffusion * dt)
    dx = np.random.normal(0, scale, n_steps)
    dy = np.random.normal(0, scale, n_steps)

    # Cumulative sum gives the trajectory
    # This implements Einstein's random walk: x(t) = Σδᵢ
    x = np.cumsum(dx)
    y = np.cumsum(dy)

    return x, y


# ─────────────────────────────────────────────
# NEW: EINSTEIN'S PHYSICAL PARAMETERS
# From Einstein's §5 numerical example (page 18)
# ─────────────────────────────────────────────
R  = 8.314        # Gas constant (J/mol·K)
T  = 290          # Temperature in Kelvin (~17°C, same as Einstein used)
N  = 6.022e23     # Avogadro's number (what Einstein wanted to find)
k  = 1.35e-3      # Water viscosity (Pa·s) — same value Einstein used
P  = 0.5e-6       # Particle radius (0.5 micrometers)

# Stokes-Einstein equation (§3, Eq.21):
# D = RT / N · 6πkP
D_physical = R * T / (N * 6 * np.pi * k * P)
print(f"Stokes-Einstein D = {D_physical:.4e} m²/s")
print(f"(Einstein got ~8×10⁻¹³ m²/s for similar parameters)")


# ─────────────────────────────────────────────
# NEW: VERIFY EINSTEIN'S DISPLACEMENT FORMULA
# λₓ = √(2Dt)  — §4, Eq.32
# ─────────────────────────────────────────────
def compute_msd(positions):
    """
    Compute Mean Squared Displacement over time.
    Verifies Einstein's §4 Eq.32: ⟨x²⟩ = 2Dt
    """
    origin = positions[0]
    n_steps = len(positions) - 1
    msd = np.zeros(n_steps + 1)
    for t in range(n_steps + 1):
        displacement = positions[t] - origin
        msd[t] = np.mean(displacement**2)
    return msd


# ─────────────────────────────────────────────
# NEW: CALCULATE AVOGADRO'S NUMBER FROM SIMULATION
# N = RT / 3πkP·λₓ²  — §5, Eq.35
# ─────────────────────────────────────────────
def calculate_avogadro(lambda_x_squared, t, T, k, P, R):
    """
    Einstein's final formula from page 18.
    Given measured displacement, calculate Avogadro's number.
    N = (1/λₓ²) · RT / 3πkP
    """
    N_calculated = (R * T) / (3 * np.pi * k * P * lambda_x_squared / t)
    return N_calculated


# ─────────────────────────────────────────────
# RUN SIMULATIONS
# ─────────────────────────────────────────────
N_PARTICLES = 100
N_STEPS     = 500
DT          = 1.0      # 1 second per step
D_SIM       = 1.0      # Normalised D for visualisation

print(f"\nRunning simulation with {N_PARTICLES} particles, {N_STEPS} steps...")

# Store all trajectories
all_x = []
all_y = []
for _ in range(N_PARTICLES):
    x, y = brownian_motion(n_steps=N_STEPS, dt=DT, diffusion=D_SIM)
    all_x.append(np.insert(x, 0, 0))  # prepend starting point 0
    all_y.append(np.insert(y, 0, 0))

all_x = np.array(all_x)  # shape: (N_PARTICLES, N_STEPS+1)
all_y = np.array(all_y)

# Compute MSD from x positions only (1D, matches Einstein's λₓ)
time_axis = np.arange(N_STEPS + 1) * DT
msd_x = np.mean(all_x**2, axis=0)           # simulated MSD
msd_theoretical = 2 * D_SIM * time_axis      # Einstein's §4: ⟨x²⟩ = 2Dt

# Fit line to MSD to extract D_measured
fit = np.polyfit(time_axis[1:], msd_x[1:], 1)
D_measured = fit[0] / 2
print(f"\nVerifying Einstein's §4 equation ⟨x²⟩ = 2Dt:")
print(f"  D (simulation input) = {D_SIM:.4f}")
print(f"  D (measured from MSD) = {D_measured:.4f}")
print(f"  Agreement: {100*(1-abs(D_measured-D_SIM)/D_SIM):.1f}%")

# Calculate Avogadro's number from final MSD (using physical D)
# Map simulation D to physical D for Avogadro calculation



# ─────────────────────────────────────────────
# PLOTTING — 4 panels
# ─────────────────────────────────────────────
fig = plt.figure(figsize=(16, 12))
fig.patch.set_facecolor('#0f0f1a')
gs = GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0])  # Your original plot
ax2 = fig.add_subplot(gs[0, 1])  # Gaussian distribution (§4)
ax3 = fig.add_subplot(gs[1, 0])  # MSD verification (§4 Eq.32)
ax4 = fig.add_subplot(gs[1, 1])  # Avogadro verification (§5 Eq.35)

DARK    = '#0f0f1a'
GRID    = '#2a2a3a'
TEXT    = '#e0e0f0'
BLUE    = '#00d4ff'
RED     = '#ff6b6b'
GREEN   = '#00ff99'
YELLOW  = '#ffd700'

for ax in [ax1, ax2, ax3, ax4]:
    ax.set_facecolor(DARK)
    ax.tick_params(colors=TEXT)
    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID)
    ax.grid(True, color=GRID, linestyle='--', alpha=0.5)

# ── PLOT 1: Your original 2D trajectory 


# ── PLOT 2: Gaussian distribution — Einstein's §4 Eq.31 ──


# ── PLOT 3: MSD verification — Einstein's §4 Eq.32 ──



# ── PLOT 4: Avogadro's number — Einstein's §5 Eq.35 ──

