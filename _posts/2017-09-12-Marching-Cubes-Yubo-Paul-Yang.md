---
layout: page
title:  "Marching Cubes"
subheadline:  "by Yubo 'Paul' Yang"
teaser: "Marching cubes is a Classic algorithm for isosurface extraction. It utilizes efficient table lookups to turn a 2D isosurface of 3D volumetric data into a collection of triangles. Although marching cubes is a dated algorithm, it still demonstrates much of the concepts behind modern rendering approaches."

categories:
    - algorithm
tags:
    - visualization
image:
   thumb: "chf_orbs.png"
header:
    image_fullwidth: "silvio-kundt-cubes.jpg"
    caption: Photo by Silvio Kundt on Unsplash
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][1], I present:

  * Basic idea behind the marching cubes algorithm
  * Plot PySCF basis functions, orbitals, and charge density using marching cubes implemented in skimage.measure

## Examples
  * [example 1][ex1]: simplest demo (Gaussian)
  * [example 2][ex2]: basis functions from PySCF
  * [example 3][ex3]: Hatree-Fock orbitals/electron density from PySCF

## References
  * [Polygonising a scalar field][ref1], Oaul Bourke
  * [Smooth Voxel Terrain][ref2], Mikola Lysenko
  * [Constrained Elastic Surface Nets][ref3], Sarah Gibson

### All visualization
{: .t60 }

{% include list-posts tag='visualization' %}

[1]: {{ site.url }}/assets/slides/marching_cubes.pdf
[ex1]: https://github.com/Paul-St-Young/share/tree/master/algorithms/iso3d/basis
[ex2]: https://github.com/Paul-St-Young/share/tree/master/algorithms/iso3d/basis
[ex3]: https://github.com/Paul-St-Young/share/tree/master/algorithms/iso3d/chf
[ref1]:http://paulbourke.net/geometry/polygonise/
[ref2]:https://0fps.net/2012/07/12/smooth-voxel-terrain-part-2/
[ref3]:http://www.merl.com/publications/docs/TR99-24.pdf
