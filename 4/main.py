"""На вход подаётся текстовый файл book.txt. Программа должна: 
1.	Привести всё к нижнему регистру. 
2.	Удалить знаки препинания. 
3.	Посчитать частоту каждого слова. 
4.	Найти топ-10 самых частых слов. 
5.	Сохранить результат в word_stats.json в виде:
json
1
{"the": 1204, "and": 987, ...}
Дополнительно (для Go): использовать bufio.Scanner для эффективного чтения.
Дополнительно (для Python): использовать collections.Counter.
"""

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