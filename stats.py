def num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Create an empty dictionary to store our character counts
    char_counts = {}

    # Loop through each character in the text
    for char in text:
        # Convert to lowercase
        char = char.lower()

        char_counts[char] = char_counts.get(char, 0) +1
        
    return char_counts

def sort_character_counts(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"character": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list