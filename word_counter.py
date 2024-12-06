import sys
import re
from typing import List
from collections import Counter, OrderedDict

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

def analyze_text_statistics(words: List[str], text: str, input_filename: str):
    """Анализирует статистику текста и сохраняет результаты."""
    import os
    os.makedirs('result', exist_ok=True)
    
    # Используем Counter для подсчета слов
    word_counter = Counter(words)
    
    # Сортировка слов по частоте с сохранением порядка появления
    sorted_words = sorted(word_counter.keys(), key=lambda x: (-word_counter[x], words.index(x)))
    
    # Сохраняем статистику слов
    words_filename = f'result/{os.path.basename(input_filename)}_words.txt'
    with open(words_filename, 'w', encoding='utf-8') as f:
        for word in sorted_words:
            f.write(f"{word}: {word_counter[word]}\n")
    
    # Сохраняем общую статистику
    stat_filename = f'result/{os.path.basename(input_filename)}_stat.txt'
    with open(stat_filename, 'w', encoding='utf-8') as f:
        # Уникальные слова
        f.write(f"Количество уникальных слов: {len(word_counter)}\n")
        
        # Статистика по длине слов
        length_stats = Counter(len(word) for word in word_counter.keys())
        f.write("\nКоличество слов по длине:\n")
        for length in sorted(length_stats.keys()):
            f.write(f"{length} буквы: {length_stats[length]}\n")
        
        # Количество знаков препинания
        punctuation_count = len(re.findall(r'[^\w\s]', text))
        f.write(f"\nКоличество знаков препинания: {punctuation_count}\n")

def main():
    if len(sys.argv) < 2:
        print("Использование: python word_counter.py <имя_файла>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    text = read_file(input_filename)
    words = preprocess_text(text)
    
    analyze_text_statistics(words, text, input_filename)
    
    print("Статистика текста успешно сгенерирована.")

if __name__ == "__main__":
    main()
