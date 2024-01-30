import string
from collections import Counter

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def word_counter(text):
    if not text:
        return 0

    text = remove_punctuation(text.lower())
    words = text.split()

    stop_words = {"the", "and", "in", "is", "it", "of", "to", "a", "for"}  # Common stop words

    filtered_words = [word for word in words if word not in stop_words]

    return len(filtered_words), Counter(filtered_words)

def main():
    try:
        user_input = input("Enter a sentence or paragraph: ")
        word_count, word_frequency = word_counter(user_input)

        print(f"Word count: {word_count}")

        if word_frequency:
            print("\nWord frequency:")
            for word, count in word_frequency.items():
                print(f"{word}: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()