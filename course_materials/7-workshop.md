# Practical tasks

## 1. Make a remote repository

## 2. Clone a repository (plus intro to VS code)

### VS Code

Visual Studio Code (VS Code) is a lightweight but powerful source code editor that runs across your desktop and is available for Windows, macOS, and Linux. It is developed by Microsoft and is free to use. VS Code has become a popular choice for developers of all levels due to its extensive features, rich ecosystem of extensions, and user-friendly interface.

#### Key Features of VS Code:

Extensive Support for Programming Languages: VS Code provides built-in support for a wide range of programming languages, including JavaScript, TypeScript, Python, Java, C++, C#, and many more. It also offers syntax highlighting, bracket matching, auto-indentation, and other code editing features that make it easier to write and understand code.

Smart Completions with IntelliSense: VS Code's IntelliSense feature provides intelligent code completion suggestions as you type. This can save you time and effort by reducing the need to manually type out code snippets. IntelliSense also offers context-aware suggestions based on your code structure and the language you are using.

Debugging Support: VS Code integrates with various debugging tools, allowing you to step through your code, inspect variables, and identify errors or bugs. This makes it easier to troubleshoot and debug your applications.

Rich Ecosystem of Extensions: VS Code has a vast marketplace of extensions that can extend its functionality and add new features. These extensions can range from code linters and formatters to language-specific tools and productivity enhancements.

Customizable Interface: VS Code allows you to customize its appearance and behavior to suit your preferences. You can change themes, fonts, keybindings, and other settings to create a workspace that feels comfortable and efficient for you.

Integrated Git Support: VS Code provides built-in Git support, allowing you to manage your Git repositories directly from the editor. You can perform common Git operations like staging changes, committing changes, and pushing and pulling code.

Code Collaboration Features: VS Code supports live collaboration features that enable multiple developers to work on the same codebase simultaneously. This can streamline development workflows and facilitate teamwork.

Remote Development: VS Code supports remote development, allowing you to connect to and work on codebases hosted on remote servers or cloud platforms. This can be useful for working on projects that are not located on your local machine.

These are just a few of the many features that make Visual Studio Code a valuable tool for developers of all levels. With its extensive capabilities, customizability, and rich ecosystem of extensions, VS Code has become a popular choice for modern software development.


### Cloning a Repository from Gitea

#### Cloning Using the Gitea UI
Locate the repository you want to clone. Navigate to the repository you want to clone on the Gitea instance.

Click the "Clone" button. The "Clone" button is located in the top right corner of the repository page.

Choose the cloning method. Gitea offers two cloning methods: HTTPS and SSH. HTTPS is the more common and straightforward method, while SSH is more secure and requires setting up SSH keys.
In reality, most organisations use the HTTPS method.

a. HTTPS Cloning: Select the HTTPS URL and copy it to your clipboard.

b. SSH Cloning: Copy the SSH URL to your clipboard. If you haven't set up SSH keys, you'll need to generate them and follow the instructions provided on the Gitea page.

Clone the repository locally. Open a terminal window or your preferred Git client (like Visual Studio Code). Paste the copied URL into the terminal or Git client and execute the git clone command. For example, if you copied the HTTPS URL, the command would be:

Bash
git clone https://[gitea-instance-url]/[organization]/[repository-name].git
Use code with caution. Learn more
Cloning Using the Command Line (e.g., in VS Code)
Open a terminal window or VS Code integrated terminal.

Navigate to the desired location for the cloned repository. You can use the cd command to change directories.

Execute the git clone command. Replace [gitea-instance-url], [organization], and [repository-name] with the actual URL, organization name, and repository name.

a. HTTPS Cloning:

Bash
git clone https://[gitea-instance-url]/[organization]/[repository-name].git
Use code with caution. Learn more
b. SSH Cloning:

Bash
git clone git@gitea-instance.com:[organization]/[repository-name].git
Use code with caution. Learn more
Verify the clone. Once the cloning process is complete, you can verify that the repository has been cloned successfully by checking the contents of the newly created directory.


## 3. Getting remote and local repositories to talk

## 4. Add a .gitignore file, plus branching and merging

## 5. Working collaboratively
