---
layout: page
title:  "Linear Sum Assignment"
subheadline:  "by Yubo \"Paul\" Yang"
teaser: "The Linear Sum Assignment Problem (LSAP) is a combinatoric optimization problem with many practical applications. An elegant solution was proposed in 1955 by Kuhn and lovingly dubbed \"The Hungarian algorithm\". This polynomial-scaling algorithm is sometimes credited as the predecessor to primal-dual linear programming approaches."

categories:
    - algorithm
tags:
    - linear programming
    - optimization
image:
   thumb: "lsap-thumb.gif"
header:
    image_fullwidth: "lsap-wide.png"
    caption: A fine example
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Definition and examples of the linear assignment problem.
  * A polynomial-scaling solution: the Hungarian algorithm.

## Examples
  * [lsap-kuhn-hung.tgz][ex1]: "a_dev" contains a simple implementation of the Hungarian algorithm along with visualization. "b_time" is a snakemake folder that measures execution time.

## References
  * [Burkard and Derigs 1980][ref1]
  * [Burkard et al. 2009][ref2]

### All Linear Programming
{: .t60 }

{% include list-posts tag='linear programming' %}

[1]:   {{ site.url }}/assets/slides/lsap-kuhn-hungarian.pdf
[ex1]: {{ site.url }}/assets/codes/lsap-kuhn-hung.tgz
[ref1]: https://www.springer.com/gp/book/9783540102670
[ref2]: http://www.assignmentproblems.com
