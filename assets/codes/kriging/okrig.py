#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def myfunc(x):
  """ true function to learn """
  return np.sin(x)
def generate_data(seed=1836, sig=.6):
  """ generate noisy samples from function """
  nsample = 128
  x = np.linspace(0, 3*np.pi, nsample)
  np.random.seed(seed)
  y = myfunc(x) + sig*np.random.randn(nsample)
  return x, y

def concat_return(func):
  def wrapper(xlist, *args, **kwargs):
    ylist = []
    for x in xlist:
      y = func(x, *args, **kwargs)
      ylist.append(y)
    return ylist
  return wrapper
@concat_return
def ordinary_krig(x0, x, y, myc, invc):
  """ ordinary kriging

  Args:
    x0 (float): prediction point
    x (np.array): sample points
    y (np.array): sample values
    myc (callable): correlation function (float, float) -> float
    invc (np.array): correlation matrix of samples
  Return:
    (float, float): (ym, ye) i.e. prediction (mean, error)
  """
  dvec = [myc(x0, x1) for x1 in x]
  # calculate Lagrange multiplier
  ovec = np.ones(len(dvec))
  nume = np.dot(np.dot(dvec, invc), ovec) - 1
  deno = np.dot(np.dot(ovec, invc), ovec)
  lam = nume/deno
  # calculate weights
  wvec = np.dot(invc, dvec-lam*ovec)
  if not np.isclose(wvec.sum(), 1):
    raise RuntimeError('weight constraint failed')
  ym = np.dot(wvec, y)
  sig2 = myc(x0, x0)-np.dot(dvec, wvec)-lam
  ye = np.sqrt(sig2)
  return ym, ye

def show_data(ax, x, y, finex, myfunc):
  ax.plot(x, y, c='k', ls='', marker='+', mew=2, label='noisy samples')
  ax.plot(finex, myfunc(finex), c='k', lw=2, ls='--', label='true function')
def show_krig(ax, finex, fineym, fineye):
  ax.plot(finex, fineym, label='kriging mean')
  ax.fill_between(finex, fineym-fineye, fineym+fineye,
    color='gray', label='kriging stddev')

if __name__ == '__main__':
  # define problem
  x, y = generate_data()                   # available data
  finex = np.linspace(min(x), max(x), 77)  # prediction locations
  # krige
  #  step 1: define correlation function
  length = 1.5
  period = 2*np.pi
  def expsin2(h, L, T):
    arg = np.pi/T*h
    sin2 = (np.sin(arg)/L)**2
    return np.exp(-2*sin2)
  def myc(x1, x2):
    return expsin2(abs(x1-x2), length, period)
  #  step 2: incorporate available data
  #   2.1 calculate correlation matrix
  cmat = np.array([[myc(x1, x2) for x1 in x] for x2 in x])
  #   2.2 add noise tolerance
  noise_level = .6
  cmat[np.diag_indices_from(cmat)] += noise_level
  #   2.3 invert correlation matrix
  invc = np.linalg.inv(cmat)
  #    check inversion
  identity = np.eye(len(x))
  if not np.allclose(np.dot(invc, cmat), identity):
    raise RuntimeError('matrix inversion failed')
  #  step 3: make predictions
  data = ordinary_krig(finex, x, y, myc, invc)
  fineym, fineye = np.array(data).T

  # show results
  fig, ax = plt.subplots(1, 1)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  show_data(ax, x, y, finex, myfunc)
  show_krig(ax, finex, fineym, fineye)
  ax.legend()
  fig.tight_layout()
  plt.show()
# end __main__
