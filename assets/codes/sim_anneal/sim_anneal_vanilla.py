import numpy as np
import random



class SimulatedAnneal:


    def __init__(self, func, x_init, tau_init = None, ran_range = None,
                time_const = None, iters = None, tau_iters = None ):

        self.func = func
        self.x_old = x_init
        self.x_new = 0
        self.tau_init = tau_init if tau_init is not None else 10
        self.ran_range = ran_range if ran_range is not None else 100
        self.time_const = time_const if time_const is not None else 10
        self.iters = iters if iters is not None else 10
        self.tau_iters = tau_iters if tau_iters is not None else 1000




    def _walker(self,tau):

        for step in range(0 , self.iters):
            self.x_new = random.uniform(0, self.ran_range)
            delta_f = self.func(self.x_new) - self.func(self.x_old)

            if delta_f <= 0:
                self.x_old = self.x_new
            else:
                acceptance_prob = min(1,np.exp(-delta_f/tau))
                if acceptance_prob > random.uniform(0,1):
                    self.x_old = self.x_new


    def simulate_anneal(self):

        tau_schedule = [self.tau_init * np.exp(-t/self.time_const) for t \
                        in range(0,self.tau_iters)]

        for tau in tau_schedule:
            self._walker(tau)
