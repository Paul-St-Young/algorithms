---
layout: page
title:  "DSATUR"
subheadline:  "by Kevin Ly"
teaser: "DSATUR (degree of saturation) is a heuristic, easy-to-follow algorithm for coloring simple graphs."

categories:
    - algorithm
tags:
    - graph theory
image:
   thumb: "dsatur-thumb.png"
header:
    image_fullwidth: "dsatur-thumb.png"
    caption: Fig. 2.9 from R.M.R. Lewis, "A Guide to Graph Colouring," Springer (2016).
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I introduce the graph coloring problem and DSATUR. I also demo the [Networkx package][nx] for Python for graphs and networks, which contains its own implementation of DSATUR (among many other algorithms!). I give an example in grouping names, with a naive solution, and then a graphical solution using DSATUR. Also included is the [Mathematica notebook][me] that I used to generate most of the graphs seen in my presentation.

## Examples
  * [elements][elem]: data for the scripts
  * [nongraphical][eg1]: naive solution
  * [graphical][eg2]: graphical solution

## References

### All Graph Theory
{: .t60 }

{% include list-posts tag='graph theory' %}

[1]:   {{ site.url }}/assets/slides/dsatur.pdf
[nx]: https://networkx.github.io
[elem]: {{ site.url }}/assets/codes/dsatur/elements.txt
[eg1]: {{ site.url }}/assets/codes/dsatur/nongraphical.py
[eg2]: {{ site.url }}/assets/codes/dsatur/example.py
[me]: {{ site.url }}/assets/codes/dsatur/make-examples.nb
