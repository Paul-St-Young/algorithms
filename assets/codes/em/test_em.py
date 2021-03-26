import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import ArtistAnimation, FFMpegWriter, PillowWriter

from em import px, em_gmm

run_name = "test1"

seed = 1
np.random.seed(seed)

num_samples = 1000
# Uniform random numbers in [0,1]x[0,1] 
data        = np.zeros((num_samples, 2))
data[0:num_samples//2,0] = np.random.rand(num_samples//2)
data[0:num_samples//2,1] = np.random.rand(num_samples//2)
# and in [1,2]x[1,2]
data[num_samples//2:,0]  = 1.0 + np.random.rand(num_samples//2)
data[num_samples//2:,1]  = 1.0 + np.random.rand(num_samples//2)
np.random.shuffle(data)

K = 2

(logl, phis, mus, covs, weights, iteration_data) = em_gmm(data, K, return_iterations=True)

print(f"phis = {phis}")
print(f"mus  = {mus}")
print(f"covs = {covs}")

# Plot the cluster assignments
cmap             = plt.get_cmap("tab20")
colors_gaussians = [cmap(i/K) for i in range(K)]

# Assign each data point to the color of the Gaussian
# that it is most likely from.
data_colors = [colors_gaussians[np.argmax(weights[n,:])] for n in range(num_samples)]

plt.scatter(data[:,0], data[:,1], c=data_colors)
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Cluster assignments")

plt.tight_layout()
plt.savefig("em_test1_assignments.png", dpi=500)

# Plot the total probability density.
plt.figure()
x  = np.linspace(0,2,200)
dx = x[1] - x[0]
y  = np.linspace(0,2,200)
dy = y[1] - y[0]
Z  = np.zeros((len(y), len(x)))
for k in range(K):
  cov            = covs[k]
  (evals, evecs) = np.linalg.eigh(cov)
  cov_inv        = evecs @ (np.diag(1.0/evals)) @ evecs.conj().T
  cov_det        = np.prod(evals)
  for i in range(len(x)):
    for j in range(len(y)):
      Z[j,i] += px(np.array([[x[i], y[j]]]), mus[k], cov_inv, cov_det) * phis[k]

cmap   = plt.get_cmap("Spectral") #LinearSegmentedColormap("mymap", [(1.,1.,1.), data_colors[0]])
extent = (-dx/2, 2+dx/2, -dy/2, 2+dy/2)
plt.imshow(Z, extent=extent, origin="lower", cmap=cmap, aspect="auto", interpolation="none")
plt.colorbar()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Optimized $P(x;\\theta)$")

plt.tight_layout()
plt.savefig(f"em_{run_name}_density.png", dpi=500)

# Plot the cluster probability densities.
plt.figure()
x  = np.linspace(0,2,200)
dx = x[1] - x[0]
y  = np.linspace(0,2,200)
dy = y[1] - y[0]
Z = np.zeros((len(y), len(x), 4))
for k in range(K):
  cmap = LinearSegmentedColormap.from_list("mymap", [(1.,1.,1.,1.), data_colors[k]], N=100)

  cov            = covs[k]
  (evals, evecs) = np.linalg.eigh(cov)
  cov_inv        = evecs @ (np.diag(1.0/evals)) @ evecs.conj().T
  cov_det        = np.prod(evals)
  for i in range(len(x)):
    for j in range(len(y)):
      prob      = px(np.array([[x[i], y[j]]]), mus[k], cov_inv, cov_det)
      color     = cmap(prob)[0]
      Z[j,i,:] += np.array([color[0], color[1], color[2], 1.0]) * phis[k]
      Z[j,i,3]  = 1.0

  extent = (-dx/2, 2+dx/2, -dy/2, 2+dy/2)
  plt.imshow(Z, extent=extent, origin="lower", aspect="auto", interpolation="none")
  #plt.colorbar()
  plt.xlabel("$x$")
  plt.ylabel("$y$")
  plt.title("Optimized $P_k(x;\\theta)$")

plt.tight_layout()
plt.savefig(f"em_{run_name}_cluster_densities.png", dpi=500)

# Plot an animation of the probability density evolving.
fig = plt.figure()

total_time = 10 * 1000 # total time for the animation in milliseconds

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for t in range(len(iteration_data["L"])):
  phis = iteration_data["phis"][t]
  mus  = iteration_data["mus"][t]
  covs = iteration_data["covs"][t]

  x  = np.linspace(0,2,200)
  dx = x[1] - x[0]
  y  = np.linspace(0,2,200)
  dy = y[1] - y[0]
  Z  = np.zeros((len(y), len(x)))
  for k in range(K):
    cov            = covs[k]
    (evals, evecs) = np.linalg.eigh(cov)
    cov_inv        = evecs @ (np.diag(1.0/evals)) @ evecs.conj().T
    cov_det        = np.prod(evals)
    for i in range(len(x)):
      for j in range(len(y)):
        Z[j,i] += px(np.array([[x[i], y[j]]]), mus[k], cov_inv, cov_det) * phis[k]

  cmap   = plt.get_cmap("Spectral") #LinearSegmentedColormap("mymap", [(1.,1.,1.), data_colors[0]])
  extent = (-dx/2, 2+dx/2, -dy/2, 2+dy/2)
  im = plt.imshow(Z, extent=extent, origin="lower", cmap=cmap, aspect="auto", interpolation="none", vmin=0, vmax=1)
  if t == 0:
    plt.colorbar()
  plt.xlabel("$x$")
  plt.ylabel("$y$")
  plt.title("Optimized $P(x;\\theta)$")

  ims.append([im])

writer = PillowWriter(fps=len(ims)//(total_time//1000))
ani    = ArtistAnimation(fig, ims, interval=total_time//len(ims), blit=True, repeat_delay=1000)

ani.save(f"em_{run_name}_animation.gif", writer=writer)

# Plot an animation of the probability densities of the clusters evolving.
fig = plt.figure()

total_time = 10 * 1000 # total time for the animation in milliseconds

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for t in range(len(iteration_data["L"])):
  phis = iteration_data["phis"][t]
  mus  = iteration_data["mus"][t]
  covs = iteration_data["covs"][t]

  x  = np.linspace(0,2,200)
  dx = x[1] - x[0]
  y  = np.linspace(0,2,200)
  dy = y[1] - y[0]
  Z = np.zeros((len(y), len(x), 4))
  for k in range(K):
    cmap = LinearSegmentedColormap.from_list("mymap", [(1.,1.,1.,1.), data_colors[k]], N=100)

    cov            = covs[k]
    (evals, evecs) = np.linalg.eigh(cov)
    cov_inv        = evecs @ (np.diag(1.0/evals)) @ evecs.conj().T
    cov_det        = np.prod(evals)
    for i in range(len(x)):
      for j in range(len(y)):
        prob      = px(np.array([[x[i], y[j]]]), mus[k], cov_inv, cov_det)
        color     = cmap(prob)[0]
        Z[j,i,:] += np.array([color[0], color[1], color[2], 1.0]) * phis[k]
        Z[j,i,3]  = 1.0
    
    extent = (-dx/2, 2+dx/2, -dy/2, 2+dy/2)
    im = plt.imshow(Z, extent=extent, origin="lower", aspect="auto", interpolation="none")
    #plt.colorbar()
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Optimized $P_k(x;\\theta)$")

  ims.append([im])

writer = PillowWriter(fps=len(ims)//(total_time//1000))
ani    = ArtistAnimation(fig, ims, interval=total_time//len(ims), blit=True, repeat_delay=1000)

ani.save(f"em_{run_name}_cluster_densities_animation.gif", writer=writer)

# Plot the log-likelihood bound vs iteration.
plt.figure()

Ls = iteration_data["L"]
plt.plot(np.arange(1,len(Ls)), Ls[1:], "ko-")
plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Lower bound on log-likelihood")

plt.tight_layout()
plt.savefig(f"em_{run_name}_loglikelihood.png", dpi=500)

plt.show()