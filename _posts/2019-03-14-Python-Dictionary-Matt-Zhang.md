---
layout: page
title:  "Hash Tables, Dictionaries, and the Art of O(1) Lookup"
subheadline:  "by Matt Zhang"
teaser: "Reconstructing the magic behind Python's most useful data structure."

categories:
    - algorithm
tags:
    - dictionary, hash table
image:


   thumb: "dictionary.jpg"
header:
    image_fullwidth: "dictionary.jpg"
    caption: Spectral clustering of a toy dataset with four clusters.
---
<!-- Page Content Starts Here -->

## Presentation Summary
Hash tables are a very commonly used data structure, allowing for O(1) data storage and retrieval. In [these slides][slides], I show how Python implements a hash table through its built-in dictionary data type.

## Examples
  * [dictionary.ipynb][code]: notebook demonstrating the inner workings of the Python dictionary.

## References
  * [Inside Python Dictionaries][ref1]
  * [LeetCode Problem 3][ref2]

### All Signal Processing
{: .t60 }

{% include list-posts tag='signal processing' %}

[slides]: {{ site.url }}/assets/slides/dictionary.pdf
[code]: {{ site.url }}/assets/notebooks/dictionary.ipynb
[ref1]: https://just-taking-aride.com/inside_python_dict/chapter1.html
[ref2]: https://leetcode.com/problems/longest-substring-without-repeating-characters/
