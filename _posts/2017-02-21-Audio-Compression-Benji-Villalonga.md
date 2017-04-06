---
layout: page
title:  "Audio Compression"
subheadline:  "by Benjamin Villalonga Correa"
teaser: "Problems in audio compression form just a subset of the general problem of signal compression, and general techniques can well be applied to solve them. However, it is possible to benefit greatly from being aware of the very particular way in which the human brain perceives and interprets sound, being able to optimize compression techniques to keep only information that is relevant to human perception. In this presentation, I focus on speech compression, and more particularly on an implementation using a Linear Predicting Model (LPM). The LPM provides a very efficient way of reconstructing a signal from a very small set of compressed data (up to 95% of data can be neglected), generating a sythesized speech that keeps the original phonemes and the quality of the voice of the speaker, who can be recognized easily. This technique has been used in telephony applications."

categories:
    - algorithm
tags:
    - signal processing
    - compression
    - speech
    - filter
image:
   thumb: "frequency_song.eps"
header:
    image_fullwidth: "fourier_song.eps"
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][7], I talk about:

  * the audio compression problem.
  * human perception of the voice.
  * the speech compression problem.
  * the Linear Prediction Model (LPM).
  * LPM implementation for speech compression.


## Examples
  * A [Jupyter notebook][1] to compress and decompress audio using an LPM. Feel free to contact me if you are having trouble using or understancing this notebook.
  * A [Jupyter notebook][2] to fourier-analyze the audio files manipulated in using the compression-decompression [notebook][2] referred to above.
  * A [.wav file][3] (me saying the English alphabet) used as a demonstration for the previous two notebooks.

## References
  * Three practical explanations of how the LPM works for speech compression are [this one][4], [this one][5] and [this one][6].
  * A comprehensive book on Linear Prediction Models is: Vaidyanathan, P. P. (2007). The theory of linear prediction. Synthesis lectures on signal processing, 2(1), 1-184.

### All Signal Processing.
{: .t60 }

{% include list-posts tag='signal processing' %}

[1]: {{ site.url }}/assets/notebooks/LPM_compress_decompress.ipynb
[2]: {{ site.url }}/assets/notebooks/LPM_fourier_analysis.ipynb
[3]: {{ site.url }}/assets/notebooks/LPM_demo.wav
[4]: http://www.ece.ucsb.edu/Faculty/Rabiner/ece259/digital%20speech%20processing%20course/lectures_new/Lecture%2013_winter_2012_6tp.pdf
[5]: http://www.seas.ucla.edu/~ingrid/ee213a/speech/vlad_present.pdf
[6]: http://cs.haifa.ac.il/~nimrod/Compression/Speech/S4LinearPredictionCoding2009.pdf
[7]: {{ site.url }}/assets/slides/LPM_compress_decompress.ipynb

