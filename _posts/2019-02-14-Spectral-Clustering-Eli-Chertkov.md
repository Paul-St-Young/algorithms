---
layout: page
title:  "Spectral Clustering"
subheadline:  "by Eli Chertkov"
teaser: "Identifying clusters in data using linear algebra and graph theory."

categories:
    - algorithm
tags:
    - clustering, data analysis
image:
   thumb: "spectral_clustering_thumbnail.png"
header:
    image_fullwidth: "spectral_clustering_thumbnail.png"
    caption: Spectral clustering of a toy dataset with four clusters.
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * A brief review of k-means, spectral clustering, and graph Laplacians.
  * Examples of using k-means and spectral clustering on a toy dataset and on the MNIST handwritten digit dataset.

## Examples
  * [algorithms.py][script]: python script with $k$-means and spectral clustering algorithms that are used in the following iPython notebooks.
  * [spectral_embedding_toy.ipynb][ex1]: spectral clustering on toy dataset iPython notebook([html][ex1h])
  * [spectral_embedding_mnist.ipynb][ex2]: spectral clustering on MNIST dataset iPython notebook([html][ex2h])

## References
  * [A Tutorial on Spectral Clustering][ref1], U. von Luxburg (2007)
  * [scikit-learn Spectral Clustering Doc][ref2]
  * [scikit-learn Clustering Overview][ref3]

### All Signal Processing
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]:    {{ site.url }}/assets/slides/SpectralEmbedding.pdf
[script]: {{ site.url }}/assets/codes/spectralclustering/algorithms.py
[ex1]:  {{ site.url }}/assets/notebooks/spectral_embedding_toy.ipynb
[ex1h]:  {{ site.url }}/assets/notebooks/spectral_embedding_toy.html
[ex2]: {{ site.url }}/assets/notebooks/spectral_embedding_mnist.ipynb
[ex2h]: {{ site.url }}/assets/notebooks/spectral_embedding_mnist.html
[ref1]:https://arxiv.org/abs/0711.0189
[ref2]:https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering
[ref3]:https://scikit-learn.org/stable/modules/clustering.html#clustering
