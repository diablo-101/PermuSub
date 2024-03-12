import itertools
import requests
import argparse
from tqdm import tqdm

def check_subdomain_exists(subdomain):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 400:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.RequestException:
        return False, None

def generate_subdomain_permutations(base_subdomain, words):
    permutations = []
    subdomain_parts = base_subdomain.split('.')
    for i in range(len(subdomain_parts) + 1):
        for combo in itertools.permutations(words, i):
            new_subdomain = '.'.join(combo) + '.' + '.'.join(subdomain_parts)
            permutations.append(new_subdomain)
    return permutations

def main():
    parser = argparse.ArgumentParser(description='Subdomain Permutation Tool')
    parser.add_argument('-d', '--domain', required=True, help='Base domain (e.g., test.domain.com)')
    parser.add_argument('-w', '--wordlist', required=True, help='File containing words to permute')
    parser.add_argument('-o', '--output', help='File to save the output')
    args = parser.parse_args()

    with open(args.wordlist, 'r') as file:
        words = file.read().splitlines()

    permutations = generate_subdomain_permutations(args.domain, words)

    if args.output:
        with open(args.output, 'w') as output_file:
            progress_bar = tqdm(permutations, desc="Checking subdomains", unit="subdomain")
            for perm in progress_bar:
                exists, status_code = check_subdomain_exists(perm)
                if exists:
                    output_file.write(f"{perm} - Status code: {status_code}\n")
    else:
        progress_bar = tqdm(permutations, desc="Checking subdomains", unit="subdomain")
        for perm in progress_bar:
            exists, status_code = check_subdomain_exists(perm)
            if exists:
                print(f"{perm} - Status code: {status_code}")

if __name__ == "__main__":
    main()
