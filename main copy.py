from stats import get_word_count, char_count
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents=f.read()
    return file_contents

if __name__ == "__main__":
    book = get_book_text('./books/frankenstein.txt')
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f"Found {get_word_count(book)} total words")
    print(char_count(book))
