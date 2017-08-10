import sys
import os
import re
import collections

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as text:
        return text.read()
        


def get_most_frequent_words(text):
    result = re.findall(r'\w+',str(text))
    return collections.Counter(result).most_common(10)

if __name__ == '__main__':
    if len(sys.argv)>1:
        filepath = sys.argv[1]
        text = load_data(filepath)
        print('Most frequent words: \n')
        result = get_most_frequent_words(text)
        for word in result:
            print(word)  
    else:
        print("Please, enter the filepath")
