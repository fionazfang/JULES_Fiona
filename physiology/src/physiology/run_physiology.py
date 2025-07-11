
from simulation import run_simulation, generate_forcings
from config     import SIM_SETTINGS
from equations  import compensation_point
import visualization as viz

if __name__ == '__main__':
    pft = 'needleleaf_tree'
    t, results = run_simulation(pft)
    from simulation import generate_forcings
    t, T, I_par, ci, O2 = generate_forcings(SIM_SETTINGS)
    ca = SIM_SETTINGS['ca_ppm'] * 1e-6 * SIM_SETTINGS['P']

    viz.plot_forcings(t, T, I_par, ci, ca)
    viz.plot_limiters(t, results)
    viz.plot_fluxes(t, results)

    import matplotlib.pyplot as plt
    plt.show()