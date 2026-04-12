# file-hash-generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A simple, dependency-free command-line tool to generate common cryptographic hashes (MD5, SHA-1, and SHA-256) for any file. It streams file contents in chunks, ensuring that very large files (like ISOs or databases) can be handled without overwhelming system memory.

## Features

- **Concurrent Hashing:** Calculates MD5, SHA-1, and SHA-256 simultaneously in a single pass of the file.
- **Memory Efficient:** Processes files in 64KB chunks to preserve RAM.
- **Zero Third-Party Dependencies:** Built entirely with Python's standard `hashlib`, `os`, `sys`, and `argparse` libraries.
- **Colorized Output:** Easily readable CLI formatting.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gbvk312/file-hash-generator.git
   cd file-hash-generator
   ```

*(No virtual environment or extra pip packages are required since it uses the Python standard library!)*

## Usage

Simply pass the path to the file you want to hash:

```bash
python hash_gen.py /path/to/your/file.txt
```

**Example Output:**
```text
Hashes for test_image.png:

MD5    : 9e107d9d372bb6826bd81d3542a419d6
SHA-1  : 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12
SHA-256: d7a8fbb307d2809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
