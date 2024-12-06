 
import sys
import re
from typing import List, Dict

def read_file(filename: str) -> str:
    """
    Читает содержимое файла.
    
    Args:
        filename (str): Путь к файлу
    
    Returns:
        str: Содержимое файла
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        sys.exit(1)

def preprocess_text(text: str) -> List[str]:
    """
    Обрабатывает текст: удаляет пунктуацию, переводит в нижний регистр.
    
    Args:
        text (str): Исходный текст
    
    Returns:
        List[str]: Список слов
    """
    # Удаляем пунктуацию, кроме многоточия
    text = re.sub(r'[^\w\s...]', '', text)
    
    # Разбиваем на слова
    words = text.lower().split()
    
    return words

def main():
    # Проверяем аргументы командной строки
    if len(sys.argv) < 2:
        print("Использование: python word_counter.py <имя_файла>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    # Читаем файл
    text = read_file(input_filename)
    
    # Обрабатываем текст
    words = preprocess_text(text)
    
    print(f"Обработано слов: {len(words)}")

if __name__ == "__main__":
    main()
