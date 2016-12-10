---
layout: page
title:  "Belief Propagation"
subheadline:  "by Eli Chertkov"
teaser: "Belief Propagation is a powerful message-passing algorithm at the heart of some of the most effective error-correcting coding schemes currently in use."

categories:
    - algorithm
tags:
    - inference
image:
   thumb: "bp.png"
header:
    image_fullwidth: "ldpc.png"
    caption: A low-density parity check code
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this talk][1], I present on the Belief Propagation (or Sum-product) algorithm for performing statistical inference on a probabilistic graphical model. I discuss the application of the method to low-density parity-check (LDPC) codes.

## Examples

The python code that I used for the LDPC code example in the talk can be found [here][2].

## References

### All optimization.
{: .t60 }

{% include list-posts tag='inference' %}

[1]: {{ site.url }}/assets/slides/BeliefPropagation.pdf
[2]: {{ site.url }}/assets/notebooks/BeliefPropagationCode.zip