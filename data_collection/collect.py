# Collect data from Open Library API

# For Khaled Hosseini: https://openlibrary.org/search/authors.json?q=khaled%20hosseini

# Run this through the command line: python collect.py -a "Khaled Hosseini"

import json
import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Fetch author data from Open Library API")
    parser.add_argument("-a", "--author_name", type=str, help="Name of the author to search for")
    args = parser.parse_args()

    author_name = args.author_name
    author_name_for_query = author_name.replace(" ", "%20").lower()
    author_name_for_file = author_name.replace(" ", "_").lower()
    author_data = fetch_author_data(author_name_for_query)

    with open(f"{author_name_for_file}.json", "w") as f:
        json.dump(author_data, f, indent=4)

    print(f"Data for {author_name} saved to {author_name_for_file}.json")

def fetch_author_data(author_name):
    url = f"https://openlibrary.org/search/authors.json?q={author_name}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Successfully fetched data for {author_name}")
        return response.json()

    return {"error": "Failed to fetch data"}

if __name__ == "__main__":
    main()