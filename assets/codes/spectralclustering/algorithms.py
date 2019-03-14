import numpy as np
import numpy.linalg as nla


def kmeans(data, k, num_iterations, num_inits=10, verbose=False):
    """Execute the k-means algorithm for
    determining the best k clusters of data
    points in a dataset.
    
    Parameters
    ----------
    data : ndarray, (n,d)
        n data points in R^d.
    k : int
        The number of clusters to separate
        the data into.
    num_iterations : int
        The number of iterations of the k-means
        algorithm to execute.
    num_inits : int, optional
        Number of random initializations to try.
        Returns the best result.
    verbose : bool, optional
        Specifies whether to print info about
        the execution of the algorithm.
    
        
    Return
    ------
    (clusters, data_point_assigment, centroids)
        The results of the k-means algorithm. Clusters
        is a list of the clusters (which are lists of ints).
        data_point_assigment is a (n,) numpy array of ints 
        that indicates which cluster a data point has been
        assigned to. And centroids is (k,d) numpy array
        specifying the cluster centers.
    """
    
    # Number of data points
    num_data_points = int(data.shape[0])
    
    # Spatial dimension d
    d = int(data.shape[1])
    
    best_results = None
    best_total_distance = np.inf
    
    for init in range(num_inits):
        # Map from data point index to cluster index.
        data_point_assignment = np.zeros(num_data_points, dtype=int)
        # list of data points in clusters
        clusters = [[]] * k

        # Initialize the centroids 
        # using k-randomly sampled points.
        centroids = np.zeros((d,k))
        for ind_cluster in range(k):
            inds_data = np.random.choice(num_data_points, k)
            centroid  = np.mean(data[inds_data, :], axis=0)

            centroids[:, ind_cluster] = centroid

        for iteration in range(num_iterations):
            if verbose:
                print('==== Iteration {}/{} ===='.format(iteration+1, num_iterations))
                print('centroids = {}'.format(centroids))

            clusters = []
            for ind_c in range(k):
                clusters.append([])

            # Assignment step:
            # Assign each data point to the 
            # cluster with nearest centroid.
            total_distance = 0.0
            for ind_point in range(num_data_points):
                distances   = np.array([nla.norm(data[ind_point, :] - centroids[:, ind_c]) for ind_c in range(k)])
                ind_cluster = np.argmin(distances)
                
                total_distance += distances[ind_cluster]

                data_point_assignment[ind_point] = ind_cluster
                clusters[ind_cluster].append(ind_point)

            # Update step:
            # Update the centroids of the
            # new clusters.
            for ind_cluster in range(k):
                cluster      = clusters[ind_cluster]
                cluster_data = np.array([data[ind_point, :] for ind_point in cluster])
                centroid     = np.mean(cluster_data, axis=0)

                centroids[:, ind_cluster] = centroid
                
            if total_distance < best_total_distance:
                best_total_distance = total_distance
                best_results = (clusters, data_point_assignment, centroids)
           
    return best_results

def spectral_clustering(data, k, num_iterations, kernel_fun, L_type='unnormalized', num_inits=10, verbose=False):
    """Execute the spectral clustering algorithm for
    determining the best k clusters of data
    points in a dataset.
    
    Parameters
    ----------
    data : ndarray, (n,d)
        n data points in R^d.
    k : int
        The number of clusters to separate
        the data into.
    num_iterations : int
        The number of iterations of the k-means
        algorithm to execute.
    kernel_fun : function(ndarray, ndarray)
        A kernel function that computes a similarity
        between two numpy arrays.
    L_type : str, optional
        The type of graph Laplacian to use: 'unnormalized' 
        (default), 'symmetric', or 'randomwalk'.
    num_inits : int, optional
        Number of random initializations to try.
        Returns the best result.
    verbose : bool, optional
        Specifies whether to print info about
        the execution of the algorithm.
    
        
    Return
    ------
    (clusters, data_point_assigment, centroids)
        The results of the k-means algorithm on the spectrally
        embedded data. Clusters is a list of the clusters 
        (which are lists of ints). data_point_assigment is 
        a (n,) numpy array of ints that indicates which 
        cluster a data point has been assigned to. And 
        centroids is (k,d) numpy array specifying the 
        cluster centers.
    """
    
    num_samples = int(data.shape[0])
    
    # The kernel matrix of the data.
    kernel_matrix = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        for j in range(i, num_samples):
            kernel_matrix[i,j] = kernel_fun(data[i,:], data[j,:])
            kernel_matrix[j,i] = kernel_matrix[i,j]

    degrees = np.sum(kernel_matrix, axis=0)
            
    # Degree matrix
    D = np.diag(degrees)
    # Kernel (affinity) matrix
    K = kernel_matrix
    
    if L_type == 'unnormalized':
        L = D - K
    elif L_type == 'symmetric':
        Dinvsqrt = np.diag(degrees**(-0.5))
        L = np.eye(num_samples) - np.dot(Dinvsqrt, np.dot(K, Dinvsqrt))
    elif L_type == 'randomwalk':
        Dinv = np.diag(1.0 / degrees)
        L = np.eye(num_samples) - np.dot(Dinv, K)
        
    (eigvals, eigvecs) = nla.eigh(L)
    
    spectral_data = eigvecs[:, 1:(k+1)]
    
    return kmeans(spectral_data, k, num_iterations, num_inits=num_inits, verbose=verbose)
