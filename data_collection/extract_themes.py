import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Extract themes from Open Library author data")
    parser.add_argument("input_file", type=str, help="Path to author JSON file")
    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        data = json.load(f)

    if "docs" not in data or len(data["docs"]) == 0:
        print("No author data found.")
        return

    author_info = data["docs"][0]

    extracted = {
        "author": author_info.get("name"),
        "themes": author_info.get("top_subjects", []),
    }

    output_file = args.input_file.replace(".json", "_theme.json")
    with open(output_file, "w") as f:
        json.dump(extracted, f, indent=4)

    print(f"Extracted theme data saved to {output_file}")

if __name__ == "__main__":
    main()
