# Subdomain Permutation Tool

## Overview
The Subdomain Permutation Tool is a Python script designed to generate permutations of subdomains by combining a base subdomain with a list of words provided in a wordlist file. This tool is useful for security professionals, penetration testers, and bug bounty hunters to discover hidden assets and potential attack surfaces.

## Features
- Generates permutations of subdomains by combining base subdomain with words from a wordlist
- Checks the existence of generated subdomains by sending HTTP requests and printing the HTTP status code
- Easy-to-use command-line interface with options to specify base subdomain and wordlist file

## Usage
To use the Subdomain Permutation Tool, follow these steps:
1. Clone the repository to your local machine.
   ```
   git clone https://github.com/example/repository.git
   ```
3. Install the required Python dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Run the script `permuSub.py` with the following command:
   ```
   python permuSub.py -s <base-subdomain> -f <wordlist-file>
   ```
   Replace `<base-subdomain>` with the base subdomain (e.g., `test.domain.com`) and `<wordlist-file>` with the path to the wordlist file containing words to permute.

## Example
Here's an example command to generate subdomain permutations:
```
python permuSub.py -s test.example.com -f wordlist.txt
```

## Requirements
- Python 3
- requests
- argparse

## Files
- `permuSub.py`: The Python script for generating subdomain permutations.
- `requirements.txt`: A text file containing the required Python dependencies.


## Acknowledgments
This tool was inspired by the need to efficiently discover hidden assets during security assessments. Special thanks to the Python community for their valuable contributions.
