---
layout: page
title:  "Coupling from the Past"
subheadline:  "by Eli Chertkov"
teaser: "Coupling from the past is an algorithm to generate perfect samples from a Markov chain (MC). It provides a measure of the mixing time M of the MC and in general scales as O(4MN), where N is the total number of states."

categories:
    - algorithm
tags:
    - markov chain
image:
   thumb: "cftp-ac.png"
header:
    image_fullwidth: "cftp-history.png"
    caption: CFTP histories
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Basic idea behind the CFTP algorithm.
  * Implementation of CFTP on a toy monotonic Markov chain.

## Examples
  * [simple\_cftp.py][ex1]: simplest CFTP implementation.
  * [CFTP.zip][ex2]: more advanced examples.

## References

### All Markov Chain
{: .t60 }

{% include list-posts tag='markov chain' %}

[1]:   {{ site.url }}/assets/slides/CouplingFromThePast.pdf
[ex1]: {{ site.url }}/assets/codes/cftp/simple_cftp.py
[ex2]: {{ site.url }}/assets/codes/cftp/CFTP.zip
