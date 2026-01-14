# Graph Greener

An automated utility designed to populate the GitHub contribution matrix through programmatic backdated commits. Built for developers who want to maintain a specific visual aesthetic on their profile.

## How it Works

The script generates a series of historical commits by manipulating the `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables, allowing you to fill in gaps in your activity history.

## Getting Started

1. **Environment**: Ensure you have **Python 3.x** installed.
2. **Configure**: Edit the variables in `graph_greener.py`:
    * `START_DAYS_AGO`: Set the starting point of your history.
    * `MAX_COMMITS_PER_DAY`: Controls the intensity of the green squares.
    * `FREQUENCY`: Adjusts commit density to simulate realistic workflow patterns.
3. **Execution**:
    ```bash
    python graph_greener.py
    ```
4. **Deployment**:
    * Create a new, empty repository on GitHub.
    * Follow the script's terminal output to push the generated local history.

## ⚠️ Disclaimer

This tool is intended for **aesthetic and educational purposes only**. Programmatic activity generation is a common experiment among developers, but it should not be used to misrepresent your actual skill level or professional work history.
