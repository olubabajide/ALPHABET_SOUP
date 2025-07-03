

# README.md
```markdown
# Alphabet Soup

A reusable, buildable Python package to solve word-search puzzles.

## Features

- Load puzzles from simple text files (e.g. `3x3`, grid lines, then word list)
- Find words in all eight directions (horizontal, vertical, diagonal, forwards & backwards)
- Command-line interface with `--version` flag
- Fully tested core logic

---
## Quickstart
```
### 1. Clone & enter the project Create 

    a. git clone https://your.repo.url/alphabet_soup.git

    b. cd alphabet_soup

### 2. Create & activate a virtual environment. This isolates your Python environment so you can safely install packages
    a. python3 -m venv .myenv
    b. source .myenv/bin/activate          # Activate your venv from the project root (where setup.py lives) for macOS/Linux
    c. .\.myenv\Scripts\Activate.ps1       #for Windows PowerShell

### 3. Install the package
    a. pip install -e .     #Editable install (for development)

    b. pip install .       #Regular install
  ****Check if alphabet-soup was installed and what version installed
  
    c. which alphabet-soup
       
    d. alphabet-soup --version

****If alphabet-soup isn’t on your $PATH, you can either:

    e. echo 'export PATH="$PWD/.myenv/bin:$PATH"' >> ~/.bashrc   ##for  macOS/Linux
    f. source ~/.bashrc                                           ##then reload your rc (or just open a new terminal)
    g. add .\.myenv\Scripts\Activate.ps1                           ##for windows Powershell
   

### 4. Usage
    alphabet-soup path/to/puzzle.txt
    python -m alphabet_soup.cli path/to/puzzle.txt    ##to bypass the wrapper

```
## Project Structure

- **src/alphabet_soup/core.py**: Puzzle loading and search algorithms
- **src/alphabet_soup/cli.py**: Entry point and argument parsing
- **tests/**: Unit tests
- **puzzle_input.txt



