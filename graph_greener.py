import os
import sys
import subprocess
from datetime import datetime, timedelta
import random

# Configuration
# Continue from where we left off (May 2023) through end of 2024
START_DATE = datetime(2023, 9, 16) 
END_DATE = datetime(2023, 9, 16)

MAX_COMMITS_PER_DAY = 5
FREQUENCY = 1
FILE_NAME = "contribution.txt"

def remove_lock_file():
    """Removes git index.lock if it exists."""
    lock_file = os.path.join(".git", index.lock")
    if os.path.exists(lock_file):
        print(f"Found lock file {lock_file}, removing it...")
        try:
            os.remove(lock_file)
            print("Lock file removed.")
        except OSError as e:
            print(f"Error removing lock file: {e}")
            sys.exit(1)

def run_command(command, env=None):
    """Runs a shell command."""
    try:
        # Removed output suppression to diagnose errors
        subprocess.run(command, check=True, shell=True, env=env)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        # Stop execution if git fails
        sys.exit(1)

def ensure_git_repo():
    if not os.path.exists(".git"):
        run_command("git init")

def make_commit(date):
    timestamp = date.strftime(f"%Y-%m-%dT{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}")
    
    with open(FILE_NAME, "a") as f:
        f.write(f"Commit for {timestamp}\n")
    
    run_command(f"git add {FILE_NAME}")
    
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = timestamp
    env["GIT_COMMITTER_DATE"] = timestamp
    
    cmd = f'git commit -m "Contribution for {timestamp}"'
    run_command(cmd, env=env)

def main():
    print("Welcome to Graph Greener!")
    
    remove_lock_file()
    
    print(f"Generating contributions from {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}...")
    
    ensure_git_repo()
    
    current_date = START_DATE
    total_commits = 0
    
    while current_date <= END_DATE:
        if random.random() < FREQUENCY:
            num_commits = random.randint(1, MAX_COMMITS_PER_DAY)
            for _ in range(num_commits):
                make_commit(current_date)
                total_commits += 1
            
            if total_commits % 50 == 0:
                 print(f"Progress: {current_date.strftime('%Y-%m-%d')} ({total_commits} commits so far)")
        
        current_date += timedelta(days=1)
        
    print("\nGeneration complete!")
    print(f"Total commits generated: {total_commits}")

if __name__ == "__main__":
    main()
