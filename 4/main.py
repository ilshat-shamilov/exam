import json
import re
from collections import Counter

def process_book():
    with open('book.txt', 'r') as file:
        text = file.read()
    
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    word_counts = Counter(words)
    top_10 = word_counts.most_common(10)
    result_dict = dict(top_10)
    with open('word_stats.json', 'w') as json_file:
        json.dump(result_dict, json_file, indent=2)

if __name__ == "__main__":
    process_book()