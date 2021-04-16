import numpy as np 
from numpy.linalg import eigh

# The probability of a Gaussian.
def px(x, mu, cov_inv, cov_det):
  N     = x.shape[0]
  d     = x.shape[1]
  coeff = 1.0/((2.0*np.pi)**(d/2.0) * cov_det**(0.5))

  result = np.zeros(N)
  for n in range(N):
    x_shifted = x[n,:] - mu
    result[n] = coeff * np.exp(-0.5 * x_shifted @ cov_inv @ x_shifted)

  return result

# Perform the Expectation-Maximization (EM) algorithm to
# find the maximum likelihood estimation of the parameters
# of a Gaussian-mixture model.
# Based on these lecture notes:
#  https://see.stanford.edu/materials/aimlcs229/cs229-notes8.pdf
#  https://www.ics.uci.edu/~smyth/courses/cs274/notes/EMnotes.pdf
# Also this video lecture is helpful:
#  https://www.youtube.com/watch?v=rVfZHWTwXSA
def em_gmm(data, num_gaussians, max_iter=100, rtol=1e-6, atol=1e-10, return_iterations=False):
  # The data matrix
  X = data

  # Number of samples
  N = data.shape[0]
  # Dimension of data
  d = data.shape[1]

  # The number of Gaussian in the Gaussian mixture model
  K    = num_gaussians
  # The probability of being in Gaussian l in {1,...,K} (initialized to uniform)
  phis = np.ones(K) / K
  # The mean vector of Gaussian l (initialized to first data points)
  mus = np.zeros((K, d))
  for k in range(K):
    mus[k,:] = X[k,:]
  # The covariance matrix of Gaussian l (initialized to data covariance)
  covs        = np.zeros((K, d, d))
  covs[0,:,:] = np.cov(X.T)
  for k in range(1,K):
    covs[k,:,:] = covs[0,:,:]

  if return_iterations:
    iteration_data = {
        "L"       : [],
        "mus"     : [],
        "covs"    : [],
        "phis"    : [],
        "weights" : []
      }

  
  log_likelihood_prev = np.inf
  weights             = np.zeros((N, K))
  for t in range(max_iter):
    for k in range(K):
      (evals, evecs) = eigh(covs[k,:,:])
      assert(np.all(evals > 1e-15))
      cov_det        = np.prod(evals)
      evals_inv      = np.array([(1.0/eval if np.abs(eval) > 1e-15 else 0.0) for eval in evals])
      cov_inv        = evecs @ np.diag(evals_inv) @ (evecs.conj().T)

      weights[:, k] = px(X, mus[k], cov_inv, cov_det) * phis[k]

    # Compute the log-likelihood.
    log_likelihood = np.sum(np.log(np.sum(weights, axis=1)))
    
    rel_change = np.abs(log_likelihood - log_likelihood_prev)/np.abs(log_likelihood)
    abs_change = np.abs(log_likelihood - log_likelihood_prev)

    print(f"=== Step {t+1} ===")
    print(f' L          = {log_likelihood}')
    print(f" rel_change = {rel_change}")
    print(f" abs_change = {abs_change}")

    if rel_change < rtol or abs_change < atol:
      break

    # Normalize the weights correctly.
    for n in range(N):
      weights[n, :] /= np.sum(weights[n, :]) 

    # Update the parameters.
    Nk   = np.sum(weights, axis=0)
    phis = Nk / N

    for i in range(d):
      mus[:, i] = (X[:,i] @ weights) / Nk
    
    for k in range(K):
      for i in range(d):
        x_shifted_i = X[:,i] - mus[k,i]
        for j in range(d):
          x_shifted_j   = X[:,j] - mus[k,j]
          covs[k, i, j] = ((x_shifted_i * x_shifted_j) @ weights[:,k]) / Nk[k]

    if return_iterations:
      iteration_data['L'].append(log_likelihood)
      iteration_data['mus'].append(np.copy(mus))
      iteration_data['covs'].append(np.copy(covs))
      iteration_data['phis'].append(np.copy(phis))
      iteration_data['weights'].append(np.copy(weights))

    log_likelihood_prev = log_likelihood

  if not return_iterations:
    return (log_likelihood, phis, mus, covs, weights)
  else:
    return (log_likelihood, phis, mus, covs, weights, iteration_data)
