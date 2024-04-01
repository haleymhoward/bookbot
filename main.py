def open_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def main():
    frank_path = "books/frankenstein.txt"
    frank_text = open_book(frank_path)
    frank_count = count_words(frank_text)
    print(f"{frank_count} words in document")

main()
    
