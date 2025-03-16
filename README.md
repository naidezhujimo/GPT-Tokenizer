# GPT-Tokenizer

## Project Overview

This repository contains two Python scripts implementing Byte Pair Encoding (BPE) tokenization, a technique used in natural language processing to efficiently encode text data. The scripts are designed to demonstrate the core concepts of BPE and provide a basic implementation for educational purposes.

## Scripts

### BPE(GPT2).py

This script reads a text file (`the_verdict.txt`), encodes the text into a UTF-8 byte sequence, and then applies BPE to merge frequent byte pairs into new tokens. The process continues until the desired vocabulary size is reached. The script includes functions for encoding and decoding text using the generated vocabulary.

### simpleTokenizer.py

This script demonstrates a similar BPE tokenization process but uses a predefined text input instead of reading from a file. It includes detailed comments explaining each step of the BPE algorithm, making it easier to understand the implementation. The script also provides functions for encoding and decoding text using the generated vocabulary.

## Usage

### Prerequisites

- Python 3.x
- A text file for input (for `BPE(GPT2).py`)

### Running the Scripts

1. **For `BPE(GPT2).py`:**
   - Place the text file (`the_verdict.txt`) in the same directory as the script.
   - Run the script using Python:
     ```bash
     python BPE(GPT2).py
     ```

2. **For `simpleTokenizer.py`:**
   - Run the script directly:
     ```bash
     python simpleTokenizer.py
     ```

### Example Output

- **Encoding and Decoding:**
  ```plaintext
  Encoded: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
  Decoded: hello world!
  ```

## Features

- **Byte Pair Encoding:** Both scripts implement the BPE algorithm to merge frequent byte pairs.
- **Dynamic Vocabulary Generation:** The vocabulary is dynamically generated based on the input text.
- **Encoding and Decoding Functions:** Each script includes functions to encode text into byte sequences and decode byte sequences back into text.

## Limitations

- The scripts are designed for educational purposes and may not be optimized for large-scale applications.
- The vocabulary size is fixed at 276 tokens, which may not be sufficient for complex text data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
