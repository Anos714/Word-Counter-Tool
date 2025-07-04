import string

def word_counter_tool():
    text = input("Enter your text: ")

    text_clean = text.lower()
    for punctuation in string.punctuation:
        text_clean = text_clean.replace(punctuation, "")

    words = text_clean.split()

    total_words = len(words)
    total_characters = len("".join(words))

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    print("\nTotal words:", total_words)
    print("Total characters (excluding spaces):", total_characters)
    print("Word frequency:")
    for word, count in word_freq.items():
        print(f"  {word}: {count}")

word_counter_tool()
