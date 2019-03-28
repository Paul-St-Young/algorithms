---
layout: page
title:  "BK-Tree"
subheadline:  "by Brian Busemeyer"
teaser: "BK-Tree is an efficient method for determining the closest member of a set to another point outside the set."

categories:
    - algorithm
tags:
    - data structures
image:
   thumb: "btree_small.png"
header:
    image_fullwidth: "btree.png"
    caption: own work
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this notebook][1] ([html][2]), I present how B+trees work.
B-trees are ubiquitous database structures, used in the NTFS, FAT, and Ext4 file system formats, among others. The reason is simple: O(log(N)) overhead, O(log(N)) lookup, O(log(N)) deletion, and its nodes can be adjusted to fill disk blocks or caches.
They excel whenever an algorithm utilizes large, slow memory access combined with small, fast memory access. Some easy examples are disk and RAM, RAM an cache, and others.

### All data structures.
{: .t60 }

{% include list-posts tag='data structures' %}

[1]: {{ site.url }}/assets/notebooks/btree.ipynb
[2]: {{ site.url }}/assets/notebooks/btree.html

