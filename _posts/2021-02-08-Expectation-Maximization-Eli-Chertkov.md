---
layout: page
title:  "Expectation Maximization"
subheadline: "by Eli Chertkov"
teaser: "Parameter estimation via maximum likelihood"

categories:
    - algorithm
tags:
    - fitting
image:
   thumb: "em_test3b_density.png"
header:
    image_fullwidth: "em_test3b_density.png"
    caption: Density using EM algorithm
author: eli

---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Expectation Maximization algorithm using Gaussian Mixture Models

## Examples
  * [em.py][2]
  * [test_em.py][3]
  * [test_em1.py][4]
  * [test_em2.py][5]
  * [test_em3.py][6]

## References
  * [Andrew Ng's Stanford CS 229 Lectures][7]
  * [Padhraic Smyth’s UCI CS 274 Lecture notes][8]

### All Fitting
{: .t60 }

{% include list-posts tag='fitting' %}

[1]: {{ site.url }}/assets/slides/EMTalk.pdf
[2]: {{ site.url }}/assets/code/em/em.py
[3]: {{ site.url }}/assets/code/em/test_em.py
[4]: {{ site.url }}/assets/code/em/test_em1.py
[5]: {{ site.url }}/assets/code/em/test_em2.py
[6]: {{ site.url }}/assets/code/em/test_em3.py
[7]: https://see.stanford.edu/materials/aimlcs229/cs229-notes8.pdf
[8]: https://www.ics.uci.edu/~smyth/courses/cs274/notes/EMnotes.pdf
