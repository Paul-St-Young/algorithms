import os
import struct
import numpy as np
import matplotlib.pyplot as plt

"""
https://gist.github.com/akesling/5358964
Loosely inspired by http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
which is GPL licensed.
"""

def read(dataset = "training", path = "."):
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """

    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows, cols)

    get_img = lambda idx: (lbl[idx], img[idx])

    # Create an iterator which returns each image in turn
    for i in range(len(lbl)):
        yield get_img(i)

def show(image):
    """
    Render a given numpy.uint8 2D array of pixel data.
    """
    from matplotlib import pyplot
    import matplotlib as mpl
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
plt.show()



### Added by Will Wheeler ###
def plot_sample( n=10, ncol=5):
  nrow = np.ceil(n/ncol)*2
  i=1
  trainingdata = read(dataset='training')
  testingdata = read(dataset='testing')
  fig = plt.figure(figsize=(15, nrow*3))
  for g in trainingdata:
    ax = plt.subplot(nrow, ncol, i)
    ax.imshow(g[1])
    ax.set_title(str(g[0])+' training')
    i += 1
    if i>n:
      break
  for g in testingdata:
    ax = plt.subplot(nrow, ncol, i)
    ax.imshow(g[1])
    ax.set_title(str(g[0])+' testing')
    i += 1
    if i>2*n:
      break
  plt.tight_layout()
  plt.show()


if __name__ == '__main__':
  plot_sample(n=10)
