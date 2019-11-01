#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def cs_comp(asamp, ysamp):
  # solve Ax=y for x
  import cvxpy as cvx
  nfull = asamp.shape[0]
  myx = cvx.Variable(nfull, complex=True)
  objective = cvx.Minimize(cvx.norm(myx, 1))
  constraints = [myx*asamp == ysamp]
  prob = cvx.Problem(objective, constraints)
  result = prob.solve()
  xarr = np.array(myx.value)
  if xarr is None:
    raise RuntimeError('cs failed')
  return xarr

if __name__ == '__main__':
  ndense = 512
  nfull = ndense # FFT basis
  nsamp = 10
  t = np.arange(ndense).astype(float)/ndense

  nwave = 40
  #nwave = 2
  w = nwave*2*np.pi
  def signal(t):
    return np.sin(w*t)
  y = signal(t)

  # take a sparse sample
  idx = np.arange(ndense)
  np.random.seed(1836)
  isamp = np.random.choice(idx, nsamp, replace=False)
  ysamp = y[isamp]

  # build FFT basis transformation matrix
  amat = []
  for irow in range(nfull):
    vec = np.zeros(nfull, dtype=complex)
    vec[irow] = 1
    row = np.fft.ifft(vec)
    amat.append(row)
  amat = np.array(amat)

  # solve compressive sensing problem
  asamp = amat[:, isamp]
  xarr = cs_comp(asamp, ysamp)
  yarr = np.dot(xarr, amat)
  dl2 = np.linalg.norm(yarr-y)

  ms = 10
  fig, ax = plt.subplots(1, 1)
  ax.set_xlabel('time')
  ax.set_ylabel('signal')
  ns_samps = 0.01+np.linspace(t.min(), t.max(), 2*nwave+1)
  nsx = ns_samps[:-1]
  nsy = signal(nsx)
  ax.plot(nsx, nsy, ls='', marker='x', c='r', ms=ms, label='Nyq.-Shan. %d samples' % (2*nwave))
  ax.plot(t[isamp], ysamp, ls='', marker='.', ms=ms, label='Comp. Sens. %d samples' % nsamp)
  ax.plot(t, yarr.real, label='CS dL2=%3.2f' % dl2)
  ax.plot(t, y, label='signal', ls='--')
  ax.legend(loc='center left')
  fig.savefig('nyquist-shannon.png', dpi=320)
  plt.show()
# end __main__
