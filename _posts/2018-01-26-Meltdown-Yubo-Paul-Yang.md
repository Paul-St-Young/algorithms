---
layout: page
title:  "Meltdown"
subheadline:  "by Yubo 'Paul' Yang"
teaser: "Meltdown is a hardware exploit that allows an unprivileged user to access system memory."

categories:
    - algorithm
tags:
    - security
image:
   thumb: "meltdown_logo.png"
header:
    image_fullwidth: "meltdown-spectre.png"
    caption: https://granicus.com/blog/spectre-meltdown-impact
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Basic idea behind the meltdown algorithm

## Examples
  * [main.c][ex1]: A simplified Proof-of-Principle implementation modified from paboldin
  * [cache_time.c][ex2]: compare access time to cached v.s. uncached addresses
  * [cache_time.h][ex3]: get_access_time to address
  * [makefile][ex4]: makefile for the above sources

## References
  * [Google Project Zero Blog][ref1], Jann Horn
  * [Meltdown and Spectre Official Website][ref2]
  * [Proof-of-Principle Implementation][ref3], Pavel Boldin

### All Security
{: .t60 }

{% include list-posts tag='security' %}

[1]:   {{ site.url }}/assets/slides/meltdown.pdf
[ex1]: {{ site.url }}/assets/codes/meltdown/main.c
[ex2]: {{ site.url }}/assets/codes/meltdown/cache_time.c
[ex3]: {{ site.url }}/assets/codes/meltdown/cache_time.h
[ex4]: {{ site.url }}/assets/codes/meltdown/makefile
[ref1]:https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html
[ref2]:https://meltdownattack.com
[ref3]:https://github.com/paboldin/meltdown-exploit
