# Author: Yubo "Paul" Yang
# Email: yubo.paul.yang@gmail.com
# Routines to parse hdf5 walker data output. Mostly built around PyTables.
import os
import tables
import numpy as np

def open_read(fname):
  fp = tables.open_file(fname, mode='r')
  return fp

def open_write(fname):
  filters = tables.Filters(complevel=5, complib='zlib')
  fp = tables.open_file(fname, mode='w', filters=filters)
  return fp

def save_vec(vec, h5file, slab, name):
  """ save numpy array into an h5 slab under name

  Args:
    vec (np.array): numpy ndarray of arbitrary dimension and type
    h5file (tables.file.File): pytables File
    slab (tables.Group): HDF5 slab
    name (str): name of CArray to create
  """
  atom = tables.Atom.from_dtype(vec.dtype)
  ca = h5file.create_carray(slab, name, atom, vec.shape)
  ca[:] = vec

def saveh5(fname, mat, name='data'):
  """ save matrix at root of h5 file, mimic call signature of np.savetxt

  e.g. mat = np.eye(3)
  saveh5('mat.h5', mat)
  $ h5ls mat.h5
  data               Dataset {3/2730, 3}

  Args:
    fname (str): name of hdf5 file to write
    mat (np.array): 2D numpy array of floats
    name (str, optional): CArray name at the root of the hdf5 file
  """
  fp = open_write(fname)
  save_vec(mat, fp, fp.root, name)
  fp.close()

def loadh5(fname, path='/data'):
  """ load matrix from h5 file, mimic np.loadtxt

  Args:
    fname (str): name of hdf5 to read
  Return:
    np.array: matrix of data
  """
  fp = open_read(fname)
  slab = fp.get_node(path)
  mat = slab.read()
  fp.close()
  return mat
