import sys
import re
from typing import List, Dict
from collections import OrderedDict

def read_file(filename: str) -> str:
    """Читает содержимое файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        sys.exit(1)

def preprocess_text(text: str) -> List[str]:
    """Обрабатывает текст: удаляет пунктуацию, переводит в нижний регистр."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def count_unique_words(words: List[str]) -> Dict[str, int]:
    """Подсчитывает уникальные слова в порядке появления."""
    word_counts = OrderedDict()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def save_word_statistics(word_counts: Dict[str, int], input_filename: str):
    """Сохраняет статистику слов в файл."""
    import os
    os.makedirs('result', exist_ok=True)
    
    output_filename = f'result/{os.path.basename(input_filename)}_words.txt'
    with open(output_filename, 'w', encoding='utf-8') as f:
        for word, count in word_counts.items():
            f.write(f"{word}: {count}\n")
    
    print(f"Статистика сохранена в {output_filename}")

def main():
    if len(sys.argv) < 2:
        print("Использование: python word_counter.py <имя_файла>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    text = read_file(input_filename)
    words = preprocess_text(text)
    
    word_counts = count_unique_words(words)
    save_word_statistics(word_counts, input_filename)

if __name__ == "__main__":
    main()
