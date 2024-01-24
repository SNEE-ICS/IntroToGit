
# Cloning a Repository from Gitea

## Cloning Using the Gitea UI & Command line
Locate the repository you want to clone. Navigate to the repository you want to clone on the Gitea instance.

1. Click the "Clone" button. The "Clone" button is located in the top right corner of the repository page.

2. Choose the cloning method. Gitea offers two cloning methods: HTTPS and SSH. HTTPS is the more common and straightforward method, so we will use this. Select the HTTPS URL and copy it to your clipboard.

3. Clone the repository locally using the git clone command. 
a. Open a terminal window in Visual Studio Code. 
b. Make sure that you are in a good directory to clone your repository (preferablly the `C:\` drive in `documents\repos` etc.)
c. Paste the copied URL into the terminal or Git client and execute the git clone command. 
For example, if you copied the HTTPS URL, the command would be:

```bash
git clone https://[gitea-instance-url]/[organization]/[repository-name].git
```

4. Hit enter! You have just cloned your first repository.