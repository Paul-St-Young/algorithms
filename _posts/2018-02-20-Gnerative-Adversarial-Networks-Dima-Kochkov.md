---
layout: page
title:  "Generative Adversarial Networks"
subheadline:  "by Dima Kochkov"
teaser: "GANs are Neural Network architecture comprised of two networks: generator and discriminator, that are pitted against each other."

categories:
    - algorithm
tags:
    - machine learning
image:
   thumb: "deconvolution.gif"
header:
    image_fullwidth: "gans-training.png"
    caption: Training GANs
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this notebook][1], I present:

  * Basic idea behind the GANs
  * Cool applications
  * Training code using [TFGAN library][tfgan]

## Examples

## References
  * [original paper][orig]
  * [cripy faces][face]

### All Machine Learning
{: .t60 }

{% include list-posts tag='machine learning' %}

[1]: {{ site.url }}/assets/notebooks/gans/gans.html
[orig]: https://arxiv.org/pdf/1406.2661.pdf
[face]: http://research.nvidia.com/sites/default/files/publications/karras2017gan-paper.pdf
[tfgan]:https://github.com/tensorflow/models/tree/master/research/gan
