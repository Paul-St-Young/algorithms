---
layout: page
title:  "Kriging"
subheadline:  "by Yubo 'Paul' Yang"
teaser: "Kriging is an interpolation method. Kriging provides confidence interval to its predictions. Kriging works by minimizing the variance of the prediction error over existing data."

categories:
    - algorithm
tags:
    - signal processing, machine learning
image:
   thumb: "okrig-nsin.png"
header:
    image_fullwidth: "meltdown-spectre.png"
    caption: https://granicus.com/blog/spectre-meltdown-impact
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Basic idea behind the kriging algorithm.
  * Implementation of ordinary kriging applied to 1D interpolation.

## Examples
  * [okrig.py][ex1]: ordinary kriging on noisy sin(x) data
  * [skl.py][ex2]: sklearn gpr applied to data imported from okrig.py

## References
  * [Kriging Example][ref1]
  * [Ordinary Kriging][ref2]
  * [Gaussian Process for Machine Learning][ref3], C. E. Rasmussen and C. K. I. Williams 2006

### All Security
{: .t60 }

{% include list-posts tag='security' %}

[1]:   {{ site.url }}/assets/slides/kriging.pdf
[ex1]: {{ site.url }}/assets/codes/kriging/okrig.py
[ex2]: {{ site.url }}/assets/codes/kriging/skl.py
[ref1]:http://www.imm.dtu.dk/~alan/krexample.pdf
[ref2]:https://msu.edu/~ashton/classes/866/papers/gatrell_ordkrige.pdf
[ref3]:http://www.gaussianprocess.org/gpml/chapters/RW.pdf
