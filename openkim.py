"""
Compute the cohesive energy and pressure of an FCC Al crystal using the
Ercolessi-Adams EAM potential implemented as a Portable Model (PM) in
OpenKIM for the experimental lattice constant a0=4.05 Angstrom.
"""
from ase.calculators.kim import KIM
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import GPa

# Set up crystal and calculator
a0 = 4.05  # experimental lattice constant
atoms = FaceCenteredCubic("Al", latticeconstant=a0)
calc = KIM("EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005")
atoms.set_calculator(calc)

# Compute energy/pressure
ecoh = -atoms.get_potential_energy() / len(atoms)
stress = atoms.get_stress()
pressure_MPa = (-sum(stress[:3]) / 3.0) * 1e3 / GPa

print("Computed cohesive energy of {:.3f} eV/atom (experiment: 3.39 eV/atom)".format(ecoh))
print("Computed pressure of {} MPa".format(pressure_MPa))


"""Demonstrates molecular dynamics with constant temperature."""
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.langevin import Langevin
from ase.md.nptberendsen import NPTBerendsen
from ase.io.trajectory import Trajectory
from ase import units

use_asap = True

if use_asap:
    from asap3 import EMT
    size = 10
else:
    from ase.calculators.emt import EMT
    size = 3

# from asap3 import EMT  # Way too slow with ase.EMT !
# size = 10

T = 1500  # Kelvin

# Set up a crystal
# atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
#                                   symbol="Cu",
#                                                             size=(size, size, size),
#                                                                                       pbc=False)

# Describe the interatomic interactions with the Effective Medium Theory
# atoms.calc = EMT()

# We want to run MD with constant energy using the Langevin algorithm
# with a time step of 5 fs, the temperature T and the friction
# coefficient to 0.02 atomic units.
# dyn = Langevin(atoms, 5 * units.fs, T * units.kB, 0.002)

# # Room temperature simulation (300K, 0.1 fs time step, atmospheric pressure)
dyn = NPTBerendsen(atoms, timestep=0.1 * units.fs, temperature=T,
        taut=0.1 * 1000 * units.fs, pressure=1.01325,
        taup=1.0 * 1000 * units.fs, compressibility=4.57e-5)

def printenergy(a=atoms):  # store a reference to atoms in the definition.
    """Function to print the potential, kinetic and total energy."""
    epot = a.get_potential_energy() / len(a)
    ekin = a.get_kinetic_energy() / len(a)
    print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
        'Etot = %.3feV' % (epot, ekin, ekin / (1.5 * units.kB), epot + ekin))
                        
dyn.attach(printenergy, interval=50)

# We also want to save the positions of all atoms after every 100th time step.
traj = Trajectory('moldyn3.traj', 'w', atoms)
dyn.attach(traj.write, interval=50)

# Now run the dynamics
printenergy()
dyn.run(10000)
