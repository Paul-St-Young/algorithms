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
example 1: sample bivariate normal distribution
example 2: optimize change-point detection model
example 3: train Bernoulli restricted Boltzmann machine on NMIST data

## References

### All optimization.
{: .t60 }

{% include list-posts tag='optimization' %}

[1]: {{ site.url }}/assets/slides/gibbs.pdf
