---
layout: page
title:  "Gibbs Sampling"
subheadline:  "by Yubo 'Paul' Yang"
teaser: "The basic Gibbs sampler samples a joint probability distribution one variable at a time. Each random variable is sampled from its full conditional probability distribution with all other variables fixed. Independent variables can be sampled simultaneously, making the Gibbs sampler ideal for the restricted Boltzmann machine."

categories:
    - algorithm
tags:
    - machine learning
image:
   thumb: "gibbs_sample2000.png"
header:
    image_fullwidth: "BN_MH_vs_Gibbs.png"
    caption: naive Metropolis-Hasting vs. numpy vs. Gibbs
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Basic idea behind the Gibbs sampling algorithm.
  * Basic application to sample the bivariate normal distribution.
  * Application to change-point detection
  * Application to restricted Boltzmann machine


## Examples
  * [example 1][ex1]: sample bivariate normal distribution
  * [example 2][ex2]: optimize change-point detection model
  * [example 3][ex3]: train Bernoulli restricted Boltzmann machine on NMIST data

## References
  * [MCMC: The Gibbs Sampler][ref1], The Clever Machine
  * [Beyesian Inference: Metropolis-Hasting Sampling][ref2], Ilker Yildirim
  * [Beyesian Inference: Gibbs Sampling][ref3], Ilker Yildirim
  * [A Practical Guide to Training Restricted Boltzmann Machines][ref4], Geoffrey E. Hinton
  * [Introduction to Restricted Boltzmann Machines][ref5], Edwin Chen
  * [deeplearning.net][ref6]

### All optimization.
{: .t60 }

{% include list-posts tag='optimization' %}

[1]: {{ site.url }}/assets/slides/gibbs.pdf
[ex1]: {{ site.url }}/assets/notebooks/gibbs_sampling/eg1_bivariate_std_normal.html
[ex2]: {{ site.url }}/assets/notebooks/gibbs_sampling/eg2_change_point_detection.html
[ex3]: {{ site.url }}/assets/notebooks/gibbs_sampling/eg3_brbm_mnist.html
[ref1]: https://theclevermachine.wordpress.com/2012/11/05/mcmc-the-gibbs-sampler/
[ref2]: http://www.mit.edu/~ilkery/papers/MetropolisHastingsSampling.pdf
[ref3]: http://www.mit.edu/~ilkery/papers/GibbsSampling.pdf
[ref4]: http://link.springer.com/chapter/10.1007/978-3-642-35289-8_32
[ref5]: http://blog.echen.me/2011/07/18/introduction-to-restricted-boltzmann-machines/
[ref6]: http://deeplearning.net/tutorial/rbm.html
