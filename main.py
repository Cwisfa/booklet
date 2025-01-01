def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()
        get_total_words(file_contents)
        get_chars_dict(file_contents)

def get_total_words(file):
        words = file.split()
        print(f"The total number of words in this book is {len(words)}.")

def get_chars_dict(file):
     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     totals = {}
     for char in file.lower(): 
          if char not in alphabet:
               continue
          elif char not in totals:
               totals[char] = 1
          else:
               totals[char] += 1
     sorted_totals = sorted(totals.items(), key=lambda item: item[1], reverse=True)
     for char, count in sorted_totals:
          print(f"The character '{char}' appears {count} times.")

main()