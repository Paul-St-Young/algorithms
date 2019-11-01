#!/usr/bin/env python
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

import pywt
from cs_simple import cs
from phantom import phantom
from config_h5 import saveh5, loadh5

def flatten_coeffs(coeffs):
  """ flatten pywt coefficients to a vector
  Args:
    tuple: pywt coeffs returned by wavedec2
  Return:
    np.array: 1D vector xvec
  """
  x0 = []
  for c in coeffs:
    x0.append(np.array(c).ravel())
  xvec = np.concatenate(x0)
  return xvec

def build_coeffs(xvec):
  """ build pywt coefficients to from a vector
   this is the inverse of flatten_coeffs

  Args:
    xvec (np.array): 1D vector
  Return:
    tuple: coeffs useful for pywt.waverec2
  """
  nc = int(np.log2(len(xvec)))/2
  coeffs = [xvec[0].reshape(1, 1)]
  for i in range(nc):
    c1 = xvec[4**i:2*4**i].reshape(2**i, 2**i)
    c2 = xvec[2*4**i:3*4**i].reshape(2**i, 2**i)
    c3 = xvec[3*4**i:4*4**i].reshape(2**i, 2**i)
    coeffs.append((c1, c2, c3))
  return coeffs

if __name__ == '__main__':
  nx = 64
  p = phantom(n=nx)
  frac = float(np.count_nonzero(p.ravel()))/nx**2
  msg1 = 'phantom density %3.2f' % frac
  print(msg1)

  # deconstruct into wavelets
  coeffs = pywt.wavedec2(p, 'haar')
  # flatten coefficients
  xvec = flatten_coeffs(coeffs)
  frac = float(np.count_nonzero(xvec))/len(xvec)
  msg2 = 'wavelet density %3.2f' % frac
  print(msg2)

  ## check raveled coefficients
  #coeffs1 = build_coeffs(xvec)
  ## reconstruct wavelets
  #p1 = pywt.waverec2(coeffs1, 'haar')
  #assert np.allclose(p, p1)

  # make transformation matrix
  fmat = 'A-phantom-n%d.h5' % nx
  nfull = nx**2
  if not os.path.isfile(fmat):
    msg = 'constructing the A matrix'
    print(msg)
    amat = []
    for irow in range(nfull):
      vec = np.zeros(nfull)
      vec[irow] = 1
      myc = build_coeffs(vec)
      row = pywt.waverec2(myc, 'haar')
      amat.append(row.ravel())
    amat = np.array(amat)
    msg = 'saving the A matrix'
    print(msg)
    saveh5(fmat, amat)
  else:
    msg = 'loading the A matrix'
    print(msg)
    amat = loadh5(fmat)

  # sample signal in dense space
  nsamp = 3000
  nsamp = 1200
  frac1 = float(nsamp)/nfull
  msg = 'sample %d/%d pixels %3.2f' % (nsamp, nfull, frac1)
  print(msg)
  idx = np.arange(nfull)
  isamp = np.random.choice(idx, nsamp, replace=False) 
  ysamp = p.ravel()[isamp]
  asamp = amat[:, isamp]

  msg = 'miminizing L1'
  print(msg)
  xarr = cs(asamp, ysamp)
  yarr = np.dot(xarr, amat)
  p1 = np.absolute(yarr.reshape(nx, nx))
  dl1 = np.absolute(p1-p).sum()

  fig = plt.figure()
  ax = fig.add_subplot(131, aspect=1)
  ax.set_title('original')
  ax.imshow(p, cmap='gray')
  ax = fig.add_subplot(132, aspect=1)
  ax.set_title('sampled %3.2f' % frac1)
  ps = np.zeros(p.shape)
  ps.ravel()[isamp] = p.ravel()[isamp]
  ax.imshow(ps, cmap='gray')
  ax = fig.add_subplot(133, aspect=1)
  ax.set_title('rec. dL1=%3.2f' % dl1)
  ax.imshow(np.absolute(p1), cmap='gray')
  fig.savefig('cs-phantom-nx%d-ns%d.png' % (nx, nsamp), dpi=320)
  plt.show()
# end __main__
