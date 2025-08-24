import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 4.135667696e-15   # Planck constant (eV·s)
hbar = h / (2*np.pi)
c = 3e8               # speed of light (m/s)
me = 9.10938356e-31   # electron mass (kg)
e = 1.60217662e-19    # electron charge (C)
eps0 = 8.854187817e-12  # vacuum permittivity (F/m)

# Material parameters: CdSe as an example quantum dot
Eg_bulk = 1.74  # bulk bandgap (eV)
me_eff = 0.13 * me   # effective electron mass
mh_eff = 0.45 * me   # effective hole mass
eps_r = 9.5          # relative permittivity

def bandgap(R_nm):
    """Return bandgap energy for quantum dot of radius R_nm (nm)."""
    R = R_nm * 1e-9  # convert to meters
    
    # Quantum confinement term
    confinement = (hbar**2 * (np.pi**2)) / (2 * (R**2)) * (1/me_eff + 1/mh_eff) / e
    
    # Coulomb interaction term
    coulomb = 1.8 * e**2 / (4*np.pi*eps0*eps_r*R) / e
    
    return Eg_bulk + confinement - coulomb

# Radii range
radii = np.linspace(1, 10, 100)  # 1 nm to 10 nm
energies = [bandgap(r) for r in radii]

# Plotting
plt.figure(figsize=(8,5))
plt.plot(radii, energies, 'b-', linewidth=2)
plt.axhline(Eg_bulk, color='r', linestyle='--', label=f'Bulk Eg = {Eg_bulk} eV')
plt.title("Quantum Confinement Effect in CdSe Quantum Dots")
plt.xlabel("Quantum dot radius (nm)")
plt.ylabel("Bandgap Energy (eV)")
plt.legend()
plt.grid(True)
plt.show()
