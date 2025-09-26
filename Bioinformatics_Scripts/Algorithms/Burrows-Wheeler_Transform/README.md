# Burrows–Wheeler Transform (Exact Matching)

## Overview
This project implements the Burrows–Wheeler Transform (BWT) for fast substring search. It builds a searchable index from a reference string and uses it to find exact matches of a query string without scanning the entire text. The script is written in Python and can be run as a standalone tool or imported as a module.

## What the Burrows–Wheeler Transform Is
The Burrows–Wheeler Transform is a method for rearranging the letters in a string so that similar letters are grouped together. On its own this rearrangement doesn’t change the information, but it makes the text easier to compress and allows much faster substring searches.

To build a BWT, a special end-of-string marker (usually `$`) is added, and all rotations or suffixes of the string are sorted alphabetically. The transform records the character that appears just before each sorted suffix. This ordering makes it possible to search backwards through the text to find all occurrences of a pattern without scanning the string character by character.

## Why It Matters
In bioinformatics, the BWT is the foundation of many sequence alignment tools such as Bowtie and BWA. These programs align billions of short DNA reads against large genomes quickly by indexing the reference genome with a BWT.  
Outside of biology, the same principle is used in text search engines, data compression tools, and version-control systems — anywhere that fast substring search or efficient storage is needed.

## What This Script Does
This script uses a BWT-based index to locate exact matches of a query string within a reference string. It follows these steps:

1. Builds a suffix array, a sorted list of all suffix positions in the reference.
2. Uses the suffix array to generate the BWT of the reference.
3. Builds two helper tables:
   - `C`: tells where each character’s block begins in the sorted order.
   - `Occ`: tells how many times each character appears up to a given position.
4. Uses backward search to process the query from right to left, updating the search range at each step.  
5. Returns the positions in the original text where the query occurs.

## Example
Reference:
banana

makefile
Copy code
Query:
ana

sql
Copy code

The script appends `$` to the reference (`banana$`), builds the suffix array and BWT, and searches the query from right to left. The positions it returns are `1` and `3`, where `ana` occurs in the reference.

## Installation
Clone the repository or copy the script into your project. No external dependencies are required beyond Python’s standard library.

git clone https://github.com/yourusername/Projects.git
cd Projects/Bioinformatics_Scripts/Algorithms/Burrows-Wheeler_Transform

shell
Copy code

## Usage
Interactive run:
python Burrows-Wheeler_Transform.py

python
Copy code

Within the script:
```python
from Burrows-Wheeler_Transform import find_match
find_match("ana", "banana$")
# -> [1, 3]
Applications
Read alignment in bioinformatics

Full-text search in search engines

Data compression

Efficient storage and retrieval in version-control systems

Future Improvements
Add command-line arguments for easier automation.

Add tests and example datasets.

Extend to handle mismatches and gaps.

Copy code
