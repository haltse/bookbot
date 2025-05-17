
 
def get_word_count(book):
    num_words = book.split()
    return len(num_words)
    #return  f"{len(num_words)} words found in the document"

def char_count(book):
    char_dict ={}
    from main import get_book_text
    for chr in book:
        char_dict[chr.lower()] = char_dict.get(chr.lower(), 0) + 1

    return(char_dict)
     

    
        
    
