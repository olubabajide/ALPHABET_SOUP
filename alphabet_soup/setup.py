
from setuptools import setup, find_packages

setup(
    name="alphabet-soup",
    version="0.1.0",
    description="A reusable word-search solver for newspapers and puzzles.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "alphabet-soup=alphabet_soup.cli:main",
        ],
    },
)
