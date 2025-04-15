def get_book_text(path):
    with open(path) as f:
        return f.read()

def count(path):
    text = get_book_text(path)
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

def count_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()       
        if char in char_count:
            char_count[char] += 1  # Increment existing count
        else:
            char_count[char] = 1   # Add new character with count 1            
    return char_count
def chars_to_sorted_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=lambda d: d["count"])
    return char_list