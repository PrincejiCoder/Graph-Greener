# Code Walkthrough: `graph_greener.py` 🧠

This document explains exactly how the automation script works, line by line.

---

## 1. Imports
```python
import os
import sys
import subprocess
from datetime import datetime, timedelta
import random
```
- **`os`**: Used to check if files or folders (like the `.git` folder) exist.
- **`sys`**: Used to exit the script if an error occurs.
- **`subprocess`**: This is the most important one. it allows Python to run terminal commands like `git add` and `git commit`.
- **`datetime`**: Used to handle dates (e.g., Year, Month, Day).
- **`random`**: Used to vary the number of commits and the exact time of each commit so they don't all look the same.

---

## 2. Configuration
```python
START_DATE = datetime(2023, 9, 16) 
END_DATE = datetime(2023, 9, 16)
MAX_COMMITS_PER_DAY = 5
FREQUENCY = 1
FILE_NAME = "contribution.txt"
```
These are variables you can change. 
- **`START_DATE` / `END_DATE`**: The timeframe you want to fill.
- **`MAX_COMMITS_PER_DAY`**: How many commits to make on a single day.
- **`FREQUENCY`**: The probability (0 to 1) that a day will get a commit. `1` means every single day gets a commit.

---

## 3. Function: `remove_lock_file()`
```python
def remove_lock_file():
    lock_file = os.path.join(".git", "index.lock")
    if os.path.exists(lock_file):
        os.remove(lock_file)
```
Git creates a "lock file" when it is busy. If the script crashes, this lock file stays behind and prevents you from making new commits. This function automatically finds and deletes it so the script can continue.

---

## 4. Function: `run_command(command, env)`
```python
def run_command(command, env=None):
    subprocess.run(command, check=True, shell=True, env=env)
```
This is a helper function. Instead of typing `subprocess.run(...)` every time, we use this to execute any terminal command. `check=True` makes sure the script stops if a command fails.

---

## 5. Function: `make_commit(date)`
This is the heart of the script.
```python
timestamp = date.strftime(f"%Y-%m-%dT{random.randint(0, 23):02d}...")
```
1. It creates a random time (Hour:Minute:Second) for the given date.
```python
with open(FILE_NAME, "a") as f:
    f.write(f"Commit for {timestamp}\n")
```
2. It adds a line of text to `contribution.txt`. Git needs a file change to make a commit.
```python
env = os.environ.copy()
env["GIT_AUTHOR_DATE"] = timestamp
env["GIT_COMMITTER_DATE"] = timestamp
```
3. **The "Hack"**: It tells Git, "Don't use today's date. Use this specific date from the past instead."
```python
cmd = f'git commit -m "Contribution for {timestamp}"'
run_command(cmd, env=env)
```
4. It finally runs the commit command.

---

## 6. The Main Loop
```python
while current_date <= END_DATE:
    if random.random() < FREQUENCY:
        num_commits = random.randint(1, MAX_COMMITS_PER_DAY)
        for _ in range(num_commits):
            make_commit(current_date)
            total_commits += 1
    current_date += timedelta(days=1)
```
- It starts at the `START_DATE`.
- For every day until it reaches the `END_DATE`:
    - It checks the `FREQUENCY`.
    - It picks a random number of commits to make.
    - It calls `make_commit()`.
    - It moves to the next day (`+1 day`).

---

## 7. Execution Entry Point
```python
if __name__ == "__main__":
    main()
```
This simply tells Python to start running the `main()` function when the file is opened.
