# GitGraph Guide 🚀

This guide explains how to use the GitGraph project, how to switch accounts, and the importance of Personal Access Tokens (PAT).

## 1. How to Switch to a Different GitHub Account

If you want to use this script to fill the graph of a different GitHub account, follow these steps:

### Step A: Update your Local Identity
GitHub credits "green squares" based on the email address in the commit. You must update this to match the new account’s email.

```powershell
git config user.name "NewAccountUserName"
git config user.email "newaccount-email@example.com"
```

### Step B: Create a New Token
Log into the **new** account and generate a classic Personal Access Token with `repo` permissions.

### Step C: Update the Remote URL
Tell Git to point to the new repository and use the new token.
```powershell
git remote set-url origin https://<NEW_TOKEN>@github.com/<NEW_USERNAME>/<NEW_REPO_NAME>.git
```

### Step D: Run & Push
1. Update `graph_greener.py` with your desired dates.
2. Run: `python graph_greener.py`
3. Push: `git push -u origin master`

---

## 2. What is a Personal Access Token (PAT)?

### Why do we need it?
GitHub no longer allows you to use your **account password** when performing Git operations (like `git push`) from the terminal or a script. This is for security.

### Its Purpose:
- **Security**: If your token is leaked, you can delete it without changing your main GitHub password.
- **Granular Permissions**: You can create a token that only has permission to "push code" but cannot change your account settings or delete repositories.
- **Automation**: Tokens are designed for scripts and tools (like this one) to log into your account securely.

### How to get one:
1. Go to **Settings** > **Developer Settings** > **Personal Access Tokens** > **Tokens (classic)**.
2. Click **Generate new token**.
3. Select the **'repo'** scope.
4. Copy the token immediately (you won't see it again!).

---

## 3. Daily Usage Recap
To add more squares to your current account:
1. Edit `START_DATE`, `END_DATE`, `MAX_COMMITS_PER_DAY`, or `FREQUENCY` in `graph_greener.py`.
2. Save the file.
3. Run: `python graph_greener.py`
4. Run: `git push`
