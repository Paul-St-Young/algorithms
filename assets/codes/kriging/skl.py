#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

from okrig import myfunc, generate_data, show_data, show_krig
from sklearn.gaussian_process.kernels import ExpSineSquared, WhiteKernel
from sklearn.gaussian_process.gpr import GaussianProcessRegressor

if __name__ == '__main__':
  # initial parameters
  #  sklearn will adjust these parameters based on data
  #  see gpr.kernel_
  length = 1.5
  period = 2*np.pi
  noise_level = .6
  # define problem
  x, y = generate_data()                   # available data
  finex = np.linspace(min(x), max(x), 77)  # prediction locations
  # krige
  #  step 1: define correlation function
  kernel = ExpSineSquared(length_scale=length, periodicity=period) +\
           WhiteKernel(noise_level)
  #  step 2: incorporate available data
  gpr = GaussianProcessRegressor(kernel=kernel)
  gpr.fit(x[:, None], y)
  print(gpr.kernel_)
  #  step 3: make predictions
  fineym, fineye = gpr.predict(finex[:, None], return_std=True)

  # show results
  fig, ax = plt.subplots(1, 1)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  show_data(ax, x, y, finex, myfunc)
  show_krig(ax, finex, fineym, fineye)
  ax.legend()
  plt.show()
# end __main__
