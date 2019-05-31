---
layout: page
title:  "Natural Language Generation"
subheadline:  "by Alina Kononov"
teaser: "How to automatically generate your thesis."

categories:
    - algorithm
tags:
    - language 
image:
   thumb: "rocket.png"
header:
    image_fullwidth: "context-free-grammar.png"
    caption: Simple context-free grammar.
---
<!-- Page Content Starts Here -->

## Presentation Summary
In [this presentation][talk], I show a few simple methods for natural language generation, including Markov text generators, n-gram Markov models, and context-free grammar. 

## Examples
  * [haiku.py][spoetry]: "Cut-up spoetry" or Haikus randomly generated from mass emails to UIUC engineering graduate students ([emails.txt][emails]).
  * [markov.tar][markov]: Implementation of a simple Markov text generator and an n-gram Markov text generator to rehash abstracts ([abstrats.txt][abstracts]).
  * [CFG.py][CFG]: Implementation of a simple context-free grammar to generate grammatically correct sentences from a word bank ([words.txt][words]).

### All natural language
{: .t60 }

{% include list-posts tag='language' %}

[talk]: {{ site.url }}/assets/slides/natural_language_generation.pdf
[spoetry]: {{ site.url }}/assets/codes/natural_language_generation/spoetry/haiku.py
[emails]: {{ site.url }}/assets/codes/natural_language_generation/spoetry/emails.txt
[markov]: {{ site.url }}/assets/codes/natural_language_generation/Markov/markov.tar
[abstracts]: {{ site.url }}/assets/codes/natural_language_generation/Markov/abstracts.txt
[CFG]: {{ site.url }}/assets/codes/natural_language_generation/context_free_grammar/CFG.py
[words]: {{ site.url }}/assets/codes/natural_language_generation/context_free_grammar/words.txt
