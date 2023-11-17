# Practical tasks

## 1. Make a remote repository

## 2. Clone a repository (plus intro to VS code)

### VS Code

Visual Studio Code (VS Code) is a lightweight but powerful source code editor that runs across your desktop and is available for Windows, macOS, and Linux. It is developed by Microsoft and is free to use. VS Code has become a popular choice for developers of all levels due to its extensive features, rich ecosystem of extensions, and user-friendly interface.

### Key Features of VS Code:

**Extensive Support for Programming Languages:** VS Code provides built-in support for a wide range of programming languages, including JavaScript, TypeScript, Python, Java, C++, C#, and many more. It also offers syntax highlighting, bracket matching, auto-indentation, and other code editing features that make it easier to write and understand code.

**Smart Completions with IntelliSense:** VS Code's IntelliSense feature provides intelligent code completion suggestions as you type. This can save you time and effort by reducing the need to manually type out code snippets. IntelliSense also offers context-aware suggestions based on your code structure and the language you are using.

**Debugging Support:** VS Code integrates with various debugging tools, allowing you to step through your code, inspect variables, and identify errors or bugs. This makes it easier to troubleshoot and debug your applications.

**Rich Ecosystem of Extensions:** VS Code has a vast marketplace of extensions that can extend its functionality and add new features. These extensions can range from code linters and formatters to language-specific tools and productivity enhancements.

**Customizable Interface:** VS Code allows you to customize its appearance and behavior to suit your preferences. You can change themes, fonts, keybindings, and other settings to create a workspace that feels comfortable and efficient for you.

**Integrated Git Support:** VS Code provides built-in Git support, allowing you to manage your Git repositories directly from the editor. You can perform common Git operations like staging changes, committing changes, and pushing and pulling code. We will focus on the command line implementation of git, but the UI is extremely useful.

**Code Collaboration Features:** VS Code supports live collaboration features that enable multiple developers to work on the same codebase simultaneously. This can streamline development workflows and facilitate teamwork.

**Remote Development:** VS Code supports remote development, allowing you to connect to and work on codebases hosted on remote servers or cloud platforms. This can be useful for working on projects that are not located on your local machine.

### How to use VS Code:

[Presenter: Demonstrate and point to screen]
#### The default UI of Visual Studio Code (VS Code) consists of several key elements:

**Activity Bar:** Located on the left side of the window, the Activity Bar provides quick access to common actions, such as opening files, searching for symbols, and managing Git repositories.

**Explorer Pane:** Situated below the Activity Bar, the Explorer Pane displays the project's files and folders, allowing you to navigate and manage your project structure.

**Editor Area:** Occupying the main central area of the window, the Editor Area is where you write and edit your code. It provides syntax highlighting, code completion, and other code editing features.

**Status Bar:** Located at the bottom of the window, the Status Bar displays information about the current file, such as its encoding, line numbers, and zoom level.

**Panels:** VS Code supports several floating panels, such as the Debug pane and the Terminal pane, which can be docked to different sides of the window to provide additional information and functionality.

**Menubar:** The Menubar, located at the top of the window, provides access to organized menus for various actions, such as File, Edit, and View.

**Command Palette:** Accessible through the keyboard shortcut (Ctrl+Shift+P or Cmd+Shift+P), the Command Palette allows you to quickly search for and execute specific actions within VS Code.

This simplified overview outlines the essential elements of VS Code's default UI, providing a starting point for understanding its layout and navigating its features.

### Cloning a Repository from Gitea

#### Cloning Using the Gitea UI & Command line
Locate the repository you want to clone. Navigate to the repository you want to clone on the Gitea instance.

1. Click the "Clone" button. The "Clone" button is located in the top right corner of the repository page.

2. Choose the cloning method. Gitea offers two cloning methods: HTTPS and SSH. HTTPS is the more common and straightforward method, while SSH is more secure and requires setting up SSH keys.
a. **In reality, most organisations use the HTTPS method.**

a. HTTPS Cloning: Select the HTTPS URL and copy it to your clipboard.

b. SSH Cloning: Copy the SSH URL to your clipboard. If you haven't set up SSH keys, you'll need to generate them and follow the instructions provided on the Gitea page.

3. Clone the repository locally using the git clone command. 
a. Open a terminal window or your preferred Git client (like Visual Studio Code). 
b. Make sure that you are in a good directory to clone your repository (preferablly the `C:\` drive in `documents\repos` etc.)
c. Paste the copied URL into the terminal or Git client and execute the git clone command. 
For example, if you copied the HTTPS URL, the command would be:

```bash
git clone https://[gitea-instance-url]/[organization]/[repository-name].git
```

4. Hit enter! You have just cloned your first repository.


## 3. Getting remote and local repositories to talk

## 4. Add a .gitignore file, plus branching and merging

## 5. Working collaboratively
