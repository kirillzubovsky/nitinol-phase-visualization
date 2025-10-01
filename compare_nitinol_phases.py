#!/usr/bin/env python3
"""
Nitinol Phase Comparison Visualization
Shows B2 austenite and B19' martensite structures side by side
"""

from ase import Atoms
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_b2_austenite():
    """
    Create B2 austenite phase unit cell
    CsCl-type body-centered cubic structure
    """
    a = 3.015  # Lattice parameter in Angstrom

    cell = [[a, 0, 0],
            [0, a, 0],
            [0, 0, a]]

    positions = [[0, 0, 0],           # Ti at corner
                 [a/2, a/2, a/2]]     # Ni at body center

    symbols = ['Ti', 'Ni']

    b2 = Atoms(symbols=symbols,
               positions=positions,
               cell=cell,
               pbc=True)

    # Repeat to show crystal structure better
    b2 = b2.repeat((2, 2, 2))

    return b2

def create_b19_martensite():
    """
    Create B19' martensite phase unit cell
    Monoclinic structure (approximate)

    B19' has monoclinic symmetry with:
    a ≈ 2.89 Å, b ≈ 4.12 Å, c ≈ 4.62 Å, β ≈ 96.8°
    """
    a = 2.89
    b = 4.12
    c = 4.62
    beta = 96.8 * np.pi / 180  # Convert to radians

    # Monoclinic cell
    cell = [[a, 0, 0],
            [0, b, 0],
            [c * np.cos(beta), 0, c * np.sin(beta)]]

    # Approximate atomic positions for B19' (simplified)
    # In reality, B19' has 4 atoms per unit cell with complex positions
    positions = [
        [0.0, 0.0, 0.0],           # Ti
        [a/2, b/2, c/2],           # Ni
        [a/2, 0.0, c/2],           # Ti
        [0.0, b/2, 0.0]            # Ni
    ]

    symbols = ['Ti', 'Ni', 'Ti', 'Ni']

    b19 = Atoms(symbols=symbols,
                positions=positions,
                cell=cell,
                pbc=True)

    # Repeat to show structure
    b19 = b19.repeat((2, 2, 2))

    return b19

def plot_structure(atoms, ax, title):
    """
    Plot atomic structure on given matplotlib axis
    """
    positions = atoms.get_positions()
    symbols = atoms.get_chemical_symbols()

    # Separate Ti and Ni atoms
    ti_pos = positions[np.array(symbols) == 'Ti']
    ni_pos = positions[np.array(symbols) == 'Ni']

    # Plot atoms
    if len(ti_pos) > 0:
        ax.scatter(ti_pos[:, 0], ti_pos[:, 1], ti_pos[:, 2],
                  c='silver', s=300, alpha=0.8, edgecolors='black',
                  linewidths=1, label='Ti')

    if len(ni_pos) > 0:
        ax.scatter(ni_pos[:, 0], ni_pos[:, 1], ni_pos[:, 2],
                  c='gold', s=300, alpha=0.8, edgecolors='black',
                  linewidths=1, label='Ni')

    # Draw unit cell
    cell = atoms.get_cell()

    # Define edges of the cell
    origin = [0, 0, 0]
    edges = [
        [origin, cell[0]],
        [origin, cell[1]],
        [origin, cell[2]],
        [cell[0], cell[0] + cell[1]],
        [cell[0], cell[0] + cell[2]],
        [cell[1], cell[1] + cell[0]],
        [cell[1], cell[1] + cell[2]],
        [cell[2], cell[2] + cell[0]],
        [cell[2], cell[2] + cell[1]],
        [cell[0] + cell[1], cell[0] + cell[1] + cell[2]],
        [cell[0] + cell[2], cell[0] + cell[2] + cell[1]],
        [cell[1] + cell[2], cell[1] + cell[2] + cell[0]]
    ]

    for edge in edges:
        points = np.array(edge)
        ax.plot3D(points[:, 0], points[:, 1], points[:, 2],
                 'b-', linewidth=1, alpha=0.3)

    ax.set_xlabel('X (Å)', fontsize=10)
    ax.set_ylabel('Y (Å)', fontsize=10)
    ax.set_zlabel('Z (Å)', fontsize=10)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=10)

    # Set equal aspect ratio
    max_range = np.array([positions[:, 0].max() - positions[:, 0].min(),
                         positions[:, 1].max() - positions[:, 1].min(),
                         positions[:, 2].max() - positions[:, 2].min()]).max() / 2.0

    mid_x = (positions[:, 0].max() + positions[:, 0].min()) * 0.5
    mid_y = (positions[:, 1].max() + positions[:, 1].min()) * 0.5
    mid_z = (positions[:, 2].max() + positions[:, 2].min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.view_init(elev=20, azim=45)

def visualize_comparison():
    """Create side-by-side comparison of B2 and B19' phases"""

    print("Creating B2 austenite structure...")
    b2 = create_b2_austenite()
    print(f"  B2 phase: {len(b2)} atoms")
    print(f"  Cell parameters: a=b=c={b2.cell.cellpar()[0]:.3f} Å (cubic)")

    print("\nCreating B19' martensite structure...")
    b19 = create_b19_martensite()
    print(f"  B19' phase: {len(b19)} atoms")
    cell_params = b19.cell.cellpar()
    print(f"  Cell parameters: a={cell_params[0]:.3f} Å, b={cell_params[1]:.3f} Å, c={cell_params[2]:.3f} Å")
    print(f"  Monoclinic angle β={cell_params[4]:.1f}°")

    # Create figure with two subplots
    fig = plt.figure(figsize=(16, 7))

    # B2 Austenite
    ax1 = fig.add_subplot(121, projection='3d')
    plot_structure(b2, ax1, 'B2 Austenite (High Temperature)\nCubic - "Memory" Phase')

    # B19' Martensite
    ax2 = fig.add_subplot(122, projection='3d')
    plot_structure(b19, ax2, "B19' Martensite (Low Temperature)\nMonoclinic - Deformable Phase")

    plt.suptitle('Nitinol Crystal Structure Comparison',
                fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout()

    # Save figure
    output_file = 'nitinol_phase_comparison.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\nSaved comparison image to: {output_file}")

    # Show interactive plot
    print("Displaying interactive comparison...")
    plt.show()

if __name__ == "__main__":
    visualize_comparison()
