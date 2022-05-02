## FAST GIT OVERVIEW

### COMMANDS

*To download a repo: `git clone <url>`

*To initialize a git repo: `git init`. Into repository folder

*To know the repo status: `git status`. First you will be able to know the branch, next you can see the repo content, included the untracked files (files that are not currently in the database)

*To stage changes: `git add -A`. Apparently nothing happens, but if you do again git status you will watch all the deletion and addition pending files have been staged.

*To commit to database: `git commit -m 'brief explanation'`. This commits every staged change to the database.

*To watch what has happen to the repo: `git log`. This allows you to watch authors, dates and brief explanation of the changes.

*To define where you will publish your repo: `git remote add origin <url>`. To push and pull from the specified origin

*To publish your repo: `git push -u origin master`. This is needed the first time you push, you are just pushing your files to the remote origin in the specified place. 

*To make your repo up-to-date: `git pull`. This just allows you to download the changes commited to the repo. If the changes are not compatible with your version, you will have to merged manually.

*To create a new branch: `git checkout -b <branch name>`. This allows experimentation without intefere.

*To switch between branches: `git checkout <branch name>`. This allows you to move between branches

*To merge branches: `git merge <merging branch>`. This is similar to `git pull` but from other branch and not from the origin.

And that's all, I expect you to find this helpful.


