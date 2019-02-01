---
layout: page
title:  "Randomized SVD"
subheadline:  "by Ryan Levy"
teaser: "Improving SVD speeds by assuming a low rank approximation and exploiting randomization."

categories:
    - algorithm
tags:
    - decomposition
image:
   thumb: "SVD_thumb.png"
header:
    image_fullwidth: "SVD.png"
    caption: Photo from SVD Wikipedia
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * A brief review of SVD and its uses
  * An implementation of a randomized SVD and some basic improvements we can perform.

## Examples
  * [randomizedSVD.ipynb][ex1]: randomizedSVD iPython notebook([html][ex1h])
    * [titan_matrix.txt][ex0]: example image text file

## References
  * [SIAM Review Article][ref1], Halko, Martinsson, Troppy (2009)
  * [Facebook's Random SVD Info Page][ref2]
  * [scikit-learn Randomized SVD Doc][ref3]

### All Signal Processing
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]:    {{ site.url }}/assets/slides/randomized_SVD.pdf
[ex0]:  {{ site.url }}/assets/notebooks/titan_matrix.txt
[ex1]:  {{ site.url }}/assets/notebooks/randomizedSVD.ipynb
[ex1h]: {{ site.url }}/assets/notebooks/randomizedSVD.html
[ref1]:https://arxiv.org/abs/0909.4061
[ref2]:https://research.fb.com/fast-randomized-svd/
[ref3]:https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html
