---
layout: page
title:  "Markov Decision Process and Reinforcement Learning"
subheadline:  "by Zeqian Li"
teaser: "How to beat human in 49 Atari games."

categories:
    - algorithm
tags:
    - machine learning
image:
   thumb: "cartpole.gif"
header:
    image_fullwidth: "cartpole.gif"
    caption: Inspired by how biological agents interact with the environment, reinforcement learning has been successful in many fiels, such as playing Go and Atari games. It also has a cool connection with stat mech. 
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [these slides][slides], I present:

  * Basic concepts of Markov Decision Process, Bellman equation
  * Statistical mechanics of Markov Decision Process
  * Soft Q-learning in reinforcement learning 

## Examples
  * A well-documented [code repo][openai] from OpenAI. 

## References
  * Most contents here are from lectures in ICTP Spring College on Physics of Complex Systems, 2018. Full video lectures are available on [ICTP Youtube channel][ictp-ytb] and [ICTP website][ictp-web]. 
  * [A good video lecture from Stanford CS231n course][cs231]. I also strongly recommend the full course.
  * [Mnih, Volodymyr, et al. "Human-level control through deep reinforcement learning." Nature 518.7540 (2015): 529.][ref-atari]
  * [Sutton, Richard S., and Andrew G. Barto. Reinforcement learning: An introduction. MIT press, 2018.][ref-sutton]
  * [Deep reinforcement learning resources on OpenAI][openai]

### All Machine Learning
{: .t60 }

{% include list-posts tag='machine learning' %}

[slides]:    {{ site.url }}/assets/slides/rl-no-animation.pdf
[ictp-ytb]:   https://www.youtube.com/watch?v=gmCZzEVs5dc&list=PLRwcSE2bmyBxsUP3FQdhP3J3Ema9vAxQB
[ictp-web]:   http://indico.ictp.it/event/8299/
[cs231]:      https://www.youtube.com/watch?v=lvoHnicueoE&index=15&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&t=0s
[ref-atari]:  https://www.nature.com/articles/nature14236
[ref-sutton]: http://www.incompleteideas.net/book/the-book-2nd.html
[openai]:     https://blog.openai.com/spinning-up-in-deep-rl/
