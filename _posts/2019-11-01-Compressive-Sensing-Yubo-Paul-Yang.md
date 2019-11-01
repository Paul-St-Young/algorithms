---
layout: page
title:  "Compressive Sensing"
subheadline:  "by Yubo \"Paul\" Yang"
teaser: "Compressive sensing takes advantage of sparsity to reconstruct full signal from sparse samples in a way that is not limited by Nyquist-Shannon. It effectively performs compression at the time of sensing so that few detector/sensors are needed. It has many practical applications such as single-pixel camera, digital-to-analog conversion, and lattice dynamics in atomic simulations."

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
In [these slides][1], I present:

  * Basic idea behind the compressive sensing (cs).
  * A few simple examples.

## Examples
  * [cs\_simple.py][ex1]: simplest CS implementation.
  * [beat\_nyqsha.py][ex2]: beat Nyquist-Shannon frequency for perfect reconstruction.
  * [cs\_phantom.py][ex3]: reconstruct Shepp-Logan phantom. You also need [phantom.py][ph] to generate the phantom image and [config\_h5][ch5] to store the constructed A matrix (or code is pretty slow).

## References
  * [molecular dynamics spectrum][ref1]
  * [lattice dynamics][ref2]
  * [belief propagation vs. L1][ref3] and its [phantom generator][refph]

### All Signal Processing
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]:   {{ site.url }}/assets/slides/csense.pdf
[ex1]: {{ site.url }}/assets/codes/csense/cs_simple.py
[ex2]: {{ site.url }}/assets/codes/csense/beat_nyqsha.py
[ex3]: {{ site.url }}/assets/codes/csense/cs_phantom.py
[ph]: {{ site.url }}/assets/codes/csense/phantom.py
[ch5]: {{ site.url }}/assets/codes/csense/config_h5.py
[ref1]: https://www.pnas.org/content/109/35/13928
[ref2]: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.113.185501
[ref3]: https://journals.aps.org/prx/abstract/10.1103/PhysRevX.2.021005
[refph]: http://aspics.krzakala.org/
