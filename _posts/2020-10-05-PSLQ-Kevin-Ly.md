---
layout: page
title:  "PSLQ"
subheadline:  "by Kevin Ly"
teaser: "Finding Integer Relations"

categories:
    - algorithm
tags:
    - integer relations
    - optimization
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Definition and examples of finding integer relations.
  * One solution via the PSLQ algogithm.

## Examples
  * [demo1.ipynb][ex1]: A demo on the basics of mpmath's PSLQ function
  * [demo2.ipynb][ex2]: A demo trying (and failing) to find a finite series form of the Euler-Mascheroni constant
  * [demo3.ipynb][ex3]: A demo showing how to use PSLQ to find a formula for Pi

## References
  * [mpmath library][ref1]
  * [Pseudocode (Bailey)][ref2]

### All Optimization
{: .t60 }

{% include list-posts tag='optimization' %}

[1]:   {{ site.url }}/assets/slides/PSLQ.pdf
[ex1]: {{ site.url }}/assets/notebooks/PSLQ/demo1.ipynb
[ex2]: {{ site.url }}/assets/notebooks/PSLQ/demo2.ipynb
[ex3]: {{ site.url }}/assets/notebooks/PSLQ/demo3.ipynb
[ref1]: http://mpmath.org
[ref2]: http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html
