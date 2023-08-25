import re
from collections import Counter

def get_words(text):
    words = re.findall(r'\w+', text.lower())
    return words

def main():
    file_path = 'Random.txt.txt'  
    N = 10  
    with open(file_path, 'r') as file:
        content = file.read()
    
    word_list = get_words(content)
    word_count = Counter(word_list)
    top_words = word_count.most_common(N)

    print(f"Top {N} most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()