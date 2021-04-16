## Guidelines for adding your post
** please pull before you push! **
  1. Fork this repository ([docs](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo))
  2. Create (and switch) to a new branch `git checkout gh-pages -b my_branch_name`
  4. Copy one of the posts in the "\_post" folder and rename in the format year-month-day-title-author.
  5. Edit your post in markdown format.
  6. Upload your presentation slides to the "assets/slides" folder. Please provide a link in post.  
    - Try and keep your file size as small as possible  
  7. Upload your graphics (if any) to the "images" folder, they can be used as the main picture or thumbnail of your post.
  8. Upload your jupyter notebooks (if any) to the "assets/notebooks" folder.
  9. In case there are changes to the original upstream repo that aren't in your fork, you can update your forked `gh-pages` branch and merge it into your working branch
```bash
# Add upstream if you don't already have it
git remote add upstream https://github.com/Paul-St-Young/algorithms.git

# Update your fork's local gh-pages; make sure all your changes are committed before this
git fetch upstream
git checkout gh-pages
git merge upstream/gh-pages
# Merge local gh-pages into your working branch
git checkout my_branch_name
git merge gh-pages
```
Fix any [merge conflicts](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line) that pop up  
  10. Push your commits to your remote fork (e.g. `git push origin my_branch_name`)   
  11. Open a pull request to merge the change from your fork ([docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork))

## Schedule

For current schedule, see [Logistics](http://paul-st-young.github.io/algorithms/roadmap/).

## Ideas for presentations

Please see [Logistics](http://paul-st-young.github.io/algorithms/roadmap/) page!
