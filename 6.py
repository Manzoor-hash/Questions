def words_by_length(word_list, min_length):
    filtered_list = [word for word in word_list if len(word) > min_length]
    return filtered_list

def main():
    word_list = input("Enter a list of words separated by spaces: ").split()
    min_length = int(input("Enter the minimum word length: "))
    
    filtered_words = words_by_length(word_list, min_length)
    
    if filtered_words:
        print("Words longer than", min_length, "characters:", filtered_words)
    else:
        print("No words found longer than", min_length, "characters.")

if __name__ == "__main__":
    main()