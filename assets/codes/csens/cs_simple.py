#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def cs(asamp, ysamp):
  nfull = asamp.shape[0]
  # solve Ax=y for x
  import cvxpy as cvx
  myx = cvx.Variable(nfull)
  objective = cvx.Minimize(cvx.norm(myx, 1))
  constraints = [myx*asamp == ysamp]
  prob = cvx.Problem(objective, constraints)
  result = prob.solve(verbose=False)
  xarr = np.array(myx.value)
  return xarr

if __name__ == '__main__':
  nfull = 128
  # parse signal
  x = np.zeros(nfull)
  x[1] = 1
  x[42] = 10
  x[101] = .5
  # signal in dense space
  np.random.seed(1836)
  amat = np.random.randn(nfull, nfull)
  y = np.dot(x, amat)
  # sample signal in dense space
  nsamp = 22
  idx = np.arange(nfull)
  isamp = np.random.choice(idx, nsamp, replace=False) 
  ysamp = y[isamp]
  asamp = amat[:, isamp]

  xarr = cs(asamp, ysamp)
  xl2 = np.linalg.lstsq(asamp.T, ysamp)[0]
  ## solution in sparse space
  #fig, ax = plt.subplots(1, 1)
  #ax.plot(idx, x, '.')
  #ax.plot(idx, xarr, '+', c='r')
  #ax.plot(idx, xl2, 'x')
  #plt.show()
  #assert 0

  # solution in dense space
  yarr = np.dot(xarr, amat)
  yl2 = np.dot(xl2, amat)
  fig, ax = plt.subplots(1, 1)
  ax.plot(idx, y, c='k', alpha=0.2, ls='', marker='.', ms=20, label='signal')
  ax.plot(isamp, ysamp, ls='', marker='.', c='k', ms=20, label='samp.')
  ax.plot(idx, yarr, '+', c='r', ms=10, mew=2, label='cs')
  ax.plot(idx, yl2, 'x', ms=15, mew=2, label='lstsq')
  ax.legend(loc='upper center')
  fig.savefig('cs-thumb.png', dpi=240)
  plt.show()
# end __main__
