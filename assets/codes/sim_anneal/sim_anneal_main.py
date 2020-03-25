import numpy as np
from sim_anneal_vanilla import SimulatedAnneal
import random
from scipy import optimize





func1 = lambda x: np.cos(14.5 * x - 0.3) + (x + 0.2) * x
func2 = lambda x: -np.sin(x)/x
func3 = lambda x: x**2 -np.cos(4*np.pi*x)

func = func2
x0=[1.]
minimizer_kwargs = {"method": "BFGS"}
ret = optimize.basinhopping(func, x0, minimizer_kwargs=minimizer_kwargs,niter=200)

x_init = random.uniform(-10,10)
tau_init = 1000
sim_anneal_obj = SimulatedAnneal( func, x_init, tau_init )
sim_anneal_obj.simulate_anneal()


print( "Simulated annealing global minimum: x = %.4f, f(x0) = %.4f" \
        % (sim_anneal_obj.x_old, func(sim_anneal_obj.x_old)))

print("scipy basin-hopping global minimum: x = %.4f, f(x0) = %.4f"\
        % (ret.x, ret.fun))
import numpy as np
import matplotlib.pyplot as plt

# Plot--------------------------------------------------------------------------
x = np.arange(-10, 10, 0.01)
 # Data for plotting
fig, ax = plt.subplots()
ax.plot(x, func(x))

ax.set(xlabel='x', ylabel='y',
       title='Objective function')



plt.show()
