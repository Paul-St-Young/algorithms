---
layout: page
title:  "Neural Network on a Tensor Train"
subheadline:  "by Xiongjie Yu"
teaser: "Redundancy in the weight matrix of a neural network can be much reduced with a tensor network formulation. More than 99% compression rate can be achieved while maintaing accuracy. Tensor train representation of a neural network is compact. This formalism may allow neural networks to be trained on mobile devices."

categories:
    - algorithm
tags:
    - machine learning
image:
   thumb: "tensor_train.png"
header:
    image_fullwidth: "toy_train.jpg"
    caption: by Darren Bockman
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Basic idea of tensor train representation of a matrix
  * Compression of a feed-forward neural network

## Examples
  * [example 1][ex1]: compression

## References
  * [Tensorizing Neural Networks][ref1]
  * [Ultimate tensorization: compressing convolutional and FC layers alike][ref2]

### All optimization.
{: .t60 }

{% include list-posts tag='optimization' %}

[1]: {{ site.url }}/assets/slides/Neural_Network_on_a_Tensor_Train.pdf
[ex1]: {{ site.url }}/assets/notebooks/TTNet.html
[ref1]: https://arxiv.org/abs/1509.06569
[ref2]: https://arxiv.org/abs/1611.03214
