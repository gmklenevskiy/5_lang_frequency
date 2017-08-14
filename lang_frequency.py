import sys
import os
import re
import collections
NUMBER_OF_FREQUENT_WORDS = 10
n = 1

def load_data(filepath):
    if not os.path.exists(filepath):
        print('The wrong filepath or filename')
        raise SystemExit(n)
    with open(filepath, 'r') as text:
        return text.read().lower()


def get_most_frequent_words(text):
    words = re.findall(r'\w+',str(text))
    return collections.Counter(words).most_common(NUMBER_OF_FREQUENT_WORDS)


if __name__ == '__main__':
    if len(sys.argv)>1:
        filepath = sys.argv[1]
        text = load_data(filepath)
        print('Most frequent words: \n')
        words = get_most_frequent_words(text)
        for word in words:
            print(word)        
    else:
        print("Please, enter the filepath")
