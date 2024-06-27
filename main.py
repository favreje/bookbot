# Author:   Jeffrey Favret
# Date:     06/26/2024
# Project:  BookBot - provides statistical information about a given book title
# -------------------------------------------------------------------------------------------------

def char_count(book_text):
    """
    Takes text from a book and returns a dict that represents the number of times each character
    appears. The Character counts are case insensitive.
    """

    count_dict = {}
    for c in book_text:
        if not c.isalpha():
            continue
        c = c.lower()
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    return count_dict


def count_words(book_text):
    words = book_text.split()
    return len(words)


def get_book_text(path, book_title):
    with open(path + book_title) as f:
        return f.read()


def main():
    path_to_file = "books/"
    book_title = "frankenstein.txt"
    text = get_book_text(path_to_file, book_title)
    word_count = count_words(text)
    c_count = char_count(text)
    sorted_character_count = dict(sorted(c_count.items(),
                                         key = lambda item: item[1], reverse=True))

    # Report Layout
    print(f"--- Begin report of {book_title}\n")
    print(f"{word_count:,} words found in the document\n")
    for k in sorted_character_count:
        print(f"The {k} character was found {c_count[k]:>6,} times")
    print("\n--- End of report ---")


if __name__ == "__main__":
    main()
