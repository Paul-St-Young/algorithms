---
layout: page
title:  "Compressive Sensing"
subheadline:  "by Yubo \"Paul\" Yang"
teaser: "Compressive sensing takes advantage of sparsity to reconstruct full signal from sparse samples in a way that is not limited by Nyquist-Shannon. It effectively performs compression at the time of sensing so that fewer detector/sensors are needed. It has many practical applications ranging such as single-pixel camera, digital-to-analog conversion, and lattice dynamics in atomic simulations."

categories:
    - algorithm
tags:
    - signal processing
image:
   thumb: "cs-thumb.png"
header:
    image_fullwidth: "cs-phantom.png"
    caption: Shepp-Logan phantom
---
<!-- Page Content Starts Here -->

## Presentation Summary
In these slides, I present:

  * Basic idea behind the compressive sensing (cs).
  * Examples.

## Examples
  * [cs\_simple.py][ex1]: simplest CS implementation.
  * [beat\_nyqsha.py][ex2]: beat Nyquist-Shannon frequency for perfect reconstruction.

## References

### All Signal Processing
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]:   {{ site.url }}/assets/slides/csense.pdf
[ex1]: {{ site.url }}/assets/codes/csense/cs_simple.py
[ex2]: {{ site.url }}/assets/codes/csense/beat_nyqsha.py
