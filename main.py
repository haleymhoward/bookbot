def main():
    path = "books/frankenstein.txt"
    file_contents = open_book(path)
    words = count_words(file_contents)
    letters = count_letters(file_contents)
    sorted_dicts = split_n_sort(letters)
    print(f"welcome to bookbot! here is your report for {path}:")
    print()
    print(f"{words} words found in document")
    print()

    for item in sorted_dicts:
        if not item["letter"].isalpha():
            continue
        print(f"The {item['letter']} character was found {item['num']} times")

    print()
    print("thanks for using bookbot! goodbye :)")

def open_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for c in text:
        lower = c.lower()
        if lower in letters:
            letters[lower] += 1
        else:
            letters[lower] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def split_n_sort(d):
    list_of_dicts = [{"letter": key, "num": value} for key, value in d.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

main()
