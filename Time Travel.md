# Git Time Travel Guide 🕰️🚀

This guide explains how to "fake" the date of your commits so they appear in the past on your GitHub contribution graph.

## The Secret: Metadata Overrides

Every Git commit has two hidden dates:
1. **Author Date**: When the code was originally written.
2. **Committer Date**: When the commit was actually created.

By default, these are both set to "Right Now." To change them, we use **Environment Variables**.

---

## 1. Faking the Date (Powershell)

If you are on Windows, run these commands before committing:

```powershell
# Set the date you want (Format: YYYY-MM-DDTHH:MM:SS)
$env:GIT_AUTHOR_DATE="2023-09-16T12:00:00"
$env:GIT_COMMITTER_DATE="2023-09-16T12:00:00"

# Now any commit you make will look like it happened on that date!
git commit -m "This is a time-traveled commit"
```

---

## 2. Fixing an Existing Commit (`--amend`)

If you already made a commit but it has the "wrong" (current) date, you can fix it:

1. **Set the fake date** (as shown above).
2. **Amendment**: Run `git commit --amend --no-edit`. 
   - This "re-opens" the last commit and injects the new fake date.

---

## 3. Updating GitHub (`--force`)

If you have already pushed the "current date" version to GitHub, the website will try to protect its history. You must force it to accept your time travel:

```powershell
git push --force
```

---

## ⚠️ Important Warning
- **Collaboration**: Never use `--force` on a repository where other people are also working. It can break their local versions.
- **Traceability**: GitHub's API still technically knows when the push actually happened, but the **Contribution Graph** and the **File History** will show your "faked" date. 

Enjoy your green squares! 🟩🟩🟩
