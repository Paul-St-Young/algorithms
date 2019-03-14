---
layout: page
title:  "BK-Tree"
subheadline:  "by Brian Busemeyer"
teaser: "BK-Tree is an efficient method for determining the closest member of a set to another point outside the set."

categories:
    - algorithm
tags:
    - optimization 
image:
   thumb: "bk_circle.png"
header:
    image_fullwidth: "bk_circle.png"
    caption: own work
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present how BK Trees work.
They are a data structure that enables efficient determinations of the closest member of a set to another point outside the set. 
A common example is spell checking, where the set is a word dictionary and the outside set is a misspelled word.
The algorithm only requires that a proper metric is defined for the set, and works using the triangle inequality.

## Examples
[My BK Tree implementation][2].

### All signal processing.
{: .t60 }

{% include list-posts tag='optimization' %}

[1]: {{ site.url }}/assets/slides/bktree.pdf
[2]: {{ site.url }}/assets/codes/bktree.ipynb

