---
layout: page
title:  "Huffman Encoding"
subheadline:  "by Chad Germany"
teaser: "Huffman Encoding is a technique of compressing data to reduce its size without losing any of the details. Huffman Coding is generally useful to compress the data in which there are frequently occurring characters. The most frequent character gets the smallest code and the least frequent character gets the largest code."

categories:
    - algorithm
tags:
    - compression
image:
   thumb: "binary_code.jpg"
header:
    image_fullwidth: "huffman.png"
    caption: A Huffman Tree 
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Basic idea behind the Huffman encoding algorithm.
  * Implementation of the algorithm on a text document.

## Examples

  * [huffman_encoding.ipynb][ex1]: I created a text file and wrote a message that the code reads and encodes that message to huffman.txt. It can then be read and and written to decode.txt([html][ex1h])

### All Compression
{: .t60 }

{% include list-posts tag='compression' %}

[1]:   {{ site.url }}/assets/slides/huffman_encoding.pdf
[ex1]:  {{ site.url }}/assets/notebooks/huffman_encoding.ipynb
[ex1h]:  {{ site.url }}/assets/notebooks/huffman_encoding.html

