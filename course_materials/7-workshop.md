# Workshop

## Objective:

This worksheet guides you through the complete Git workflow process using an example SQL project. Follow the steps to initialize a Git repository, create an issue, and raise a pull request.

---

### Step 1: Initialize a Git Repository

1. **Open your terminal or command prompt.**

2. **Navigate to the directory where you want to create your project.**

    ```bash
    cd path/to/your/directory
    ```

3. **Initialize a new Git repository.**

    ```bash
    git init
    ```

---

### Step 2: Create a SQL Project

1. **Create a new SQL file for your project.**

    ```bash
    touch main.sql
    ```

2. **Add some SQL code to the file.**

    ```sql
    -- main.sql
    CREATE TABLE users (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    );
    ```

3. **Stage and commit your changes.**

    ```bash
    git add main.sql
    git commit -m "Initial SQL project setup"
    ```

---

### Step 3: Create an Issue

1. **Visit the repository on GitHub or Gitea.**

2. **Navigate to the "Issues" tab.**

3. **Create a new issue:**
   - Title: "Implement User Registration"
   - Description: "Create SQL statements for user registration feature."

4. **Assign the issue to yourself.**

---

### Step 4: Work on a New Feature Branch

1. **Create a new branch for your feature.**

    ```bash
    git checkout -b feature-user-registration
    ```

2. **Add SQL code for user registration to `main.sql`.**

    ```sql
    -- main.sql
    ALTER TABLE users ADD COLUMN registration_date DATE;
    ```

3. **Stage and commit your changes.**

    ```bash
    git add main.sql
    git commit -m "Add user registration feature"
    ```

---

### Step 5: Raise a Pull Request

1. **Push your feature branch to the remote repository.**

    ```bash
    git push origin feature-user-registration
    ```

2. **Visit the repository on GitHub or Gitea.**

3. **Navigate to the "Pull Requests" tab.**

4. **Create a new pull request:**
   - Base: `main` or `master` branch
   - Compare: `feature-user-registration` branch

5. **Add a description of your changes.**

6. **Assign a reviewer and label to your pull request.**

7. **Submit the pull request.**

---

Congratulations! You've completed the Git workflow process, from initializing a repository to creating an issue and raising a pull request. This workflow demonstrates how to collaboratively work on a project, manage tasks, and propose changes using Git and platforms like GitHub or Gitea.