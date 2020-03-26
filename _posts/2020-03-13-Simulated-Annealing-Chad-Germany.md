---
layout: page
title:  "Simulated Annealing"
subheadline: "by Chad Germany"
teaser: "A global minimum/maximum can be found amoungst local minima/maxima"

categories:
    - algorithm
tags:
    - optimization 
image:
   thumb: "simulated-annealing.png"
header:
    image_fullwidth: "simulated-annealing.png"
    caption: Graph of simulated annealing procedure from "Shift scheduling in a Nursing Home using Simulated Annealing."
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Simulated Annealing

## Examples
  * [example 1][ex1]: Simulated annealing code that minimizes objective function.
  * [module][ex1_2]: Module with simulated annealing class.
  * [example 2][ex2]: Applies simulated annealing algorithm to travelling salesman problem.
## References

### All Simulated Annealing
{: .t60 }

{% include list-posts tag='simulated annealing' %}

[1]: {{ site.url }}/assets/slides/Simulated_Annealing_2.pdf
[ex1]:{{ site.url }}/assets/codes/sim_anneal/sim_anneal_main.py
[ex1_2]:{{ site.url }}/assets/codes/sim_anneal/sim_anneal_vanilla.py
[ex2]: {{ site.url }}/assets/codes/sim_anneal/sim_anneal_travelling_salesman.py
