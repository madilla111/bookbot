def count_words(text):
    dict = {'p':0, 'c': 0, ' ': 0}
    for c in text:
        if c.lower() in dict:
            dict[c.lower()] += 1
    return dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))
    return file_contents
    


main()