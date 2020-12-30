from ase.calculators.kim import KIM
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import GPa
from ase.io import read
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.langevin import Langevin
from ase.md.nptberendsen import NPTBerendsen
from ase.io.trajectory import Trajectory
from ase import units

for f in ['Li2SbZn-1.cif',  'Li2SbZn-2.cif',  'LiSbZn-1.cif',  'LiSbZn-2.cif']:
    v_lst = []
    for T in range(300, 1300, 100):
        v_T = []
        print('-' * 100)
        print(f, T)
        # Set up crystal and calculator
        atoms = read('Li-Sb-Zn/' + f)
        atoms *= (2, 2, 2)
        # calc = KIM("EAM_Dynamo_ErcolessiAdams_1994_Al__MO_123629422045_005")
        calc = KIM("LJ_ElliottAkerson_2015_Universal__MO_959249795837_003")
        atoms.set_calculator(calc)
        
        # T = 1500  # Kelvin
        
        ###########################
        # Compute energy/pressure
        ##########################
        
        # ecoh = -atoms.get_potential_energy() / len(atoms)
        # stress = atoms.get_stress()
        # pressure_MPa = (-sum(stress[:3]) / 3.0) * 1e3 / GPa
        # 
        # print("Computed cohesive energy of {:.3f} eV/atom (experiment: 3.39 eV/atom)".format(ecoh))
        # print("Computed pressure of {} MPa".format(pressure_MPa))
        
        ###########################################################
        # We want to run MD with constant energy using the Langevin algorithm
        # with a time step of 5 fs, the temperature T and the friction
        # coefficient to 0.02 atomic units.
        ##########################################################
        
        # dyn = Langevin(atoms, 5 * units.fs, T * units.kB, 0.002)
        
        ############################################################################
        # Room temperature simulation (300K, 0.1 fs time step, atmospheric pressure)
        ############################################################################
        
        dyn = NPTBerendsen(atoms, timestep=0.1 * units.fs, temperature=T,
                taut=0.1 * 1000 * units.fs, pressure=1.01325,
                taup=1.0 * 1000 * units.fs, compressibility=4.57e-5)
        
        def printenergy(a=atoms):  # store a reference to atoms in the definition.
            """Function to print the potential, kinetic and total energy."""
            epot = a.get_potential_energy() / len(a)
            ekin = a.get_kinetic_energy() / len(a)
            v = a.get_volume()
            v_T.append(v)
            print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
                'Etot = %.3feV volume = %.3f' % (epot, ekin, ekin / (1.5 * units.kB), epot + ekin, v))
                                
        dyn.attach(printenergy, interval=50)
        
        # We also want to save the positions of all atoms after every 100th time step.
        traj = Trajectory(f+str(T)+'.traj', 'w', atoms)
        dyn.attach(traj.write, interval=50)
        
        # Now run the dynamics
        printenergy()
        dyn.run(20000)
        v_lst.append(v_T[-2000:]/2000)
    print(f, v_lst)
