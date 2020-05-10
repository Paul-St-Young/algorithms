---
layout: page
title:  "Dithering"
subheadline: "by Kevin Ly"
teaser: "Image dithering / digital halftoning"

categories:
    - algorithm
tags:
    - dither
    - halftoning
    -  
author: ryan

---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][1], I present:

  * Examples of image dithering and digital halftoning on same classic photos

## Examples   
  * [Random dither][2]
  * [Ordered dither][3]
  * [Error-diffusion halftoning][4]

## References  
  * [[1] `DHALF.TXT`][5]  


[1]: {{ site.url }}/assets/slides/dither.pdf
[2]: {{ site.url }}/assets/notebooks/dither/random_dither.ipynb
[3]: {{ site.url }}/assets/notebooks/dither/ordered_dither.ipynb
[4]: {{ site.url }}/assets/notebooks/dither/error_diffusion.ipynb
[5]: https://github.com/SixLabors/ImageSharp/blob/master/src/ImageSharp/Processing/Processors/Dithering/DHALF.TXT
