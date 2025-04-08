````markdown
# Unique Integers Processor

A Python program that processes files containing integers and generates output files with unique integers sorted in ascending order.

---

## Overview

This program reads input files with integers (one integer per line), finds all unique integers, sorts them in ascending order, and writes them to output files. It handles special cases like invalid inputs, empty lines, and whitespace.

---

## Features

- Reads integers from input files
- Filters to only unique integers
- Sorts integers in ascending order
- Handles special cases:
  - Whitespace before/after integers
  - Empty lines
  - Lines with multiple integers
  - Non-integer inputs
- Tracks execution time
- Works across all platforms (Windows, macOS, Linux)

---

## Requirements

- Python 3.6 or newer

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/unique-integers-processor.git
```

Navigate to the project directory:

```bash
cd unique-integers-processor
```

Run the program once to create the needed folders:

```bash
python unique_integers_terminal.py
```

---

## Usage

### Interactive Mode

Run the program without arguments for an interactive menu:

```bash
python unique_integers_terminal.py
```

### Command-Line Mode

Process all files in the input folder:

```bash
python unique_integers_terminal.py --all
```

Process a specific file:

```bash
python unique_integers_terminal.py --file sample_inputs/my_file.txt
```

Display help:

```bash
python unique_integers_terminal.py --help
```

---

## Input Format Specifications

- Input files should contain integers, one per line
- Valid integers range from -1023 to 1023

Lines with any of the following will be skipped:

- Non-integer content
- Multiple integers
- Empty lines

---

## Output Format

- Output files will be saved in the `sample_results` folder
- Output filenames follow the pattern: `[input_filename]_results.txt`
- Each output file contains unique integers from the input file, sorted in ascending order

---

## Example

### Input file:

```
5
14
5
-9
62
-1
-9
-9
```

### Output file:

```
-9
-1
5
14
62
```

Note that -9 and 5 only appear once in the output, despite appearing multiple times in the input.

---

## File Structure

```
unique-integers-processor/
├── unique_integers_terminal.py
├── sample_inputs/           # Place input files here
└── sample_results/          # Output files will be generated here
```

---

## Algorithm

The program uses a boolean array approach for tracking seen integers:

- Creates a boolean array covering the range -1023 to 1023
- Marks each valid integer as "seen" in the array
- Outputs the position of each "true" value in the array, naturally producing a sorted result

---

## Performance

The program is optimized for both time and space efficiency:

- **O(n)** time complexity where `n` is the number of lines in the input file
- **O(1)** space complexity as the boolean array size is constant

---

## Contributing

For bug reports or contributions, please open an issue or submit a pull request on GitHub.
````
