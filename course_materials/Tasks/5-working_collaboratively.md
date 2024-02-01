# Working collaboratively

You are going to contribute a new file to this 'introtogit' repository.  To do this, we will work through the process of i) creating an issue describing what you want to add to the repository, ii) creating a branch to address that issue, and iii) creating a pull request to merge your branch into the main branch (and close the issue automatically)

1. Decide what you would like to contribute to the [code](code) folder. This should be either i) a SQL script, ii) and R script, or iii) a python script. It can be a simple function, a basic piece of code, or a simple select query. The code itself doesn't matter here, we're illustrating the principle of how lots of people can work on the same repository at the same time.

2. Create an issue describing what you are going to create. Again this is a toy example, but use the opportunity to think about what makes good issue writing. Describe clearly what you are going to make and why it is useful. Save the issue, add any labels if you think that is appropriate, and assign yourself.

3. Clone this repository, using what you have learned from previous exercises, and open the folder in VS Code. Create a new branch related to your issue. It is good practise to name your branch so that users can easily link to an issue, using the issue number. So, for example, if your created issue number #2 and it contained query that counted patients by SubICB, you could call it `2-subicb-counts`. The code to do this is in the previous exercise.

4. Create your new script and write your code, save it and use 'git status' to check that git is detecting your new file.

5. Add and commit your new file. Then push, using `--set-upstream` to create a remote version of your new branch.

6. Go back to Gitea and click on 'branches' from the main repository page. You should see your branch there, and an option for 'new pull request'. Click this. In the description box, add a sentence about what your pull request does. Additionally/instead, you can write 'Closes #X', where X is the number of the issue that you created that describes your planned work. 'Closes' is a special work in Github and Gitea, and when followed by a link to an issue (the '#' character preceding a number tells Gitea you are referring to an issue), you can link the issue to the pull request explicitly. Click 'create pull request' then assign an appropriate reviewer.

7. The reviewer will approve and merge your pull request, or they may request changes! Once this is done, you can change your branch back to main, and pull to see your merged changes

```bash

git checkout main
git pull

```

8. Finally you can delete your branch as follows:

```bash

git branch -d [your-branchname]

```

The process then repeats from here