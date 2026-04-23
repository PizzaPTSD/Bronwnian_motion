import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(n_steps=1000, dt=0.01, diffusion=1.0):
    """
    Simulate 2D Brownian motion.
    
    n_steps:   number of time steps
    dt:        time step size 
    diffusion: diffusion coefficient
    """
    # Random increments: normal dist scaled by sqrt(2 * D * dt)
    # This directly implements Einstein's §4: ⟨Δ²⟩ = 2Dτ`
    # change to 3D by sqrt(6Dt) and adding dz
    scale = np.sqrt(2 * diffusion * dt)
    dx = np.random.normal(0, scale, n_steps)
    dy = np.random.normal(0, scale, n_steps)

    # sum up the increments (displacement) to produce coordinates
    x = np.cumsum(dx)
    y = np.cumsum(dy)

    return x, y

x, y = brownian_motion(n_steps=2000)

#plot the trajectory
plt.figure(figsize=(8, 8))
plt.plot(x, y, lw=0.5, alpha=0.7)
plt.scatter([x[0]], [y[0]], color='green', zorder=5, label='Start')
plt.scatter([x[-1]], [y[-1]], color='red', zorder=5, label='End')
plt.title("2D Brownian Motion")
plt.legend()
plt.axis('equal')
plt.show()

