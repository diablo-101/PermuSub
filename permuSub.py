import itertools
import requests
import argparse

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
    parser.add_argument('-s', '--subdomain', required=True, help='Base subdomain (e.g., test.domin.com)')
    parser.add_argument('-f', '--wordlist', required=True, help='File containing words to permute')
    args = parser.parse_args()

    with open(args.wordlist, 'r') as file:
        words = file.read().splitlines()

    permutations = generate_subdomain_permutations(args.subdomain, words)

    for perm in permutations:
        exists, status_code = check_subdomain_exists(perm)
        if exists:
            print(f"{perm} - Status code: {status_code}")

if __name__ == "__main__":
    main()
