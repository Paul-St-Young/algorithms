---
layout: page
title:  "Dijkstra"
subheadline:  "by Kiel Williams"
teaser: "For a general graph with an arbitrary number of nodes and edges, it's usually not obvious what the shortest path is between two nodes. Dijkstra's algorithm is a famous method for systematically determining the length of that shortest path. I explore how to implement this algorithm for a simple graph in 2D, and show how it still works even if the path is subject to some simple constraints."

categories:
    - algorithm
tags:
    - graph theory
image:
   thumb: "dijkstra_wall.gif"
header:
    image_fullwidth: "dijkstra_foundit.png"
    caption: Dijkstra algorithm
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Basic idea behind the Dijkstra algorithm

## Examples
  * [example 1][ex1]: Jupyter [notebook][ex1nb] with simple implementation of Dijkstra.

## References

### All Graph Theory
{: .t60 }

{% include list-posts tag='graph theory' %}

[ex1]: {{ site.url }}/assets/notebook/dijkstra_alg.html
[ex1nb]: {{ site.url }}/assets/notebook/dijkstra_alg.ipynb
