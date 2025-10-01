#!/usr/bin/env python3
"""
Nitinol Phase Comparison Visualization
Shows B2 austenite and B19' martensite structures side by side

All visualization parameters are locked in SHARED_PARAMS to ensure both
structures are always displayed consistently. To change how the structures
look, modify the values in SHARED_PARAMS at the top of the file.
"""

from ase import Atoms
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import CheckButtons
import numpy as np

# Shared visualization parameters - ensures both structures are always identical
SHARED_PARAMS = {
    'num_atoms': 32,           # Total atoms in each structure
    'repetitions_b2': (2, 2, 4),   # How to repeat B2 unit cell
    'repetitions_b19': (2, 2, 2),  # How to repeat B19' unit cell
    'initial_view': {
        'elev': 20,            # Initial elevation angle
        'azim': 45             # Initial azimuth angle
    },
    'bond_distance': 3.2,      # Maximum bond distance in Angstroms
    'atom_size': 300,          # Size of atom spheres
    'bond_width': 1.5,         # Width of bond lines
    'bond_alpha': 0.4          # Transparency of bonds
}

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

    # Use shared repetition parameters
    b2 = b2.repeat(SHARED_PARAMS['repetitions_b2'])

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

    # Use shared repetition parameters
    b19 = b19.repeat(SHARED_PARAMS['repetitions_b19'])

    return b19

def plot_structure(atoms, ax, title):
    """
    Plot atomic structure on given matplotlib axis with bonds
    """
    positions = atoms.get_positions()
    symbols = atoms.get_chemical_symbols()

    # Draw bonds first (so they appear behind atoms)
    # Use shared bond parameters
    max_bond_distance = SHARED_PARAMS['bond_distance']

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distance = np.linalg.norm(positions[i] - positions[j])

            # Only draw bonds between nearest neighbors
            if distance < max_bond_distance:
                # Draw bond as a line
                bond_points = np.array([positions[i], positions[j]])
                ax.plot3D(bond_points[:, 0], bond_points[:, 1], bond_points[:, 2],
                         'gray', linewidth=SHARED_PARAMS['bond_width'],
                         alpha=SHARED_PARAMS['bond_alpha'], zorder=1)

    # Separate Ti and Ni atoms
    ti_pos = positions[np.array(symbols) == 'Ti']
    ni_pos = positions[np.array(symbols) == 'Ni']

    # Plot atoms (with higher zorder so they appear on top of bonds)
    # Use shared atom size parameter
    if len(ti_pos) > 0:
        ax.scatter(ti_pos[:, 0], ti_pos[:, 1], ti_pos[:, 2],
                  c='silver', s=SHARED_PARAMS['atom_size'], alpha=0.9, edgecolors='black',
                  linewidths=1.5, label='Ti', zorder=3)

    if len(ni_pos) > 0:
        ax.scatter(ni_pos[:, 0], ni_pos[:, 1], ni_pos[:, 2],
                  c='gold', s=SHARED_PARAMS['atom_size'], alpha=0.9, edgecolors='black',
                  linewidths=1.5, label='Ni', zorder=3)

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
    """Create side-by-side comparison of B2 and B19' phases with interactive controls"""

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

    # Create figure with two subplots and space for controls
    fig = plt.figure(figsize=(17, 7))

    # B2 Austenite
    ax1 = fig.add_subplot(121, projection='3d')
    plot_structure(b2, ax1, 'B2 Austenite (High Temperature)\nCubic - "Memory" Phase')

    # B19' Martensite
    ax2 = fig.add_subplot(122, projection='3d')
    plot_structure(b19, ax2, "B19' Martensite (Low Temperature)\nMonoclinic - Deformable Phase")

    # Set both to the same initial viewing angle using shared parameters
    ax1.view_init(elev=SHARED_PARAMS['initial_view']['elev'],
                  azim=SHARED_PARAMS['initial_view']['azim'])
    ax2.view_init(elev=SHARED_PARAMS['initial_view']['elev'],
                  azim=SHARED_PARAMS['initial_view']['azim'])

    plt.suptitle('Nitinol Crystal Structure Comparison',
                fontsize=16, fontweight='bold', y=0.98)

    # Add interactive controls
    # Create checkbox area at the bottom
    ax_check = plt.axes([0.02, 0.02, 0.15, 0.15])
    check = CheckButtons(ax_check, ['Lock Rotation', 'Show Grid', 'Show Legends'],
                        [False, True, True])

    # Track checkbox states
    state = {
        'lock_rotation': False,
        'show_grid': True,
        'show_legends': True
    }

    def on_checkbox_clicked(label):
        """Handle checkbox clicks"""
        if label == 'Lock Rotation':
            state['lock_rotation'] = not state['lock_rotation']
            if state['lock_rotation']:
                # Sync the views
                ax2.view_init(elev=ax1.elev, azim=ax1.azim)
                fig.canvas.draw_idle()

        elif label == 'Show Grid':
            state['show_grid'] = not state['show_grid']
            # Toggle grid, axes, and panes
            for ax in [ax1, ax2]:
                ax.grid(state['show_grid'])
                ax.set_axis_on() if state['show_grid'] else ax.set_axis_off()
                # Toggle panes
                ax.xaxis.pane.set_visible(state['show_grid'])
                ax.yaxis.pane.set_visible(state['show_grid'])
                ax.zaxis.pane.set_visible(state['show_grid'])
            fig.canvas.draw_idle()

        elif label == 'Show Legends':
            state['show_legends'] = not state['show_legends']
            for ax in [ax1, ax2]:
                legend = ax.get_legend()
                if legend:
                    legend.set_visible(state['show_legends'])
            fig.canvas.draw_idle()

    check.on_clicked(on_checkbox_clicked)

    # Store the original motion_notify_event handler
    def on_move(event):
        """Synchronize rotation when locked"""
        if state['lock_rotation'] and event.inaxes in [ax1, ax2]:
            # Get the view angles from the active axis
            if event.inaxes == ax1:
                ax2.view_init(elev=ax1.elev, azim=ax1.azim)
            elif event.inaxes == ax2:
                ax1.view_init(elev=ax2.elev, azim=ax2.azim)
            fig.canvas.draw_idle()

    # Connect the motion event
    fig.canvas.mpl_connect('motion_notify_event', on_move)

    plt.tight_layout(rect=[0, 0.05, 1, 0.96])

    # Save figure
    output_file = 'nitinol_phase_comparison.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\nSaved comparison image to: {output_file}")

    # Show interactive plot
    print("Displaying interactive comparison...")
    print("\nControls:")
    print("  - Lock Rotation: Synchronize rotation of both structures")
    print("  - Show Grid: Toggle 3D grid and axes")
    print("  - Show Legends: Toggle atom type legends")
    plt.show()

if __name__ == "__main__":
    visualize_comparison()
