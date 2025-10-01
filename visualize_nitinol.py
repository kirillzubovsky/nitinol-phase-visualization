#!/usr/bin/env python3
"""
Nitinol (NiTi) Wire Visualization
Creates and visualizes a B2 austenite phase nitinol structure
"""

from ase import Atoms
from ase.build import bulk
from ase.visualize import view
import numpy as np

def create_nitinol_wire(length=20, diameter=10):
    """
    Create a nitinol wire structure in B2 (austenite) phase

    Parameters:
    -----------
    length : int
        Length of the wire in angstroms (along z-axis)
    diameter : int
        Approximate diameter of the wire in angstroms

    Returns:
    --------
    atoms : ase.Atoms
        The nitinol wire structure
    """

    # Create B2 CsCl structure (austenite phase of NiTi)
    # Lattice parameter for NiTi B2 phase is approximately 3.015 Angstrom
    a = 3.015

    # Create base unit cell - B2 structure
    # Ti at corners (0,0,0), Ni at body center (0.5,0.5,0.5)
    cell = [[a, 0, 0],
            [0, a, 0],
            [0, 0, a]]

    positions = [[0, 0, 0],           # Ti
                 [a/2, a/2, a/2]]     # Ni

    symbols = ['Ti', 'Ni']

    nitinol = Atoms(symbols=symbols,
                    positions=positions,
                    cell=cell,
                    pbc=True)

    # Replicate to create wire shape
    nx = int(diameter / a)
    ny = int(diameter / a)
    nz = int(length / a)

    wire = nitinol.repeat((nx, ny, nz))

    # Create cylindrical wire shape by removing atoms outside radius
    center_x = wire.cell[0][0] / 2
    center_y = wire.cell[1][1] / 2
    radius = diameter / 2

    positions = wire.get_positions()
    distances = np.sqrt((positions[:, 0] - center_x)**2 +
                       (positions[:, 1] - center_y)**2)

    # Keep only atoms within cylindrical radius
    mask = distances <= radius
    wire = wire[mask]

    return wire

def visualize_nitinol():
    """Create and visualize nitinol wire"""

    print("Creating nitinol wire structure...")
    wire = create_nitinol_wire(length=30, diameter=15)

    print(f"Wire created with {len(wire)} atoms")
    print(f"  Ti atoms: {sum(1 for atom in wire if atom.symbol == 'Ti')}")
    print(f"  Ni atoms: {sum(1 for atom in wire if atom.symbol == 'Ni')}")
    print(f"\nWire dimensions:")
    print(f"  Cell: {wire.cell.cellpar()[:3]} Angstrom")

    # Visualize
    print("\nLaunching ASE viewer...")
    view(wire)

if __name__ == "__main__":
    visualize_nitinol()
