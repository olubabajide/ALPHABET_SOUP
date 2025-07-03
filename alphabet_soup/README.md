

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

### 1. Clone & enter the project Create 
```
git clone https://your.repo.url/alphabet_soup.git
cd alphabet_soup

### 2. Create & activate a virtual environment
```
    python3 -m venv .myenv
for macOS/Linux
    source .myenv/bin/activate
for Windows PowerShell
    .\.myenv\Scripts\Activate.ps1
```
### 3. Install the package

Editable install (for development):
    pip install -e .

Regular install:
    pip install .
**Check if installed and what version installed
    which alphabet-soup
    alphabet-soup --version

#If alphabet-soup isn’t on your $PATH, you can either:
for  macOS/Linux
    echo 'export PATH="$PWD/.myenv/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
for windows Powershel
  add .\.venv\Scripts\Activate.ps1
   

### 4. Usage
    alphabet-soup path/to/puzzle.txt
##Or bypass the wrapper:
    python -m alphabet_soup.cli path/to/puzzle.txt

## Usage

# Use a Virtual Environment. This isolates your Python environment so you can safely install packages:
cd ~/alphabet_soup
python3 -m venv myenv
# Activate your venv from the project root (where setup.py lives):
    source myenv/bin/activate

```bash
alphabet-soup path/to/puzzle.txt

If what you really want is for your shell to “see” the alphabet-soup stub every time you open a terminal, you just need to append its bin-folder to your PATH. Assuming your venv lives at ~/alphabet_soup/myenv, you can do:

# add the venv’s bin dir to YOUR user’s PATH
echo 'export PATH="$HOME/alphabet_soup/myenv/bin:$PATH"' >> ~/.bashrc

# then reload your rc (or just open a new terminal)
source ~/.bashrc

which alphabet-soup
head -n1 $(which alphabet-soup)
alphabet-soup path/to/puzzle.txt

```

## Project Structure

- **src/alphabet_soup/core.py**: Puzzle loading and search algorithms
- **src/alphabet_soup/cli.py**: Entry point and argument parsing
- **tests/**: Unit tests

```bash
pytest
```
```
``` 
