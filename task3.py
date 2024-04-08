def read_words(filename):
    """Read words from the input file."""
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]
    return words

def group_anagrams(words):
    """Group anagrams together."""
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return anagrams.values()

def write_anagrams(anagrams, filename):
    """Write grouped anagrams to the output file."""
    with open(filename, 'w') as file:
        for group in anagrams:
            file.write(' '.join(group) + '\n')

def main():
    input_filename = 'words.txt'
    output_filename = 'anagrams.txt'

    # Step 1: Read words from the input file
    words = read_words(input_filename)

    # Step 2: Group anagrams together
    grouped_anagrams = group_anagrams(words)

    # Step 3: Write grouped anagrams to the output file
    write_anagrams(grouped_anagrams, output_filename)

    print("Anagrams grouped and written to anagrams.txt.")

if __name__ == "__main__":
    main()
