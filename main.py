import sys

# Check if the correct number of arguments were provided

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we get here, we have the correct number of arguments
path_to_book = sys.argv[1]

from stats import num_words, count_characters, sort_character_counts

def main():
    path = path_to_book

    with open(path) as f:
        file_contents = f.read()

    word_count = num_words(file_contents)

    char_counts = count_characters(file_contents)

    sorted_chars = sort_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
