# Add a `.gitignore` file, plus branching and merging

1. In VS code, use `ls` and `cd` to make sure that you are in the top-level folder of your git repository.

2. Use `git status` and `git pull` to make sure that your repository is up to date, and that you are on the main branch.

3. We are going to make a fake dataset in our repository, which we do not want to upload to Gitea. Open excel, and put in some fake data. Save the file in CSV format.

5. Type `git status` into your terminal. You should see that your CSV file is there and ready to be added and committed. We don't want to do this!

4. In your terminal, in your top-level folder in your repository type `touch .gitignore`. To make a new, empty file called `.gitignore`. Open this file using the explorer bar in VS code (or can you find a terminal command to open the file?)

5. Add the line '*.csv' (excluding quotes) to the top of your `.gitignore` and save and close the file.

6. Type in `git status` again. You should see that your CSV file is no longer available for adding and committed, but your .gitignore file is.

7. Now that we are happy we can add, commit and push our changes using our knowledge gained from the last exercise.