---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: algorithm.jpg
widget1:
  title: "Blog"
  url: 'http://paul-st-young.github.io/algorithms/blog/'
  image: news.jpg
  text: 'Every week, one of us will learn an algorithm, present and leave a brief summay at this altar.'
widget2:
  title: "Schedule"
  url: "http://paul-st-young.github.io/algorithms/roadmap/"
  image: wheel.jpg
  text: 'We meet every other Thusday from 1:00-2:00 pm CST in Loomis 322.'
widget3:
  title: "Archive"
  url: 'http://paul-st-young.github.io/algorithms/blog/archive'
  image: cyborg.jpg
  text: 'We will archive covered algorithms here, as well as post potentially interesting algorithms to be covered.'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
#callforaction:
#  url: https://tinyletter.com/feeling-responsive
#  text: Inform me about new updates and features ›
#  style: alert
#permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---
